from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
import base64
import json
import requests

# Load private key from file
def load_private_key(filepath):
    with open(filepath, "rb") as key_file:
        private_key = RSA.import_key(key_file.read())
    return private_key

# Decrypt data using AES and RSA
def decrypt_data(encrypted_data, private_key):
    encrypted_aes_key = base64.b64decode(encrypted_data['encrypted_aes_key'])
    nonce = base64.b64decode(encrypted_data['nonce'])
    tag = base64.b64decode(encrypted_data['tag'])
    ciphertext = base64.b64decode(encrypted_data['ciphertext'])
    
    cipher_rsa = PKCS1_OAEP.new(private_key)
    aes_key = cipher_rsa.decrypt(encrypted_aes_key)
    cipher_aes = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    return data.decode()

# Load the encrypted data from file
url = 'http://localhost:3000/data'

# Send a GET request to fetch the data
response = requests.get(url)

# Assuming the server responds with JSON data
if response.status_code == 200:
    encrypted_data = response.json()
    print('Received encrypted data:', encrypted_data)
else:
    print('Failed to fetch data, status code:', response.status_code)

# Load private key
private_key = load_private_key("keys/private.pem")

# Decrypt and print the decrypted content
decrypted_content = decrypt_data(encrypted_data, private_key)
print("Decrypted Clipboard Content:", decrypted_content)
