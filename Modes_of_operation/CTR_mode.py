import os
import random

# Maximiliano Cazares Martínez: All the functions about CTR mode and Vigenere Cipher
# Manuel Esau Cruz Ramirez: All the functions about CBC mode
# Elias Munoz Primero: All the functions about CF

                    #0                  #5                 #10                 #15           
english_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
                #16             #20                 #25                 #30
                'q','r','s','t','u','v','w','x','y','z',' ','+','-','*','/','_']


def GetData(filename):
    script_directory = os.path.dirname(__file__)
    filepath = f'{script_directory}/{filename}'
    f = open(filepath, 'r')
    data = ''
    for line in f:
        data += line
    f.close()
    return data

def StoreData(filename, data):
    script_directory = os.path.dirname(__file__)
    filepath = f'{script_directory}/{filename}'
    f = open(filepath, 'w')
    f.write(str(data))
    f.close

def IndexFinder(words):
    a = []
    for i in range(len(words)):
        b = []
        for j in range(len(words[i])):
            b.append(english_alphabet.index(words[i][j]))
        a.append(b)
    return a

def NumbersToLetters(alphabet, m):
    a = []
    for i in range(len(m)):
        b = ''
        for j in range(len(m[i])):
            b += alphabet[m[i][j]]
        a.append(b)
    return a

def ArrayToString(message):
    a = ''
    for i in range(len(message)):
        a += message[i]
    return a

def CreateCounter(amount, key): 
    counters = []
    for i in range(amount):
        counter = ''
        for j in range(len(key)):
            counter += english_alphabet[random.randint(0,25)]
        counters.append(counter)
    return counters

def CompleteMessage(message, size):
    a = message[-1]
    for i in range(size - len(a)):
        a += ' '
    message.pop()
    message.append(a)
    return message

def GenerateKey(keyfile, lenKey):
    a = ''
    for i in range(lenKey):
        a += english_alphabet[random.randint(0,25)]
    StoreData(keyfile, a)

def MessageXORCounter(message, counter):
    c = []
    for i in range(len(message)):
        d = []
        for j in range(len(message[i])):
            d.append(eval(bin(message[i][j])) ^ eval(bin(counter[i][j])))
        c.append(d)
    return c

# Vignere Cipher

def SplitMessage(plaintext, key):
    div = []
    for i in range(0, len(plaintext), len(key)):
        div.append(plaintext[i:i+len(key)])
    return div

def encryption(plaintext, key, n):
    ciphertext = []
    for i in range(len(plaintext)):
        c = []
        for j in range(len(plaintext[i])):
            c.append((plaintext[i][j] + key[j][0]) % n)
        ciphertext.append(c)
    return ciphertext

def decryption(ciphertext, key, n):
    plaintext = []
    for i in range(len(ciphertext)):
        p = []
        for j in range(len(ciphertext[i])):
            p.append((ciphertext[i][j] - key[j][0]) % n)
        plaintext.append(p)
    return plaintext