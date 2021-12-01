import os
import base64
from Crypto.Hash import SHA256

# https://pycryptodome.readthedocs.io/en/latest/src/hash/sha256.html?highlight=hash

def GetMedia(filename):
    script_directory = os.path.dirname(__file__)
    filepath = f'{script_directory}/{filename}'
    f = open(filepath, 'rb')
    ImageBytes = f.read()
    return base64.b64encode(ImageBytes)

def GetText(filename):
    script_directory = os.path.dirname(__file__)
    filepath = f'{script_directory}/{filename}'
    f = open(filepath)
    data = ""
    for line in f:
        data += line
    return bytes(data, 'utf-8')

def Hash256(filename, type):
    if type == 'text':
        data = GetText(filename)
    elif type == 'media':
        data = GetMedia(filename)
    
    h = SHA256.new()
    h.update(data)
    return h.hexdigest()