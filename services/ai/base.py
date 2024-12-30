"""Base class for AI services."""
from abc import ABC, abstractmethod
from typing import List, Dict

class BaseAIService(ABC):
    """Abstract base class for AI services."""
    
    @abstractmethod
    def get_response(
        self,
        message: str,
        conversation_history: List[Dict[str, str]] = None
    ) -> str:
        """
        Get response from AI model.
        
        Args:
            message: User message
            conversation_history: Previous conversation messages
            
        Returns:
            AI response
        """
        pass
