from cryptography.fernet import Fernet

# Generates a key and saves it to a file.
def generate_key(file_name="secret.key"):
    key = Fernet.generate_key()
    with open(file_name, "wb") as key_file:
        key_file.write(key)
    print(f"Key saved to {file_name}")

if __name__ == "__main__":
    generate_key()