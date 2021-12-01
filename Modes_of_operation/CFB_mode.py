import random
from cVigenere import *
i_vector = "cake"

# Maximiliano Cazares Martínez: All the functions about CTR mode and Vigenere Cipher
# Manuel Esau Cruz Ramirez: All the functions about CBC mode
# Elias Munoz Primero: All the functions about CF

def generate_word():
    word=""
    for i in range(0,4):
        word+=english_alphabet[random.randint(0,25)]
    return word

def read_file():
    plainText = list()
    with open("text.txt") as f:    
        linesDocument = f.readlines()
    for i in range(len(linesDocument)):
        for j in range(len(linesDocument[i])):
            if(linesDocument[i][j].lower() in english_alphabet):            
                plainText.append(linesDocument[i][j].lower())
    words = list()
    part = ""
    counter=0    
    for i in plainText:
        part+=i
        counter+=1
        if(counter==4):
            words.append(part)
            counter=0
            part=""
    partitions = list()
    for i in words:
        partitions.append(index_finder(i))    
    return partitions

def Encrypted_CFB(iv,txt,key):
    c0 = list()
    p0 = txt[0]
    enc = encryption(iv,key,26)
    for i in range(4):
        c0.append(enc[i]^p0[i])
    cm = list()
    cm.append(c0)
    ci=list()
    for i in range(1,len(txt)):
        pi=txt[i]
        enc=encryption(cm[i-1],key,26)
        for j in range(4):
            ci.append(pi[j]^enc[j])
        cm.append(ci)
        ci=[]
    return cm

def Decrypted_CFB(iv,cm,key):
    p0 = list()
    c0 = cm[0]
    enc = encryption(iv,key,26)
    for i in range(4):
        p0.append(enc[i]^c0[i])    
    pm = list()
    pm.append(p0)
    pi = list()
    for i in range(1,len(cm)):
        ci=cm[i]
        enc=encryption(cm[i-1],key,26)
        for j in range(4):
            pi.append(ci[j]^enc[j])
        pm.append(pi)
        pi=[]
    return pm

def saveFile(name,content):
    try:
        with open(name,"w") as f:
            for row in content:
                for e in row:
                    f.write(english_alphabet[e%26])
    except Exception as e:
        print(e)

def implement_CFB():
    global i_vector
    txt = read_file()
    i_vector = index_finder(i_vector)
    n_key = index_finder(key)
    cm = Encrypted_CFB(i_vector,txt,n_key)
    pm = Decrypted_CFB(i_vector,cm,n_key)
    saveFile("EncryptionCFB.txt",cm)
    saveFile("DecryptionCFB.txt",pm)

implement_CFB()