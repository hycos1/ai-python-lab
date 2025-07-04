"""
Exceptions for OpenRouter API client
"""


class OpenRouterError(Exception):
    """Base exception for OpenRouter API errors"""
    pass


class APIError(OpenRouterError):
    """Exception raised when API returns an error response"""
    
    def __init__(self, message, status_code=None, response_data=None):
        super().__init__(message)
        self.status_code = status_code
        self.response_data = response_data


class AuthenticationError(OpenRouterError):
    """Exception raised when authentication fails"""
    pass


class RateLimitError(OpenRouterError):
    """Exception raised when rate limit is exceeded"""
    pass


class ModelNotFoundError(OpenRouterError):
    """Exception raised when specified model is not found"""
    pass
