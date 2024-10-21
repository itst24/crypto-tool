import argparse
from cryptography.fernet import Fernet

def load_key(key_file="secret.key"):
    with open(key_file, "rb") as file:
        return file.read()

def encrypt_file(filename, key_file):
    key = load_key(key_file)
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()
    
    encrypted_data = fernet.encrypt(data)

    with open(filename + ".encrypted", "wb") as file:
        file.write(encrypted_data)

    print(f"Encrypted '{filename}' as '{filename}.encrypted'")

def decrypt_file(filename, key_file):
    key = load_key(key_file)
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open(filename.replace(".encrypted", ""), "wb") as file:
        file.write(decrypted_data)

    print(f"Decrypted '{filename}' back to '{filename.replace('.encrypted', '')}")

parser = argparse.ArgumentParser(description="Encryption/Decryption Tool")

parser.add_argument("action", choices=["encrypt", "decrypt"], help="Action to perform: Encrypt/Decrypt")
parser.add_argument("file", help="File to encrypt/deccrypt")
parser.add_argument("--key", default="secret.key", help="Default key file: secret.key")

args = parser.parse_args()

if args.action == "encrypt":
    encrypt_file(args.file, args.key)
elif args.action == "decrypt":
    decrypt_file(args.file, args.key)