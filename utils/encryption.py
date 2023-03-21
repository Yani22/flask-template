from cryptography.fernet import Fernet
from app import ENV_VARIABLES

ENCRYPTION_KEY = bytes(ENV_VARIABLES['ENCRYPTION_KEY'], 'utf-8')
fernet = Fernet(ENCRYPTION_KEY)

def encrypt(string):
    return fernet.encrypt(bytes(string, 'utf-8')).decode()

def decrypt(string):
    return fernet.decrypt(bytes(string, 'utf-8')).decode()