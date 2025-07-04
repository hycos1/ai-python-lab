"""
AI Python Lab - Simple OpenRouter API Client

A simple and easy-to-use client for OpenRouter API that provides access to various AI models.
"""

from .openrouter_client import OpenRouterClient
from .exceptions import OpenRouterError, APIError, AuthenticationError

__version__ = "0.1.0"
__all__ = ["OpenRouterClient", "OpenRouterError", "APIError", "AuthenticationError"]
