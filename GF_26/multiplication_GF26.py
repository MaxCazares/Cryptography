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

    # a = resP[0]
    # fgx = BitArray('0b000000')
    # for i in range(1, len(resP)):
    #     fgx = fgx ^ (a ^ resP[i])
    
    # return fgx

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

# x^2+1    000101
# x^2      000100
# x^4+x^2  010100

# x^3+1    001001
# x^2      000100
# x^5+x^2  100100

# x+1      000011
# x^2      000100
# x^3+x^2  001100

# x+1       000011
# x+1       000011
# x^2+2x+1  000101

# f = input('\nenter the binary coefficients of f(x): ')
# g = input('\nenter the binary coefficients of g(x): ')

# fx, gx = BitArray('0b000011'), BitArray('0b000011')
# print(f'\nthe product of f(x) * g(x) = {MultGF26(fx,gx).bin}')