import Encrypt_File as ef

# Read encrypted data from file
with open('File Handling/encrypted_data.txt', 'rb') as f:
    cipher_text = f.read()

# Decrypt the data
plain_text = ef.cipher_suite.decrypt(cipher_text)

# Display or process the decrypted data
print(plain_text.decode('utf-8'))
