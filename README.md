# Discord RSI Bot

This is a Discord bot that fetches kline data from the Bybit API, calculates the Relative Strength Index (RSI), and sends messages to a Discord channel with RSI updates.

## Setup Instructions

### Prerequisites

- Docker
- A Discord bot token
- A Discord server (guild) ID
- A Discord channel ID

### Step 1: Clone the repository

```sh
git clone <your-repo-url>
cd <your-repo-directory>
```

### Step 2: Create a `.env` file

Create a `.env` file in the root directory and fill it with the reference to .env-example file:

```env
DISCORD_TOKEN=<your-discord-token>
DISCORD_GUILD=<your-guild-name>
DISCORD_CHANNEL_ID=<your-channel-id>
RSI_PERIOD=<selected rsi period>
```

Replace `<your-discord-token>`, `<your-guild-name>`, `<your-channel-id>` and `<selected rsi period>` with your actual Discord bot token, server name, and channel ID. Some RSI period suggestions.

#### Example RSI Periods
The RSI can be calculated over various periods depending on your trading strategy. Here are some common periods:

14-day RSI: Standard period, widely used in most analyses.
9-day RSI: Popular in short-term trading.
7-day RSI: Used for very short-term trading, providing more sensitive indicators.
2-5 day RSI: Very short-term strategies, suitable for high volatility and day trading

### Step 3: Build and run the Docker container

Build and run the Docker container using Docker Compose:

```sh
docker-compose build
docker-compose up
```

## Usage

The bot will periodically fetch kline data from the Bybit API and calculate the RSI. It will send messages to the Discord channel with RSI updates, advising whether to consider buying or selling based on the RSI value.
