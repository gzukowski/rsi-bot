import os
import discord
import requests
import pandas as pd
import ta
from discord.ext import tasks
from dotenv import load_dotenv

BYBIT_API_URL = 'https://api-testnet.bybit.com/v5/\
market/kline?symbol=SOLUSDT&interval=60'


class DiscordBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        load_dotenv()
        self.TOKEN = os.getenv('DISCORD_TOKEN')

    def fetch_kline_data(self):
        try:
            response = requests.get(BYBIT_API_URL)
            response.raise_for_status()
            data = response.json()
            return data['result']
        except requests.RequestException as e:
            print(f"Error fetching data from Bybit API: {e}")
            return None

    def calculate_rsi(self, data, period=14):
        df = pd.DataFrame(data)
        df['close'] = df['list'].apply(lambda x: x[4])
        df['close'] = df['close'].astype(float)
        rsi = ta.momentum.RSIIndicator(df['close'], window=period)
        return rsi.rsi().iloc[-1]

    @tasks.loop(seconds=5)
    async def update(self) -> None:
        data = self.fetch_kline_data()
        if data is not None:
            rsi = self.calculate_rsi(data)
            if rsi is not None:
                if rsi > 70:
                    message = f'RSI is over 70: {rsi:.2f}. Consider selling.'
                elif rsi < 30:
                    message = f'RSI is below 30: {rsi:.2f}. Consider buying.'
                else:
                    message = f'RSI is currently {rsi:.2f}.'

                try:
                    await self.channel.send(message)
                except discord.DiscordException as e:
                    print(f"Error sending message to Discord: {e}")

    @update.before_loop
    async def before_update(self) -> None:
        """
        Making sure bot is ready before setting the guild and channel.
        """
        await self.wait_until_ready()

    def set_channel(self) -> None:
        for channel in self.guild.channels:
            if channel.id == os.getenv('DISCORD_CHANNEL_ID'):
                break

        self.channel = channel

    def set_guild(self) -> None:
        for guild in self.guilds:
            if guild.name == os.getenv('DISCORD_GUILD'):
                break

        self.guild = guild

    async def on_ready(self):
        self.set_guild()
        self.set_channel()

    async def setup_hook(self) -> None:
        """
        This will just be executed when the bot starts.
        """
        print(f"Logged in as {self.user.name}")
        self.update.start()


intents = discord.Intents.default()
client = DiscordBot(intents=intents)
client.run(client.TOKEN)
