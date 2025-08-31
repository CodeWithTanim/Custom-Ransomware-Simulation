import os
import pyAesCrypt
import logging

BUFFER_SIZE = 64 * 1024  # 64KB buffer for encryption

# Setup logging
logging.basicConfig(filename="simulation.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def generate_key():
    """Generate a random AES key and save to key.key"""
    import secrets
    key = secrets.token_hex(16)  # 128-bit key
    with open("key.key", "w") as f:
        f.write(key)
    logging.info("Key generated and saved to key.key")
    return key

def load_key():
    """Load AES key from key.key"""
    if not os.path.exists("key.key"):
        raise FileNotFoundError("Key file not found!")
    with open("key.key", "r") as f:
        key = f.read()
    return key

def list_files(folder):
    """Recursively list all files in a folder"""
    files = []
    for root, _, filenames in os.walk(folder):
        for file in filenames:
            files.append(os.path.join(root, file))
    return files
