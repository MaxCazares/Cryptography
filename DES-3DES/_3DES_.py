import os
import base64 as b64
from Crypto import Random
from Crypto.Cipher import DES, DES3
from Crypto.Random import get_random_bytes

# https://pycryptodome.readthedocs.io/en/latest/src/cipher/des3.html

# EDE: Encryption - Decryption - Encryption
# Option 1: (24) all sub-keys take different values

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

def Generation3DESKey(filename):
    key = DES3.adjust_key_parity(get_random_bytes(24))   
    encode_key = b64.b64encode(key)
    StoreData(filename, encode_key)

def Generation3DESIV(filename):
    iv = Random.new().read(DES3.block_size)
    encode_iv = b64.b64encode(iv)
    StoreData(filename, encode_iv)

def Predefined3DESCipher(plaintext_filename, key_filename, iv_filename):
    key = b64.b64decode(GetData(key_filename))
    iv = b64.b64decode(GetData(iv_filename))
    plaintext = DataToBytes(plaintext_filename)

    cipher = DES3.new(key, DES3.MODE_CFB, iv)
    ciphertext = cipher.encrypt(plaintext)

    encode_ciphertext = b64.b64encode(ciphertext)
    filename = f'{plaintext_filename[:-4]}.des'
    StoreData(filename, encode_ciphertext)

def Predefined3DESDecipher(ciphertext_filename, key_filename, iv_filename):
    key = b64.b64decode(GetData(key_filename))
    iv = b64.b64decode(GetData(iv_filename))
    ciphertext = b64.b64decode(GetData(ciphertext_filename))

    decipher = DES3.new(key, DES3.MODE_CFB, iv)
    decrypt_text = decipher.decrypt(ciphertext)
    plaintext = str(decrypt_text, 'utf-8')

    filename = f'{ciphertext_filename[:-4]}_.txt'
    StoreData(filename, plaintext)    