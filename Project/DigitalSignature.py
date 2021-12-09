import os
import base64
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

# https://pycryptodome.readthedocs.io/en/latest/src/examples.html#generate-public-key-and-private-key

# Parte de HASH
def Hash256(data):
    h = SHA256.new()
    h.update(data)
    return base64.b64encode(h.digest())

# Parte de RSA
def GetBytesFromFile(filename):
    script_directory = os.path.dirname(__file__)
    filepath = f'{script_directory}/{filename}'
    f = open(filepath, 'rb')
    FileBytes = f.read()
    return base64.b64encode(FileBytes)

def privateKeyGenerator(privateKeyFile, key):
    script_directory = os.path.dirname(__file__)
    privateKey = f'{script_directory}/{privateKeyFile}'
    private_key = key.export_key()
    file_out = open(privateKey, "wb")
    file_out.write(private_key)
    file_out.close()

def publicKeyGenerator(publicKeyFile, key):
    script_directory = os.path.dirname(__file__)
    publicKey = f'{script_directory}/{publicKeyFile}'

    public_key = key.publickey().export_key()
    file_out = open(publicKey, "wb")
    file_out.write(public_key)
    file_out.close()

def KeyGenerator(private, public):
    key = RSA.generate(2048)
    privateKeyGenerator(private, key)
    publicKeyGenerator(public, key)

def RSAEncrypt(data, encryptedFile, publicKey):
    script_directory = os.path.dirname(__file__)
    datafile = f'{script_directory}/{encryptedFile}'

    file_out = open(datafile, "wb")

    recipient_key = RSA.import_key(open(f'{script_directory}/{publicKey}').read())
    session_key = get_random_bytes(16)

    # Encrypt the session key with the public RSA key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    # Encrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)
    [ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
    file_out.close()

def RSADecrypt(encryptedData, privateKey):
    script_directory = os.path.dirname(__file__)
    encrypted_data = f'{script_directory}/{encryptedData}'

    file_in = open(encrypted_data, "rb")
    private_key = RSA.import_key(open(f'{script_directory}/{privateKey}').read())

    enc_session_key, nonce, tag, ciphertext = \
    [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]

    # Decrypt the session key with the private RSA key
    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)

    # Decrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    return data