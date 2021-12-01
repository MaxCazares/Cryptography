import os
import base64 as b64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html?highlight=aes#Crypto.Cipher.AES.new

def StoreData(filename, data):
    script_directory = os.path.dirname(__file__)
    filepath = f'{script_directory}/{filename}'
    f = open(filepath, 'w')
    f.write(str(data))
    f.close

def GetData(filename):
    script_directory = os.path.dirname(__file__)
    filepath = f'{script_directory}/{filename}'
    f = open(filepath, 'r')
    data = f.readline() 
    f.close()
    return eval(data)

def DataToBytes(filename):
    script_directory = os.path.dirname(__file__)
    filepath = f'{script_directory}/{filename}'
    f = open(filepath)
    data = ""
    for line in f:
        data += line
    return bytes(data, 'utf-8')

def GenerationAESKey(key_size, filename):
    key = get_random_bytes(key_size)
    encode_key = b64.b64encode(key)
    StoreData(filename, encode_key)

def GenerationAESiv(filename):
    iv = get_random_bytes(AES.block_size)
    encode_iv = b64.b64encode(iv)
    StoreData(filename, encode_iv)

def AESCipher(plaintext_filename, key_filename, iv_filename, mode_operation):
    key = b64.b64decode(GetData(key_filename))
    # iv = b64.b64decode(GetData(iv_filename))
    plaintext = DataToBytes(plaintext_filename)

    cipher = AES.new(key, mode_operation, iv_filename)
    ciphertext = cipher.encrypt(plaintext)

    encode_ciphertext = b64.b64encode(ciphertext)
    filename = f'{plaintext_filename[:-4]}.aes'
    StoreData(filename, encode_ciphertext)

def AESDecipher(ciphertext_filename, key_filename, iv_filename, mode_operation):
    key = b64.b64decode(GetData(key_filename))
    # iv = b64.b64decode(GetData(iv_filename))
    ciphertext = b64.b64decode(GetData(ciphertext_filename))

    decipher = AES.new(key, mode_operation, iv_filename)
    decrypt_text = decipher.decrypt(ciphertext)
    plaintext = str(decrypt_text, 'utf-8')

    filename = f'{ciphertext_filename[:-4]}_.txt'
    StoreData(filename, plaintext)    