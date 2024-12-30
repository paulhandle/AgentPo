"""Main entry point for the Telegram AI Bot."""
import logging
from services.bot.manager import BotManager

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main():
    """Start the bot."""
    bot_manager = BotManager()
    bot_manager.run()

if __name__ == '__main__':
    main()
