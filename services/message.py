"""Message handling service for the Telegram bot."""
from telegram import Update, Bot

class MessageHandler:
    """Service for handling message processing."""
    
    def clean_message(self, message: str, bot: Bot) -> str:
        """
        Clean the message text by removing bot mentions and extra whitespace.
        
        Args:
            message: The original message text
            bot: The bot instance
            
        Returns:
            Cleaned message text
        """
        # Remove bot username/mention if present
        if bot.username:
            message = message.replace(f"@{bot.username}", "")
            
        # Clean and return
        return message.strip()
    
    def is_bot_mentioned(self, update: Update, bot: Bot) -> bool:
        """
        Check if the bot is mentioned in the message.
        
        Args:
            update: The update object
            bot: The bot instance
            
        Returns:
            True if bot is mentioned, False otherwise
        """
        if not update.message or not update.message.text:
            return False
            
        # Check for bot username in message
        if bot.username and f"@{bot.username}" in update.message.text:
            return True
            
        # Check for bot mention in entities
        if update.message.entities:
            for entity in update.message.entities:
                if entity.type == "mention":
                    mention = update.message.text[
                        entity.offset:entity.offset + entity.length
                    ]
                    if mention == f"@{bot.username}":
                        return True
                        
        return False
