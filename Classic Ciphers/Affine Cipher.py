import random
from sympy import mod_inverse

            #0                   #5                 #10                 #15                 #20                 #25
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']

def maximoComunDivisor(a, b):
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a

def key_generator(n):
    a = random.randint(0, n-1)
    b = random.randint(0, n-1)

    while maximoComunDivisor(a,n) != 1:
        a = random.randint(0, n-1)

    return a,b

def cipher(mi, a , b, n):
    return ((a * mi + b) % n)

def decipher(ci, a, b, n):
    return (a * (ci - b)) % n

# n = int(input('Tamaño del alfabeto: '))
n = len(alphabet)
a,b = key_generator(n)
m = random.randint(0,n)

ci = cipher(m, a, b, n)

print(f'mi: {alphabet[m]} - {m}, ci: {alphabet[ci]} - {ci},' 
    +f' n: {n}, a: {a}, mcd(a,n): {maximoComunDivisor(a,n)}, b: {b}')

mi = decipher(ci, mod_inverse(a,n), b, n)

print(f'\nci: {alphabet[ci]} - {ci}, mi: {alphabet[mi]} - {mi},' 
    +f' n: {n}, a: {a}, a\': {mod_inverse(a,n)}, b: {b}')