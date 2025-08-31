from utils import generate_key, load_key
from encryptor import encrypt_folder
from decryptor import decrypt_folder
import os

SANDBOX_FOLDER = "sandbox"

def main():
    print("==== Custom Ransomware Simulation ====")
    print("1. Encrypt sandbox files")
    print("2. Decrypt sandbox files")
    choice = input("Enter choice (1/2): ")

    if choice == "1":
        key = generate_key()
        encrypt_folder(SANDBOX_FOLDER, key)
    elif choice == "2":
        key = load_key()
        decrypt_folder(SANDBOX_FOLDER, key)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
