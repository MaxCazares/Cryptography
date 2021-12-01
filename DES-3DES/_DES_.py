from _3DES_ import *

# EEE: Encryption - Encryption - Encryption
# key: 3 different 8 bit key

def writeFile(filename, data):
    script_directory = os.path.dirname(__file__)
    file_path = f"{script_directory}/{filename}"
    f = open(file_path, 'a')
    f.write(f'{str(data)}\n')
    f.close()

def readFile(filename):
    script_directory = os.path.dirname(__file__)
    file_path = f"{script_directory}/{filename}"
    f = open(file_path, 'r')
    a, b, c = f.readline(), f.readline(), f.readline()
    f.close()
    return eval(a), eval(b), eval(c)

def GenerationDESKey(filename):
    k1 = b64.b64encode(get_random_bytes(8))
    k2 = b64.b64encode(get_random_bytes(8))
    k3 = b64.b64encode(get_random_bytes(8))
    writeFile(filename, k1)
    writeFile(filename, k2)
    writeFile(filename, k3)

def GenerationDESIV(filename):
    iv1 = b64.b64encode(Random.new().read(DES.block_size))
    iv2 = b64.b64encode(Random.new().read(DES.block_size))
    iv3 = b64.b64encode(Random.new().read(DES.block_size))
    writeFile(filename, iv1)
    writeFile(filename, iv2)
    writeFile(filename, iv3)

def cipher(k, iv, m):
    cipher = DES.new(k, DES.MODE_CFB, iv)
    ciphertext = cipher.encrypt(m)
    return ciphertext

def decipher(k, iv, c):
    decipher = DES.new(k, DES.MODE_CFB, iv)
    plaintext = decipher.decrypt(c)
    return plaintext

def DESEEECipher(plaintext_filename, key_filename, iv_filename):
    k1, k2, k3 = readFile(key_filename)    
    k1, k2, k3 = b64.b64decode(k1), b64.b64decode(k2), b64.b64decode(k3)
    iv1, iv2, iv3 = readFile(iv_filename)
    iv1, iv2, iv3 = b64.b64decode(iv1), b64.b64decode(iv2), b64.b64decode(iv3)
    plaintext = DataToBytes(plaintext_filename)

    c1 = cipher(k1, iv1, plaintext)
    c2 = cipher(k2, iv2, c1) 
    c3 = cipher(k3, iv3, c2)
    c3 = b64.b64encode(c3)
    
    filename = f'{plaintext_filename[:-4]}.des'
    StoreData(filename, c3)

def DESEEEDecipher(ciphertext_filename, key_filename, iv_filename):
    k1, k2, k3 = readFile(key_filename) 
    k1, k2, k3 = b64.b64decode(k1), b64.b64decode(k2), b64.b64decode(k3)
    iv1, iv2, iv3 = readFile(iv_filename)
    iv1, iv2, iv3 = b64.b64decode(iv1), b64.b64decode(iv2), b64.b64decode(iv3)
    ciphertext = b64.b64decode(GetData(ciphertext_filename))

    d3 = decipher(k3, iv3, ciphertext)
    d2 = decipher(k2, iv2, d3)
    d1 = decipher(k1, iv1, d2)
    plaintext = str(d1, 'utf-8')

    filename = f'{ciphertext_filename[:-4]}_.txt'
    StoreData(filename, plaintext)  