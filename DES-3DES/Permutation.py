def PermuteAByte(b, p):
    a = ''
    for i in range(8):
        a += chr(b[(p[i]-1)])
    return bytes(a, 'utf-8')

b = b'10111101'

permutation = [2,6,3,1,4,8,5,7]       #01 11 11 10   
a = PermuteAByte(b,permutation)       
print(f'{b} => {permutation} = {a}')

permutation2 = [8,7,6,5,1,2,3,4]      #10 11 10 11
a2 = PermuteAByte(b,permutation2)
print(f'{b} => {permutation2} = {a2}')