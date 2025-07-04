from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r', encoding='utf-8') as f:
    return f.read()


setup(
  name='ai-python-lab',
  version='0.1.0',
  author='n1le.dev',
  author_email='n1le.dev@gmail.com',
  description='Simple and easy-to-use Python client for OpenRouter API that provides access to various AI models.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/hycos1/ai-python-lab',
  packages=find_packages(),
  install_requires=[
    'openai>=1.0.0',
    'requests>=2.25.1'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Software Development :: Libraries :: Python Modules'
  ],
  keywords='openrouter ai gpt claude anthropic openai chatbot api client artificial intelligence',
  project_urls={
    'Bug Reports': 'https://github.com/hycos1/ai-python-lab/issues',
    'Source': 'https://github.com/hycos1/ai-python-lab',
    'Documentation': 'https://github.com/hycos1/ai-python-lab#readme'
  },
  python_requires='>=3.7'
)
