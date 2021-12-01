import random
import numpy as np

'''
Cazares Martinez Maximiliano - xgcd and Identity Matrix 
Cipriano Damian Sebastian - inverseMatrix and helped with Identity Matrix
Toledo Espinosa Cristina Aline - keygeneration 

En este codigo se encuentran 5 funciones distintas:

xgcd: esta función permite usar el algoritmo de euclides extendido 
mcd: esta función calcula el maximo comund divisor de 2 enteros 
KeyGeneration: esta función crea una matriz invertible y con determinante coprimo al tamaño del alfabeto 
inverseMatrix: esta función retorna la matriz inversa de una matriz proporcionada como parametro
identityMatrix: esta función revisa si una matriz es la inversa de la otra al multiplicar ambas y obtener como resultado la matriz identidad  
'''

def xgcd(a, n):
    u, v = a, n
    x1, x2 = 1, 0
    while(u != 1):
        q = v//u
        r = v - (q * u)
        x = x2 - (q * x1)
        v, u, x2, x1 = u, r, x1, x 
    return (x1 % n)
    
# d = determinante de la matrix
# n = tamaño del alfabeto
def mcd(d,n):
    if(n==0): return d
    return mcd(n,int(n)%int(d))

# kg = la llave generada
kg=np.zeros((3,3))
def KeyGeneration(n):
    kg = np.random.randint(0,n,(3,3))
    d = kg[0][0]*(kg[1][1]*kg[2][2]-kg[1][2]*kg[2][1])-kg[0][1]*(kg[1][0]*kg[2][2]-kg[1][2]*kg[2][0])+kg[0][2]*(kg[1][0]*kg[2][1]-kg[1][1]*kg[2][0])
    if(d!=0 and mcd(d,n)==1):
        return kg
    else:
        return KeyGeneration(n)

# K = llave
# K1 = llave inversa
c=np.zeros((3,3))
def IdentityMatrix(kg, K1):
    for i in range(3):
        for j in range(3):
            for k in range(3):
                c[i][j] += kg[i][k] * K1[k][j]
    if(c[0][0]==1 and c[1][1]==1 and c[2][2]==1):
        return c
    else:
        return c

# K = llave
# K1 = llave inversa
# n = tamaño

def egcd(a, b):
    if a == 0:
        return (int(b), 0, 1)
    else:
        g, y, x = egcd(int(b) % a, a)
        return (g, x - (int(b) // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, int(m))
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % int(m)

def inverseMatrix(kg,n):
    K1=np.zeros((3,3))
    mult = -1
    d = kg[0][0]*(kg[1][1]*kg[2][2]-kg[1][2]*kg[2][1])-kg[0][1]*(kg[1][0]*kg[2][2]-kg[1][2]*kg[2][0])+kg[0][2]*(kg[1][0]*kg[2][1]-kg[1][1]*kg[2][0])
    d = d%int(n)
    d = modinv(d,n)
    co_fctr_1 = [(kg[1][1] * kg[2][2]) - (kg[1][2] * kg[2][1]),
                 -((kg[1][0] * kg[2][2]) - (kg[1][2] * kg[2][0])),
                 (kg[1][0] * kg[2][1]) - (kg[1][1] * kg[2][0])]

    co_fctr_2 = [-((kg[0][1] * kg[2][2]) - (kg[0][2] * kg[2][1])),
                 (kg[0][0] * kg[2][2]) - (kg[0][2] * kg[2][0]),
                 -((kg[0][0] * kg[2][1]) - (kg[0][1] * kg[2][0]))]

    co_fctr_3 = [(kg[0][1] * kg[1][2]) - (kg[0][2] * kg[1][1]),
                 -((kg[0][0] * kg[1][2]) - (kg[0][2] * kg[1][0])),
                 (kg[0][0] * kg[1][1]) - (kg[0][1] * kg[1][0])]

    K1 = [[(d * (co_fctr_1[0]))%int(n), (d * (co_fctr_2[0]))%int(n), (d * (co_fctr_3[0]))%int(n)],
                [(d * (co_fctr_1[1]))%int(n), (d * (co_fctr_2[1]))%int(n), (d * (co_fctr_3[1]))%int(n)],
                [(d * (co_fctr_1[2]))%int(n), (d * (co_fctr_2[2]))%int(n), (d * (co_fctr_3[2]))%int(n)]]
    return K1
    
n = input('Tamaño del alfabeto: ')
kg=KeyGeneration(n)
print(f'La Key que cifra es: {kg}')
K1=inverseMatrix(kg,n)
print(f'La Key que descifra es: {K1}')
print(f'Matriz identidad: {IdentityMatrix(kg,K1)}')