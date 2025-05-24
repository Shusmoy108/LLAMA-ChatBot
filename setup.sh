#!/bin/bash

# Exit if any command fails
set -e

echo "Creating virtual environment in ./venv"
python3 -m venv venv

echo "Activating virtual environment"
source venv/bin/activate

echo "Installing dependencies from requirements.txt"
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Virtual environment is ready. Use 'source venv/bin/activate' to activate it."
