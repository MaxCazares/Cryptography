from HashOwn import *
from HashLibrary import *

def Exercise1():
    m = int(input('Ingresa un número mayor o igual a 3: '))
    filename = input('Ingresa nombre del archivo: ')
    n = 2 ** m

    mXOR = HashFunction(filename, n)
    print(f'Esta es la xor de los bloques: {mXOR}')

def Exercise3(FileInfo):
    file, type = FileInfo[0], FileInfo[1] 
    digest = Hash256(file, type)
    print(f'\nArchivo: {file} \nDigesto: {digest}')

# Exercise1()

files = [['test.txt', 'text'], ['uno.jpg', 'media'], ['marcianito.mp4', 'media']]
for file in files:
    Exercise3(file)