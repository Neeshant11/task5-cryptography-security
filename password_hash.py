import bcrypt

password = b"MySecurePassword123"

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print("Hash:", hashed)

if bcrypt.checkpw(password, hashed):
    print("Password Verified")