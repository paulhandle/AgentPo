"""Telegram bot message handlers."""
import logging
from typing import Dict, Set

from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode

from config import base
from services.message import MessageHandler
from services.ai.openai import OpenAIService

logger = logging.getLogger(__name__)

# Initialize services
message_handler = MessageHandler()
ai_service = OpenAIService()

# Track user conversations
user_contexts: Dict[int, list] = {}
active_users: Set[int] = set()

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /start command."""
    user = update.effective_user
    welcome_message = (
        f"👋 Hello {user.first_name}! I'm {base.BOT_NAME}, "
        f"specialized in {base.BOT_SPECIALTY}.\n\n"
        "I can help you with:\n"
        "• One-on-one conversations\n"
        "• Group chat support (when mentioned)\n"
        "• Specialized assistance in my domain\n\n"
        "Feel free to ask me anything related to my specialty!"
    )
    await update.message.reply_text(welcome_message)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /help command."""
    help_text = (
        "🔍 Available Commands:\n"
        "/start - Start a conversation\n"
        "/help - Show this help message\n"
        "/reset - Reset conversation history\n"
        "/specialty - Learn about my specialty\n\n"
        "You can also just send me a message and I'll respond!"
    )
    await update.message.reply_text(help_text)

async def reset_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Reset the conversation history for a user."""
    user_id = update.effective_user.id
    user_contexts[user_id] = []
    await update.message.reply_text("🔄 Conversation history has been reset!")

async def specialty_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show the bot's specialty."""
    specialty_text = (
        f"🌟 My Specialty: {base.BOT_SPECIALTY}\n\n"
        f"{base.BOT_SPECIALTY_DESCRIPTION}"
    )
    await update.message.reply_text(specialty_text)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle incoming messages."""
    # Ignore messages from unauthorized groups
    if (update.effective_chat.type != 'private' and 
        update.effective_chat.id not in base.ALLOWED_GROUP_IDS):
        return

    # In groups, only respond when mentioned
    if (update.effective_chat.type != 'private' and 
        not message_handler.is_bot_mentioned(update, context.bot)):
        return

    user_id = update.effective_user.id
    message_text = message_handler.clean_message(update.message.text, context.bot)

    try:
        # Get or initialize conversation history
        conversation = user_contexts.get(user_id, [])
        
        # Get AI response
        response = ai_service.get_response(message_text, conversation)
        
        # Update conversation history
        conversation.extend([
            {"role": "user", "content": message_text},
            {"role": "assistant", "content": response}
        ])
        user_contexts[user_id] = conversation[-10:]  # Keep last 10 messages
        
        # Send response
        await update.message.reply_text(
            response,
            parse_mode=ParseMode.MARKDOWN
        )
        
    except Exception as e:
        logger.error(f"Error handling message: {e}")
        await update.message.reply_text(
            "😔 I encountered an error processing your request. Please try again later."
        )
