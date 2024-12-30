"""OpenAI service implementation."""
from typing import List, Dict
import httpx
from openai import OpenAI

from config import models, proxy
from config.base import SYSTEM_MESSAGE
from .base import BaseAIService

class OpenAIService(BaseAIService):
    """Service for handling OpenAI interactions."""
    
    def __init__(self):
        """Initialize the OpenAI service."""
        # Configure proxy if enabled
        proxy_config = proxy.get_proxy_config()
        http_client = httpx.Client(
            proxy=proxy_config['http'] if proxy_config else None
        )
        
        # Initialize OpenAI client
        self.client = OpenAI(
            api_key=models.OPENAI_CONFIG['api_key'],
            http_client=http_client
        )
        self.config = models.OPENAI_CONFIG
        
    def get_response(
        self,
        message: str,
        conversation_history: List[Dict[str, str]] = None
    ) -> str:
        """Get response from OpenAI."""
        # Prepare messages
        messages = [{"role": "system", "content": SYSTEM_MESSAGE}]
        
        # Add conversation history if available
        if conversation_history:
            messages.extend(conversation_history)
            
        # Add current message
        messages.append({"role": "user", "content": message})
        
        try:
            # Get completion from OpenAI
            response = self.client.chat.completions.create(
                model=self.config['model'],
                messages=messages,
                temperature=self.config['temperature'],
                max_tokens=self.config['max_tokens']
            )
            
            # Extract and return the response text
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            raise Exception(f"Error getting OpenAI response: {str(e)}")
