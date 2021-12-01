english_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
key = "hund"

def index_finder(word):
    wordp = []
    for i in range(len(word)):
        wordp.append(english_alphabet.index(word[i]))
    return wordp

def GenerationKey(plaintext, key):
    if len(plaintext) == len(key): 
        return(key) 
    else: 
        for i in range(len(plaintext) - len(key)): 
            key.append(key[i % len(key)]) 
    return key

def encryption(plaintext, complete_key, n):
    ciphertext = []
    for i in range(len(plaintext)):
        ciphertext.append((plaintext[i] + complete_key[i]) % n)
    return ciphertext

def decryption(ciphertext, complete_key, n):
    plaintext = []
    for i in range(len(ciphertext)):
        plaintext.append((ciphertext[i] - complete_key[i]) % n)
    return plaintext