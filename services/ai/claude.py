"""Claude service implementation."""
from typing import List, Dict
import httpx
import anthropic

from config import models, proxy
from config.base import SYSTEM_MESSAGE
from .base import BaseAIService

class ClaudeService(BaseAIService):
    """Service for handling Claude interactions."""
    
    def __init__(self):
        """Initialize the Claude service."""
        config = models.get_model_config(models.ModelType.CLAUDE)
        proxy_config = proxy.get_proxy_config()
        
        # Initialize client with proxy if configured
        self.client = anthropic.Anthropic(
            api_key=config['api_key'],
            http_client=httpx.Client(proxies=proxy_config) if proxy_config else None
        )
        self.config = config
        
    def get_response(
        self,
        message: str,
        conversation_history: List[Dict[str, str]] = None
    ) -> str:
        """Get response from Claude."""
        try:
            # Prepare messages
            system = SYSTEM_MESSAGE
            
            # Format conversation history
            history = ""
            if conversation_history:
                for msg in conversation_history:
                    role_prefix = "Human: " if msg["role"] == "user" else "Assistant: "
                    history += f"{role_prefix}{msg['content']}\n\n"
            
            # Create the complete prompt
            prompt = f"{system}\n\n{history}Human: {message}\n\nAssistant:"
            
            # Get completion from Claude
            response = self.client.messages.create(
                model=self.config['model'],
                max_tokens=self.config['max_tokens'],
                temperature=self.config['temperature'],
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            return response.content[0].text.strip()
            
        except Exception as e:
            raise Exception(f"Error getting Claude response: {str(e)}")
