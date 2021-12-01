from CTR_mode import *

# Encryption
def StartEncryption(keyfile, file_to_encrypt, file_counters, EncryptedFile):
    key = GetData(keyfile)
    a = GetData(file_to_encrypt)
    b = CompleteMessage(SplitMessage(a.lower().replace(' ', ''), key), len(key))

    c = len(b)
    d = CreateCounter(c, key)

    e = IndexFinder(b)
    f = IndexFinder(d)
    StoreData(file_counters, f)

    g = encryption(f, IndexFinder(key), len(english_alphabet))
    h = MessageXORCounter(e, g)

    i = NumbersToLetters(english_alphabet, h)
    j = ArrayToString(i)
    StoreData(EncryptedFile, j)

    print(f'\nkey: {IndexFinder(key)} \nplaintext: {a} \nsplit text: {b} ')
    print(f'\n# counters: {c} \ncounters: {d}')
    print(f'\ntexto en numeros: {e} \nCounters en numeros: {f}')
    print(f'\nCounters cifrados: {g}  \nfinal: {h}')
    print(f'\nFinal en letras: {i} \nfinal en cadena: {j}')

# Decryption

def StartDecryption(keyfile, EncryptFile, file_counters, DecryptedFile):
    key = GetData(keyfile)
    a = GetData(EncryptFile)
    b = SplitMessage(a, key)
    c = IndexFinder(b)

    d = GetData(file_counters)
    e = encryption(eval(d), IndexFinder(key), len(english_alphabet))

    f = MessageXORCounter(c, e)
    g = NumbersToLetters(english_alphabet, f)
    h = ArrayToString(g)
    StoreData(DecryptedFile,h)

    print('\n\tElementos para decifrar')
    print(f'\nkey: {key}')
    print(f'\ntexto cifrado: {a} \ntexto separado: {b} \ntexto separado en numeros: {c}')
    print(f'\ncounters cifrados: {d} \ncounters decifrados: {e}')
    print(f'\ntexto en numeros: {f} \ntexto en letras: {g} \ntexto en cadena: {h}')

keyfile = 'key.txt'
file_to_encrypt = 'text.txt'
file_counters = 'counters.txt'
EncryptedFile = 'textEncrypted.txt'
DecryptedFile = 'text_.txt'

GenerateKey(keyfile, 4)
StartEncryption(keyfile, file_to_encrypt, file_counters, EncryptedFile)
StartDecryption(keyfile, EncryptedFile, file_counters, DecryptedFile)