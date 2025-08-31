import pyAesCrypt
import os
from utils import BUFFER_SIZE, list_files

def decrypt_file(file_path, password):
    if not file_path.endswith(".aes"):
        return
    decrypted_file = file_path[:-4]
    try:
        pyAesCrypt.decryptFile(file_path, decrypted_file, password, BUFFER_SIZE)
        os.remove(file_path)
        print(f"Decrypted: {decrypted_file}")
    except ValueError:
        print(f"Wrong key for file: {file_path}")

def decrypt_folder(folder, password):
    files = list_files(folder)
    for file in files:
        decrypt_file(file, password)
