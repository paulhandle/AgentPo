"""Telegram bot manager."""
import signal
import sys
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler as TelegramMessageHandler,
    filters
)

from config import base, proxy
from . import handlers

class BotManager:
    """Manager class for the Telegram bot."""
    
    def __init__(self):
        """Initialize the bot manager."""
        self.application = None
        
    def setup(self):
        """Set up the bot application."""
        # Configure proxy settings
        proxy_url = proxy.HTTP_PROXY if proxy.USE_PROXY else None
        
        # Create the Application with proxy
        self.application = (
            Application.builder()
            .token(base.TELEGRAM_BOT_TOKEN)
            .proxy_url(proxy_url)
            .get_updates_proxy_url(proxy_url)
            .build()
        )

        # Add handlers
        self.application.add_handler(CommandHandler("start", handlers.start_command))
        self.application.add_handler(CommandHandler("help", handlers.help_command))
        self.application.add_handler(CommandHandler("reset", handlers.reset_command))
        self.application.add_handler(CommandHandler("specialty", handlers.specialty_command))
        self.application.add_handler(
            TelegramMessageHandler(filters.TEXT & ~filters.COMMAND, handlers.handle_message)
        )
        
    def signal_handler(self, signum, frame):
        """Handle shutdown signals."""
        print("\nReceived signal to terminate. Shutting down gracefully...")
        if self.application:
            self.application.stop_running()
        sys.exit(0)
        
    def run(self):
        """Start the bot."""
        if not self.application:
            self.setup()
            
        # Set up signal handlers
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
            
        print("Starting bot...")
        try:
            self.application.run_polling(
                allowed_updates=Update.ALL_TYPES,
                close_loop=False
            )
        except Exception as e:
            print(f"Error running bot: {e}")
            raise
