# AgentPo

AgentPo is a simple yet powerful Telegram bot powered by OpenAI's GPT models. It provides intelligent responses and assistance through Telegram's messaging interface.

## Features

- 🤖 OpenAI GPT integration
- 💬 Natural conversation handling
- 👥 Group chat support
- 🔄 Conversation history management
- 🌐 Proxy support
- 🛡️ Access control for users and groups

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/AgentPo.git
cd AgentPo
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy the example environment file and configure your settings:
```bash
cp .env.example .env
```

5. Edit `.env` with your configuration:
- Add your Telegram Bot Token
- Configure OpenAI API key
- Set allowed users and groups
- Configure proxy settings (if needed)

## Usage

1. Start the bot:
```bash
python bot.py
```

2. In Telegram, start a conversation with your bot:
- `/start` - Start the bot
- `/help` - Show available commands
- `/reset` - Reset conversation history
- `/specialty` - Learn about the bot's specialty

## Configuration

The bot can be configured through environment variables in the `.env` file:

- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token
- `OPENAI_API_KEY`: Your OpenAI API key
- `BOT_NAME`: Name of your bot
- `BOT_SPECIALTY`: Bot's area of expertise
- `ALLOWED_GROUP_IDS`: Comma-separated list of allowed group IDs
- `ADMIN_USER_IDS`: Comma-separated list of admin user IDs
- `USE_PROXY`: Enable/disable proxy (true/false)
- `HTTP_PROXY`: HTTP proxy URL
- `HTTPS_PROXY`: HTTPS proxy URL

## Development

The project structure is organized as follows:

```
AgentPo/
├── bot.py                 # Main entry point
├── config/               # Configuration modules
│   ├── base.py          # Base configuration
│   ├── models.py        # AI model settings
│   └── proxy.py         # Proxy settings
├── services/            # Core services
│   ├── ai/             # AI service implementations
│   │   ├── base.py     # Base AI service
│   │   └── openai.py   # OpenAI implementation
│   ├── bot/            # Bot services
│   │   ├── handlers.py # Message handlers
│   │   └── manager.py  # Bot manager
│   └── message.py      # Message processing
├── .env                # Environment configuration
├── .env.example        # Example environment file
└── requirements.txt    # Python dependencies
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [OpenAI](https://openai.com/)
