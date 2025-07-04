# Development Guide

This guide covers development setup and processes for the ai-python-lab project.

## Development Setup

### 1. Clone the repository
```bash
git clone https://github.com/n1le-dev/ai-python-lab.git
cd ai-python-lab
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install development dependencies
```bash
pip install -e .
pip install pytest pytest-cov
```

### 4. Set up environment variables
```bash
export OPENROUTER_API_KEY="your-api-key-here"
```

## Running Tests

### Run all tests
```bash
pytest
```

### Run tests with coverage
```bash
pytest --cov=ai_python_lab --cov-report=html
```

### Run specific test file
```bash
pytest tests/test_basic.py
```

## Code Style

### Format code (if using black)
```bash
black ai_python_lab/ tests/ examples/
```

### Check code style (if using flake8)
```bash
flake8 ai_python_lab/ tests/ examples/
```

## Building the Package

### Build distribution packages
```bash
pip install build
python -m build
```

This creates both wheel and source distributions in the `dist/` directory.

### Check the package
```bash
pip install twine
twine check dist/*
```

## Publishing to PyPI

### Test on TestPyPI first
```bash
twine upload --repository testpypi dist/*
```

### Upload to PyPI
```bash
twine upload dist/*
```

## Testing Examples

### Run basic usage examples
```bash
cd examples/
python basic_usage.py
```

## Project Structure

```
ai-python-lab/
├── ai_python_lab/           # Main package
│   ├── __init__.py          # Package initialization
│   ├── openrouter_client.py # Main client implementation
│   └── exceptions.py        # Custom exceptions
├── examples/                # Usage examples
│   └── basic_usage.py       # Basic usage examples
├── tests/                   # Test files
│   └── test_basic.py        # Basic tests
├── README.md                # Main documentation
├── DEVELOPMENT.md           # This file
├── LICENSE                  # MIT license
├── setup.py                 # Setup script
├── pyproject.toml           # Modern package configuration
├── MANIFEST.in              # Package manifest
└── pytest.ini              # Test configuration
```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Add tests for new functionality
5. Run tests: `pytest`
6. Commit your changes: `git commit -am 'Add some feature'`
7. Push to the branch: `git push origin feature-name`
8. Submit a pull request

## Release Process

1. Update version in `ai_python_lab/__init__.py`
2. Update version in `setup.py` if needed
3. Update CHANGELOG.md (if you have one)
4. Create a new git tag: `git tag v0.1.0`
5. Push the tag: `git push origin v0.1.0`
6. Build and upload to PyPI

## API Key Management

For development and testing, you can:

1. Set environment variable: `export OPENROUTER_API_KEY="your-key"`
2. Create a `.env` file (add to `.gitignore`):
   ```
   OPENROUTER_API_KEY=your-key-here
   ```
3. Pass directly to client: `OpenRouterClient(api_key="your-key")`

**Never commit API keys to version control!**

## Useful Commands

### Install package in development mode
```bash
pip install -e .
```

### Uninstall package
```bash
pip uninstall ai-python-lab
```

### Check package info
```bash
pip show ai-python-lab
```

### List installed packages
```bash
pip list
```

## Troubleshooting

### Common Issues

1. **Import errors**: Make sure you've installed the package in development mode (`pip install -e .`)
2. **API key errors**: Verify your OpenRouter API key is set correctly
3. **Test failures**: Ensure all dependencies are installed and API key is configured
4. **Build errors**: Check that all required files are included in MANIFEST.in

### Getting Help

- Check existing issues on GitHub
- Create a new issue with detailed error information
- Include Python version, OS, and package versions in bug reports
