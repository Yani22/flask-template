from app import app
from utils.encryption import encrypt, decrypt
import click

@app.cli.command('encrypt')
@click.argument('string')
def encrypt_string(string):
    print(encrypt(string))
    return

@app.cli.command('decrypt')
@click.argument('string')
def decrypt_string(string):
    print(decrypt(string))
    return
