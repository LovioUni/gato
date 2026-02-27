from cryptography.fernet import Fernet
import os

def generate_key():
    if not os.path.exists("gatokey.txt"):
        key = Fernet.generate_key()
        with open("gatokey.txt", "wb") as file:
            file.write(key)
        print("Key generada en gatokey.txt")

def encrypt(value) -> str:
    with open("gatokey.txt", "rb") as file:
        key = file.read()
    fernet = Fernet(key)
    return fernet.encrypt(value.encode()).decode()

def decrypt(value) -> str:
    with open("gatokey.txt", "rb") as file:
        key = file.read()
    fernet = Fernet(key)
    return fernet.decrypt(value.encode()).decode()