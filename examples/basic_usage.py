"""
Basic usage examples for ai-python-lab OpenRouter client
"""

import os
from ai_python_lab import OpenRouterClient, quick_chat, ask_ai

# Example 1: Basic client usage
def basic_client_example():
    print("=== Basic Client Example ===")
    
    # Initialize client (make sure OPENROUTER_API_KEY is set)
    client = OpenRouterClient()
    
    # Simple chat
    response = client.simple_chat("What is the meaning of life?")
    print(f"AI: {response}")
    
    # Chat with conversation
    messages = [
        {"role": "user", "content": "Hello, how are you?"},
        {"role": "assistant", "content": "I'm doing well, thank you! How can I help you today?"},
        {"role": "user", "content": "Can you explain quantum computing in simple terms?"}
    ]
    
    response = client.chat(messages)
    print(f"AI: {response}")


# Example 2: Using different models
def different_models_example():
    print("\n=== Different Models Example ===")
    
    client = OpenRouterClient()
    
    question = "What is artificial intelligence?"
    
    # Try different models
    models = [
        "openrouter/cypher-alpha:free",
        "anthropic/claude-3-haiku",
        "openai/gpt-3.5-turbo"
    ]
    
    for model in models:
        try:
            response = client.simple_chat(question, model=model)
            print(f"\n{model}:")
            print(response[:200] + "..." if len(response) > 200 else response)
        except Exception as e:
            print(f"Error with {model}: {e}")


# Example 3: Quick functions
def quick_functions_example():
    print("\n=== Quick Functions Example ===")
    
    # Quick chat function
    response = quick_chat("Tell me a joke")
    print(f"Joke: {response}")
    
    # Even simpler alias
    response = ask_ai("What's the weather like today?")
    print(f"Weather: {response}")


# Example 4: Advanced configuration
def advanced_config_example():
    print("\n=== Advanced Configuration Example ===")
    
    client = OpenRouterClient(
        site_url="https://myapp.com",
        site_name="My AI App",
        default_model="openrouter/cypher-alpha:free"
    )
    
    # Chat with custom parameters
    response = client.chat(
        messages=[{"role": "user", "content": "Write a short poem about coding"}],
        temperature=0.8,
        max_tokens=150,
        top_p=0.9
    )
    print(f"Poem: {response}")


# Example 5: Error handling
def error_handling_example():
    print("\n=== Error Handling Example ===")
    
    from ai_python_lab.exceptions import AuthenticationError, APIError, RateLimitError
    
    try:
        # This will fail if no API key is set
        client = OpenRouterClient(api_key="invalid-key")
        response = client.simple_chat("Hello")
    except AuthenticationError as e:
        print(f"Authentication failed: {e}")
    except RateLimitError as e:
        print(f"Rate limit exceeded: {e}")
    except APIError as e:
        print(f"API error: {e}")


# Example 6: Simple chatbot
def chatbot_example():
    print("\n=== Simple Chatbot Example ===")
    print("Type 'quit' or 'exit' to stop")
    
    client = OpenRouterClient()
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['quit', 'exit']:
            break
        
        try:
            response = client.simple_chat(user_input)
            print(f"AI: {response}")
        except Exception as e:
            print(f"Error: {e}")


# Example 7: Multi-turn conversation
def conversation_example():
    print("\n=== Multi-turn Conversation Example ===")
    print("Type 'quit' or 'exit' to stop")
    
    client = OpenRouterClient()
    conversation = []
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['quit', 'exit']:
            break
        
        # Add user message to conversation
        conversation.append({"role": "user", "content": user_input})
        
        try:
            # Get AI response
            response = client.chat(conversation)
            print(f"AI: {response}")
            
            # Add AI response to conversation
            conversation.append({"role": "assistant", "content": response})
            
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    # Check if API key is set
    if not os.getenv("OPENROUTER_API_KEY"):
        print("Please set the OPENROUTER_API_KEY environment variable")
        print("Example: export OPENROUTER_API_KEY='your-api-key-here'")
        exit(1)
    
    # Run examples
    basic_client_example()
    different_models_example()
    quick_functions_example()
    advanced_config_example()
    error_handling_example()
    
    # Uncomment to run interactive examples
    # chatbot_example()
    # conversation_example()
