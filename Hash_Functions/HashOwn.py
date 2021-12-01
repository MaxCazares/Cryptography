import os

def GetData(filename):
    script_directory = os.path.dirname(__file__)
    filepath = f'{script_directory}/{filename}'
    f = open(filepath, 'r')
    data = ''
    for line in f:
        data += line
    f.close()
    return data

def xor(m):
    a = 0
    for i in range(len(m)):
        a ^= int(m[i], 2)
    return hex(a)

def SplitMessage(message, n):
    div = []
    for i in range(0, len(message), n):
        div.append(message[i: i+n])
    return div

def CompleteLetter(letter):
    if len(letter) < 8:
        a = ''
        for i in range(8 - len(letter)):
            a += '0'
        letter = a + letter
        return letter
    else:
        return letter

def TextToBinary(message):
    binary_message = ''
    for i in message:
        binary_message += CompleteLetter(format(ord(i), 'b'))
    return binary_message

def HashFunction(filename, n):
    message = GetData(filename)
    binary_message = TextToBinary(message)
    smessage = SplitMessage(binary_message, n)
    mXOR = xor(smessage)
    return mXOR