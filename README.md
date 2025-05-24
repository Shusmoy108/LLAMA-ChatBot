# Personal Chatbot with Llama 2

A powerful chatbot application built with Llama 2 7B model, featuring a user-friendly Streamlit web interface. This project allows you to have natural conversations with an AI assistant powered by the Llama 2 language model.

## Features

- 🤖 Powered by Llama 2 7B Chat model
- 💬 Interactive chat interface using Streamlit
- 🎯 Context-aware conversations
- 🧹 Easy conversation clearing
- 📝 Markdown support in responses
- 🚀 Fast and efficient using llama.cpp

## Prerequisites

- Python 3.8 or higher
- Sufficient disk space for the model (approximately 2.6GB)
- CUDA-capable GPU (optional, but recommended for better performance)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd ChatBot
download llama model from https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q2_K.gguf
```

2. Run the setup script to create a virtual environment and install dependencies:
```bash
./setup.sh
```

3. Activate the virtual environment:
```bash
source venv/bin/activate  # On Unix/macOS
# or
.\venv\Scripts\activate  # On Windows
```

## Usage

1. Start the chatbot application:
```bash
./runchat.sh
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Start chatting with the AI assistant!

## Project Structure

- `app.py` - Main application file containing the Streamlit interface and chat logic
- `requirements.txt` - Python dependencies
- `setup.sh` - Setup script for environment and dependencies
- `runchat.sh` - Script to run the chatbot
- `llama-2-7b-chat.Q2_K.gguf` - The Llama 2 model file [Need to Download from https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q2_K.gguf]
- `data/` - Directory for storing any additional data
- `venv/` - Python virtual environment

## Dependencies

- streamlit - Web interface
- llama-index - Document processing and indexing
- llama-cpp-python - Python bindings for llama.cpp
- langchain - Framework for LLM applications
- cohere - Additional language model capabilities

## Notes

- The model file (llama-2-7b-chat.Q2_K.gguf) is not included in the repository due to its size. You'll need to obtain it separately.
- The application uses a quantized version of Llama 2 7B (Q2_K) for better performance.
- GPU acceleration is enabled by default if available.

## License

[Add your license information here]

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 