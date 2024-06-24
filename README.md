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
```

Replace `<your-discord-token>`, `<your-guild-name>`, and `<your-channel-id>` with your actual Discord bot token, server name, and channel ID.

### Step 3: Build and run the Docker container

Build and run the Docker container using Docker Compose:

```sh
docker-compose build
docker-compose up
```

## Usage

The bot will periodically fetch kline data from the Bybit API and calculate the RSI. It will send messages to the Discord channel with RSI updates, advising whether to consider buying or selling based on the RSI value.
