import keyboard
import pyperclip as pc
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes
import base64
import json
import requests
import json

# Load public key from file
def load_public_key(filepath):
    with open(filepath, "rb") as key_file:
        public_key = RSA.import_key(key_file.read())
    return public_key

# Encrypt data using AES and RSA
def encrypt_data(data, public_key):
    aes_key = get_random_bytes(16)
    cipher_aes = AES.new(aes_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data.encode())
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)
    return {
        'encrypted_aes_key': base64.b64encode(encrypted_aes_key).decode(),
        'nonce': base64.b64encode(cipher_aes.nonce).decode(),
        'tag': base64.b64encode(tag).decode(),
        'ciphertext': base64.b64encode(ciphertext).decode()
    }

# Main function to capture keyboard inputs and encrypt clipboard content
def capture_keyboard(public_key):
    while True:
        try:
            keyboard.wait('ctrl+shift+space')
            clipboard_content = pc.paste()
            encrypted_content = encrypt_data(clipboard_content, public_key)
            url = 'http://localhost:3000/store'
            # Send a POST request with JSON data
            response = requests.post(url, json=encrypted_content)

            print("Encrypted data saved to file.")
        except KeyboardInterrupt:
            print("Ctrl+C pressed. Exiting...")
            break

# Load public key
public_key = load_public_key("keys/public.pem")
capture_keyboard(public_key)
