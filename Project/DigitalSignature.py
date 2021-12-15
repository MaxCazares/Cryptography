import os
import base64
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
import binascii

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

def GetData(filename):
    script_directory = os.path.dirname(__file__)
    filepath = f'{script_directory}/{filename}'
    f = open(filepath, 'r')
    data = f.readline() 
    f.close()
    return data

def RSAEncrypt(data, encryptedFile, publicKey):
    script_directory = os.path.dirname(__file__)
    datafile = f'{script_directory}/{encryptedFile}'

    encryptor = PKCS1_OAEP.new(RSA.import_key(open(f'{script_directory}/{publicKey}').read()))
    encryptedData =   binascii.hexlify(encryptor.encrypt(data))

    # print(f'tipo de encrypedData: {type(encryptedData)}\n')
    # print(f'esto es encryptedData: {encryptedData}')

    file_out = open(datafile, "wb")
    file_out.write(encryptedData)
    file_out.close()

def RSADecrypt(encryptedData, privateKey):    
    script_directory = os.path.dirname(__file__)    
    encryptedData =  binascii.unhexlify(GetData(encryptedData))

    decryptor = PKCS1_OAEP.new(RSA.import_key(open(f'{script_directory}/{privateKey}').read()))
    decrypted = decryptor.decrypt(encryptedData)
    # print(f'Este es el tipo de datos: {type(encryptedData)}')
    # print(f'estos son los datos: {encryptedData}') 
    # print(f'esto sale del decifrador: {decrypted}')
    return decrypted