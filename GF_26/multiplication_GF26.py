from bitstring import BitArray, BitStream
# https://bitstring.readthedocs.io/en/latest/index.html

irreducible_polynomial = BitArray('0b000011')

def product(bits):    
    if not bits[0]:
        return bits << 1
    else:
        return (bits << 1) ^ irreducible_polynomial

def MultGF26(f, g):
    fx = BitArray(f'0b{f}')
    gx = BitArray(f'0b{g}')

    resP = []
    for i in range(0, 5):
        aux = fx
        if gx[i]:
            j = i
            for j in range(i,5):
                aux = product(aux)    
            resP.append(aux)

    if gx[5]:
        resP.append(fx)

    a = resP[0]
    fgx = []
    for i in range(1, len(resP)):
        fgx.append(a ^ resP[i])
    
    if len(fgx) > 0:
        return fgx[0]
    else:
        return a

def CompleteZeros(f):
    a = ''
    if len(f) < 7:
        for i in range(6 - len(f)):
            a += '0'
    return f'{a}{f}'

def RightLen(f,g):
    f , g = f[2:], g[2:]
    f, g = CompleteZeros(f), CompleteZeros(g)
    return f, g

def multiplicativeInverse(limite, a):
    row = limite-1
    col = limite-1
    for i in range(0, row):
        aux = a[i][0]
        for j in range(1, col):
            aux2 = a[i][j]
            if aux2 == '000001':
                print(aux,a[0][j])
                break