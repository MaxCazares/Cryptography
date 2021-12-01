from cVigenere import *
import random
import os

# Maximiliano Cazares Martínez: All the functions about CTR mode and Vigenere Cipher
# Manuel Esau Cruz Ramirez: All the functions about CBC mode
# Elias Munoz Primero: All the functions about CFB

def saveFile(name,content):
    try:
        with open(name,"w") as f:
            for row in content:
                for e in row:
                    f.write(english_alphabet[e%26])
    except Exception as e:
        print(e)

def GetData(filename):
    script_directory = os.path.dirname(__file__)
    filepath = f'{script_directory}/{filename}'
    f = open(filepath, 'r')
    data = ''
    for line in f:
        data += line
    f.close()
    return data

def generarVector(key):
    a = ''
    for i in range(len(key)):
        a = (english_alphabet[random.randint(0,25)])
        vector.append(a)
    return vector

def Encrypt_CBC(vector, key, plaintext):
    enc = []
    key = index_finder(key)
    vector = index_finder(vector)
    #print(f'key: {key}')
    #print(f'vector: {vector}')
    aux_v = vector #IV --> c1 --> c2 ...
    for i in range(0,len(plaintext),len(vector)):
        aux_m = plaintext[i:i+len(vector)] #m1, m2, m3 ...
        aux_m = index_finder(aux_m)
        #print(f'm: {aux_m}\n')
        # XOR
        aux_x = encryption(aux_m, vector, 26)
        # Encrypt
        aux_c = encryption(aux_x, key, 26)
        aux_v = aux_c #IV --> c1 --> c2 ...
        enc.append(aux_c)

    return enc

def Decrypt_CBC(vector, key, ciphertext):
    dec = []
    key = index_finder(key)
    vector = index_finder(vector)
    #print(f'key: {key}')
    #print(f'vector: {vector}')
    aux_v = vector #IV --> c1 --> c2 ...
    for i in range(0,len(plaintext),len(vector)):
        aux_c = plaintext[i:i+len(vector)] #m1, m2, m3 ...
        aux_c = index_finder(aux_c)
        # Decrypt
        aux_m = decryption(aux_c, key, 26)
        # XOR
        aux_x = encryption(aux_m, vector, 26)
        aux_v = aux_c #IV --> c1 --> c2 ...
        dec.append(aux_c)

    return dec

print('\nVigenere Cipher - CBC')
plaintext = GetData('p.txt')
key = 'dehd'
vector = 'sabh'
print(f'\n key: {key} \n Vector: {vector} \n plaintext: {plaintext}')
ciphertext = Encrypt_CBC(vector, key, plaintext)
m = Decrypt_CBC(vector, key, ciphertext)
print(f'Cipher:\n {ciphertext}\n')
print(f'Decrypt:\n {m}\n')
saveFile("EncryptionCFB.txt", ciphertext)
saveFile("DecryptionCFB.txt", m)