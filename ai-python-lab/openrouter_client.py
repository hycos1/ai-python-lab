"""
OpenRouter API Client

A simple client for interacting with OpenRouter API using the OpenAI Python library.
"""

import os
from typing import Dict, List, Optional, Any, Union
from openai import OpenAI
from .exceptions import OpenRouterError, APIError, AuthenticationError, RateLimitError


class OpenRouterClient:
    """
    A client for interacting with OpenRouter API.
    
    This client provides a simple interface to send messages to various AI models
    available through OpenRouter.
    """
    
    def __init__(
        self,
        api_key = "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",
        base_url: str = "https://openrouter.ai/api/v1",
        default_model: str = "openrouter/cypher-alpha:free"
    ):
        """
        Initialize the OpenRouter client.
        
        Args:
            api_key: OpenRouter API key. If not provided, will look for OPENROUTER_API_KEY env var.
            base_url: Base URL for OpenRouter API. Defaults to "https://openrouter.ai/api/v1".
            site_url: Your site URL for rankings on openrouter.ai (optional).
            site_name: Your site name for rankings on openrouter.ai (optional).
            default_model: Default model to use if not specified in requests.
        """
        self.api_key = api_key
        if not self.api_key:
            raise AuthenticationError("API key is required. Set OPENROUTER_API_KEY environment variable or pass api_key parameter.")
        
        self.base_url = base_url
        self.default_model = default_model
        
        # Initialize OpenAI client with OpenRouter configuration
        self.client = OpenAI(
            base_url=self.base_url,
            api_key=self.api_key
        )
    
    def _get_headers(self) -> Dict[str, str]:
        """Get headers for API requests."""
        headers = {}
        return headers
    
    def chat(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        top_p: float = 1.0,
        frequency_penalty: float = 0.0,
        presence_penalty: float = 0.0,
        stop: Optional[Union[str, List[str]]] = None,
        **kwargs
    ) -> str:
        """
        Send a chat completion request to OpenRouter.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content' keys.
            model: Model to use. If not specified, uses default_model.
            temperature: Sampling temperature (0.0 to 2.0).
            max_tokens: Maximum number of tokens to generate.
            top_p: Nucleus sampling parameter.
            frequency_penalty: Frequency penalty (-2.0 to 2.0).
            presence_penalty: Presence penalty (-2.0 to 2.0).
            stop: Stop sequences.
            **kwargs: Additional parameters to pass to the API.
            
        Returns:
            The generated text response.
            
        Raises:
            APIError: If the API returns an error.
            AuthenticationError: If authentication fails.
            RateLimitError: If rate limit is exceeded.
        """
        try:
            response = self.client.chat.completions.create(
                model=model or self.default_model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=top_p,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty,
                stop=stop,
                extra_headers=self._get_headers(),
                extra_body={},
                **kwargs
            )
            return response.choices[0].message.content
        except Exception as e:
            self._handle_error(e)
    
    def simple_chat(
        self,
        message: str,
        model: Optional[str] = None,
        **kwargs
    ) -> str:
        """
        Send a simple chat message to OpenRouter.
        
        Args:
            message: The message to send.
            model: Model to use. If not specified, uses default_model.
            **kwargs: Additional parameters to pass to the chat method.
            
        Returns:
            The generated text response.
        """
        messages = [{"role": "user", "content": message}]
        return self.chat(messages, model=model, **kwargs)
    
    def get_models(self) -> List[Dict[str, Any]]:
        """
        Get list of available models from OpenRouter.
        
        Returns:
            List of model dictionaries.
        """
        try:
            response = self.client.models.list()
            return [model.dict() for model in response.data]
        except Exception as e:
            self._handle_error(e)
    
    def _handle_error(self, error: Exception) -> None:
        """Handle API errors and convert them to appropriate exceptions."""
        error_message = str(error)
        
        if "401" in error_message or "authentication" in error_message.lower():
            raise AuthenticationError(f"Authentication failed: {error_message}")
        elif "429" in error_message or "rate limit" in error_message.lower():
            raise RateLimitError(f"Rate limit exceeded: {error_message}")
        elif "404" in error_message or "not found" in error_message.lower():
            raise APIError(f"Model not found: {error_message}")
        else:
            raise APIError(f"API error: {error_message}")


# Convenience functions for quick usage
def quick_chat(
    message: str,
    api_key: Optional[str] = None,
    model: str = "openrouter/cypher-alpha:free",
    **kwargs
) -> str:
    """
    Quick chat function for simple one-off requests.
    
    Args:
        message: The message to send.
        api_key: OpenRouter API key. If not provided, will look for OPENROUTER_API_KEY env var.
        model: Model to use.
        **kwargs: Additional parameters to pass to the chat method.
        
    Returns:
        The generated text response.
    """
    client = OpenRouterClient(api_key=api_key, default_model=model)
    return client.simple_chat(message, **kwargs)


def ask_ai(message: str, **kwargs) -> str:
    """
    Simple alias for quick_chat with a more intuitive name.
    
    Args:
        message: The message to send.
        **kwargs: Additional parameters to pass to quick_chat.
        
    Returns:
        The generated text response.
    """
    return quick_chat(message, **kwargs)
