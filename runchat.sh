#!/bin/bash

# Exit on errors
set -e

echo "👉 Activate your environment with: source venv/bin/activate"
source venv/bin/activate
echo "Activating virtual environment"
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

echo "Downloading LLAMA Model..."

$PYTHON download_model.py


echo "Running Streamlit Chatbot app on http://localhost:8500"
streamlit run app.py --server.port 8500 &  # Run in background
APP_PID=$!  # Capture the PID of the background process

# Function to stop the app
stop_app() {
  echo -e "\nStopping Streamlit app (PID: $APP_PID)..."
  kill $APP_PID
  wait $APP_PID 2>/dev/null
  echo "Streamlit app stopped."
  deactivate
  echo "Deactivating virtual environment"
  echo "✅ Done!"
  exit 0
}

# Watch for 'q' key to quit
echo "Press 'q' then [ENTER] to quit."

while true; do
  read -r -n1 input
  if [[ "$input" == "q" ]]; then
    stop_app
  fi
done


