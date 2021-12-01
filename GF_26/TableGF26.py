from multiplication_GF26 import *

limite = 64
a = []
for i in range(1, limite):
    b = []
    for j in range(1, limite):
        fx, gx = RightLen(bin(i), bin(j))
        b.append(MultGF26(fx, gx).bin)
    a.append(b)

for i in range(0, len(a)):
    print(f'\n{a[i]}\n')

multiplicativeInverse(limite, a)