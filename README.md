# TradeClawNewsAI

TradeClawNewsAI is an AI-powered assistant that listens to crypto updates from Telegram channels and automatically posts optimized content to Binance Square, delivering real-time curated market insights to the community.

## Features

- Listens to messages in a Telegram channel.
- Rewrites and optimizes content with AI.
- Posts content to Binance Square automatically.
- Supports logging and monitoring.

## Setup

1. Clone the repo:

```bash
git clone <YOUR_REPO_URL>
cd TradeClawNewsAI
Install dependencies:

pip install -r requirements.txt
Configure your API keys:

Copy config.example.py to config.py

Fill in your Telegram Bot Token, Chat ID, and Binance Square API Key.

Run the bot:

python telegram_listener.py
Usage
The bot listens to the configured Telegram channel and posts new messages automatically.

Check your Binance Square to see the posts.

Logs are printed in the console.

Notes
Only text posts are currently supported.

Make sure your Binance Square API Key is valid and not expired.

Respect daily posting limits to avoid errors.

![imagealt](https://github.com/enessamancioglu/TradeClawNewsAI/blob/main/bot_rewrite.png?raw=true)

