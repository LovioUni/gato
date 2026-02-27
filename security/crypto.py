from cryptography.fernet import Fernet

key = b'mmXqnZBDVQeISgB83eUuUsjfljSRw8PkSAv80lMBdXA='

fernet = Fernet(key)

def encrypt(value):
    return fernet.encrypt(value.encode()).decode()

def decrypt(value):
    return fernet.decrypt(value.encode()).decode()