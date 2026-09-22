from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

key = AESGCM.generate_key(bit_length=256)
aesgcm = AESGCM(key)

nonce = os.urandom(12)
data = b"Confidential Data"

ciphertext = aesgcm.encrypt(nonce, data, None)
print("Encrypted:", ciphertext)

plaintext = aesgcm.decrypt(nonce, ciphertext, None)
print("Decrypted:", plaintext.decode())