from DigitalSignature import *

# Parte del profesor
def Professor():
    KeyGenerator('llavePrivada.pem', 'llavePublica.pem')
    grades = GetBytesFromFile('MixColumn.xlsx')
    HASHgrades = Hash256(grades)
    RSAEncrypt(HASHgrades, 'grades.bin', 'llavePublica.pem')

# Parte del Jefe de Servicios Escolares
def Chief():
    DecryptedGrades = RSADecrypt('grades.bin', 'llavePrivada.pem')
    grades = GetBytesFromFile('MixColumn.xlsx')
    HashGrades2 = Hash256(grades)

    if HashGrades2 == DecryptedGrades:
        print('Las calificaciones NO sufrieron modificaciones')
    else:
        print('Las calificaciones SI sufrieron modificaciones')

# Professor()
# Chief()

# a = Hash256(GetBytesFromFile('Mixcolumn.xlsx'))
# print(a)
# print(type(a))