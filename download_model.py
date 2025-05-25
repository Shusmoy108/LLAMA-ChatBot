import os
import wget

def bar_custom(current, total, width=80):
    print("Downloading %d%% [%d / %d] bytes" % (current / total * 100, current, total))

# Set the model URL and filename
model_url = "https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q2_K.gguf"
filename = "llama-2-7b-chat.Q2_K.gguf"

# Check if the file already exists
if os.path.exists(filename):
    print(f"File '{filename}' already exists. Skipping download.")
else:
    print(f"File '{filename}' not found. Downloading...")
    wget.download(model_url, out=filename, bar=bar_custom)
    print("\nDownload complete.")
