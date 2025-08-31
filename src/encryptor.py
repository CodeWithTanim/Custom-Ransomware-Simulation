import pyAesCrypt
import os
from utils import BUFFER_SIZE, list_files

def encrypt_file(file_path, password):
    encrypted_file = file_path + ".aes"
    pyAesCrypt.encryptFile(file_path, encrypted_file, password, BUFFER_SIZE)
    os.remove(file_path)
    print(f"Encrypted: {file_path}")

def encrypt_folder(folder, password):
    files = list_files(folder)
    for file in files:
        encrypt_file(file, password)
