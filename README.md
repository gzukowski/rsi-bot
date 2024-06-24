# Discord RSI Bot

This is a Discord bot that fetches kline data from the Bybit API, calculates the Relative Strength Index (RSI), and sends messages to a Discord channel with RSI updates.

## Setup Instructions

### Prerequisites

- Docker
- A Discord bot token
- A Discord server (guild) ID
- A Discord channel ID

### Step 1: Discord Bot Configuration

1. **Create a Discord Bot:**
    - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
    - Click on "New Application".
    - Give your application a name and click "Create".
    - Go to the "Bot" tab on the left sidebar.
    - Reset the token and copy it for your .env file.

2. **Invite Your Bot to Your Server:**
    - Go to the "OAuth2" tab on the left sidebar.
    - Select "bot" for url generator.
    - Select "Send Messages" and "Mention Everyone" in bot permissions.
    - Copy the generated url and paste it into your browser.
    - Select the certain server.

3. **Get Your Server and Channel ID:**
    - Enable Developer Mode in Discord by going to User Settings > Advanced > Developer Mode.
    - Right-click your server icon and click "Copy ID" to get your server (guild) ID.
    - Navigate to the channel where you want the bot to send messages, right-click the channel name, and click "Copy ID" to get your channel ID.

### Step 2: Clone the Repository

```sh
git clone <your-repo-url>
cd <your-repo-directory>
```

### Step 3: Create a `.env` File

Create a `.env` file in the root directory and fill it with the following content:

```env
DISCORD_TOKEN=<your-discord-token>
DISCORD_GUILD=<your-guild-id>
DISCORD_CHANNEL_ID=<your-channel-id>
RSI_PERIOD=<selected-rsi-period>
```

Replace `<your-discord-token>`, `<your-guild-id>`, `<your-channel-id>`, and `<selected-rsi-period>` with your actual Discord bot token, server ID, and channel ID. 

#### Example RSI Periods
The RSI can be calculated over various periods depending on your trading strategy. Here are some common periods:

- **14-day RSI**: Standard period, widely used in most analyses.
- **9-day RSI**: Popular in short-term trading.
- **7-day RSI**: Used for very short-term trading, providing more sensitive indicators.
- **2-5 day RSI**: Very short-term strategies, suitable for high volatility and day trading.

### Step 4: Build and Run the Docker Container

Build and run the Docker container using Docker Compose:

```sh
docker-compose build
docker-compose up
```
Successful run should look like this:
![image](https://github.com/gzukowski/rsi-bot/assets/85632612/6aa116ed-02d3-4705-8a12-1939e86451d0)


## Usage

The bot will periodically fetch kline data from the Bybit API and calculate the RSI. It will send messages to the Discord channel with RSI updates, advising whether to consider buying or selling based on the RSI value.
