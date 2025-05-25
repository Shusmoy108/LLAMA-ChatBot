#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Function to find available Python interpreter
find_python() {
    if command -v python3 &>/dev/null; then
        echo "python3"
    elif command -v python &>/dev/null; then
        echo "python"
    else
        echo "❌ Python is not installed. Please install Python 3."
        exit 1
    fi
}

PYTHON=$(find_python)

echo "Using Python interpreter: $PYTHON"

echo "Creating virtual environment in ./venv"
$PYTHON -m venv venv

echo "Activating virtual environment"
source venv/bin/activate

echo "Installing dependencies from requirements.txt"
pip install --upgrade pip
pip install -r requirements.txt

#echo "Downloading LLaMA 2 7B Chat model (Q2_K GGUF)..."
#cd venv/bin/wget -c https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q2_K.gguf

echo "✅ Setup complete!"
echo "👉 Activate your environment with: source venv/bin/activate"
echo "Download LLaMA 2 7B Chat model (Q2_K GGUF) from https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q2_K.gguf"
#source venv/bin/activate


