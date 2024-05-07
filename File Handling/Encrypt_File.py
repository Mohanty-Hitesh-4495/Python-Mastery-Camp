from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Read sensitive data from file
with open('File Handling/sensitive_data.txt', 'rb') as f:
    plaintext = f.read()

# Encrypt the data
cipher_text = cipher_suite.encrypt(plaintext)

# Write encrypted data to a file
with open('File Handling/encrypted_data.txt', 'wb') as f:
    f.write(cipher_text)
