"""
Basic tests for ai-python-lab OpenRouter client
"""

import pytest
import os
from unittest.mock import Mock, patch
from ai_python_lab import OpenRouterClient, quick_chat, ask_ai
from ai_python_lab.exceptions import AuthenticationError, APIError


class TestOpenRouterClient:
    """Test cases for OpenRouterClient"""
    
    def test_init_without_api_key(self):
        """Test initialization without API key raises AuthenticationError"""
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(AuthenticationError):
                OpenRouterClient()
    
    def test_init_with_api_key(self):
        """Test initialization with API key"""
        client = OpenRouterClient(api_key="test-key")
        assert client.api_key == "test-key"
        assert client.base_url == "https://openrouter.ai/api/v1"
        assert client.default_model == "openrouter/cypher-alpha:free"
    
    def test_init_with_env_var(self):
        """Test initialization with environment variable"""
        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "env-key"}):
            client = OpenRouterClient()
            assert client.api_key == "env-key"
    
    def test_init_with_custom_params(self):
        """Test initialization with custom parameters"""
        client = OpenRouterClient(
            api_key="test-key",
            site_url="https://example.com",
            site_name="Test Site",
            default_model="custom-model"
        )
        assert client.site_url == "https://example.com"
        assert client.site_name == "Test Site"
        assert client.default_model == "custom-model"
    
    def test_get_headers_empty(self):
        """Test _get_headers with no site info"""
        client = OpenRouterClient(api_key="test-key")
        headers = client._get_headers()
        assert headers == {}
    
    def test_get_headers_with_site_info(self):
        """Test _get_headers with site info"""
        client = OpenRouterClient(
            api_key="test-key",
            site_url="https://example.com",
            site_name="Test Site"
        )
        headers = client._get_headers()
        assert headers["HTTP-Referer"] == "https://example.com"
        assert headers["X-Title"] == "Test Site"
    
    @patch('ai_python_lab.openrouter_client.OpenAI')
    def test_simple_chat(self, mock_openai):
        """Test simple_chat method"""
        # Mock the OpenAI client and response
        mock_client = Mock()
        mock_openai.return_value = mock_client
        
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = "Test response"
        mock_client.chat.completions.create.return_value = mock_response
        
        client = OpenRouterClient(api_key="test-key")
        response = client.simple_chat("Hello")
        
        assert response == "Test response"
        mock_client.chat.completions.create.assert_called_once()
    
    @patch('ai_python_lab.openrouter_client.OpenAI')
    def test_chat_with_messages(self, mock_openai):
        """Test chat method with message history"""
        mock_client = Mock()
        mock_openai.return_value = mock_client
        
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = "Test response"
        mock_client.chat.completions.create.return_value = mock_response
        
        client = OpenRouterClient(api_key="test-key")
        messages = [{"role": "user", "content": "Hello"}]
        response = client.chat(messages)
        
        assert response == "Test response"
        mock_client.chat.completions.create.assert_called_once()


class TestQuickFunctions:
    """Test cases for quick functions"""
    
    @patch('ai_python_lab.openrouter_client.OpenRouterClient')
    def test_quick_chat(self, mock_client_class):
        """Test quick_chat function"""
        mock_client = Mock()
        mock_client_class.return_value = mock_client
        mock_client.simple_chat.return_value = "Test response"
        
        response = quick_chat("Hello", api_key="test-key")
        
        assert response == "Test response"
        mock_client_class.assert_called_once_with(api_key="test-key", default_model="openrouter/cypher-alpha:free")
        mock_client.simple_chat.assert_called_once_with("Hello")
    
    @patch('ai_python_lab.openrouter_client.quick_chat')
    def test_ask_ai(self, mock_quick_chat):
        """Test ask_ai function"""
        mock_quick_chat.return_value = "Test response"
        
        response = ask_ai("Hello")
        
        assert response == "Test response"
        mock_quick_chat.assert_called_once_with("Hello")


class TestErrorHandling:
    """Test cases for error handling"""
    
    def test_handle_authentication_error(self):
        """Test _handle_error with authentication error"""
        client = OpenRouterClient(api_key="test-key")
        
        with pytest.raises(AuthenticationError):
            client._handle_error(Exception("401 Unauthorized"))
    
    def test_handle_rate_limit_error(self):
        """Test _handle_error with rate limit error"""
        from ai_python_lab.exceptions import RateLimitError
        
        client = OpenRouterClient(api_key="test-key")
        
        with pytest.raises(RateLimitError):
            client._handle_error(Exception("429 Too Many Requests"))
    
    def test_handle_api_error(self):
        """Test _handle_error with generic API error"""
        client = OpenRouterClient(api_key="test-key")
        
        with pytest.raises(APIError):
            client._handle_error(Exception("500 Internal Server Error"))


if __name__ == "__main__":
    pytest.main([__file__])
