#!/bin/bash

# Exit if any command fails
set -e

echo "Running Streamlit Chatbot app"
streamlit run app.py --server.port 8500
