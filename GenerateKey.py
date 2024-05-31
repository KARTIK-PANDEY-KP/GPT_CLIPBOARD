from Crypto.PublicKey import RSA
import os 

def save_rsa_keys(filepath, key):
    with open(filepath, "wb") as key_file:
        key_file.write(key)

# Generate RSA keys
key = RSA.generate(4096)
try:
    os.mkdir("keys/")
except:
    pass
private_key = key.export_key()
public_key = key.publickey().export_key()

# Save keys to files
save_rsa_keys("keys/private.pem", private_key)
save_rsa_keys("keys/public.pem", public_key)
