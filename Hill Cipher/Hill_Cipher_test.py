from Hill_Cipher import *


size_alphabet = int(input('\n\nTamaño del alfabeto: '))
key = KeyGeneration(size_alphabet)
file_name = input('Nombre del archivo: ')

StoreKey(file_name, key)
key_file = GetKey(file_name)
print(f'\nKey que cifra: {key_file}')

inverse_key = InverseMatrix(key_file, size_alphabet)
print(f'\nKey que decifra (matrix inversa): {inverse_key}')

print(f'\nMatriz identidad: {IdentityMatrix(key_file, inverse_key, size_alphabet)}\n')