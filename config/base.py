"""Base configuration for the Telegram AI Bot."""
import os
from typing import List
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Telegram Configuration
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
BOT_NAME = os.getenv('BOT_NAME', 'AICustomerServiceBot')

# Parse comma-separated lists
ALLOWED_GROUP_IDS: List[int] = [
    int(id_) for id_ in os.getenv('ALLOWED_GROUP_IDS', '').split(',')
    if id_.strip()
]
ADMIN_USER_IDS: List[int] = [
    int(id_) for id_ in os.getenv('ADMIN_USER_IDS', '').split(',')
    if id_.strip()
]

# Bot Specialty Configuration
BOT_SPECIALTY = os.getenv('BOT_SPECIALTY', 'customer_service')
BOT_SPECIALTY_DESCRIPTION = os.getenv(
    'BOT_SPECIALTY_DESCRIPTION',
    "I am a customer service expert specializing in technical support and product inquiries."
)

# System message for AI
SYSTEM_MESSAGE = f"""You are {BOT_NAME}, a specialized AI assistant focusing on {BOT_SPECIALTY}.
{BOT_SPECIALTY_DESCRIPTION}

Guidelines:
1. Be professional, courteous, and helpful
2. Keep responses concise but informative
3. If you're unsure, acknowledge it and suggest alternatives
4. Maintain a friendly tone while remaining professional
5. Use appropriate emojis sparingly to enhance communication
6. If a question is outside your expertise, politely say so
7. Always prioritize accuracy over speculation

Current Specialty: {BOT_SPECIALTY}"""
