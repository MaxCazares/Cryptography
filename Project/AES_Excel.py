import os
import xlrd
import base64 as b64
from Crypto import Random
import mysql.connector as sql
from Crypto.Cipher import AES
from Crypto.Util import Counter

def DBconnection():
    mydb = sql.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "gradescrypto"
    )
    return mydb

def StoreData(filename, data):
    script_directory = os.path.dirname(__file__)
    filepath = f'{script_directory}/{filename}'
    f = open(filepath, 'w')
    f.write(str(data))
    f.close

def GetData(filename):
    script_directory = os.path.dirname(__file__)
    filepath = f'{script_directory}/{filename}'
    f = open(filepath, 'r')
    data = f.readline() 
    f.close()
    return eval(data)

def KeyCounterGenerator(keyFile, counterFile):
    # Set up the counter with a nonce.
    # 64 bit nonce + 64 bit counter = 128 bit output
    nonce = Random.get_random_bytes(8)
    countf = Counter.new(64, nonce)
    key = Random.get_random_bytes(32) # 256 bits key

    print(f'contador: {countf} \ntipo: {type(countf)}')

    StoreData(f'{keyFile}.txt',b64.b64encode(key))
    StoreData(f'{counterFile}.txt',b64.b64encode(f'{countf}'.encode('utf-8')))

def menu():
    os.system('cls') 
    print("[1] Generar llave y contador")
    print("\n[2] Leer de excel")
    print("\n[3] Guardar en la DB")
    print("\n[4] Leer de la DB")
    print("\n[5] Salir")

def GradesMenu():
    while True:
        menu()
        menuOpcion = input("\nInserte una opcion >> ")
        # menuOpcion = '3'
        if menuOpcion == '1':
            keyFile = input('Nombre del archivo para la llave de AES: ')
            counterFile = input('Nombre del archivo para el contador de AES: ')
            # keyFile, counterFile = 'llave', 'contador'
            KeyCounterGenerator(keyFile, counterFile)

            input("\nTeclea cualquier letra para continuar. ")

        elif menuOpcion == '2':
            script_directory = os.path.dirname(__file__)
            grades = input('Nombre del archivo de calificaciones (.xls): ')

            # abre el archivo .xls
            wb = xlrd.open_workbook(f'{script_directory}/{grades}')
            
            # se extrae la información del excel
            sheet = wb.sheet_by_index(0)
            sheet.cell_value(0, 0)
            IDmateria=sheet.cell_value(1,2)
            sheet.cell_value(0,0)

            for i in range(3,sheet.nrows):
                boleta,name,calificacion=sheet.row_values(i)
                print(f'{int(boleta)} {name} {calificacion}')

            input("\nTeclea cualquier letra para continuar. ")

        elif menuOpcion == '3':
            script_directory = os.path.dirname(__file__)

            keyFile = input('Nombre del archivo de la llave de AES: ')
            counterFile = input('Nombre del archivo del contador de AES: ')
            # keyFile, counterFile = 'llave', 'contador'

            key = b64.b64decode(GetData(f'{keyFile}.txt'))
            countf = eval(b64.b64decode(GetData(f'{counterFile}.txt')).decode('utf-8'))
            # print(f'key: {key} \ncounter: {countf} \ntipo: {type(countf)}')

            encrypto = AES.new(key, AES.MODE_CTR, counter = countf)
            insertAlumno = "INSERT INTO alumno (Boleta, Nombre) VALUES (%s, %s)"
            insertNota = "INSERT INTO nota (idAsig,calificacion,idAlumno) VALUES (%s,%s,%s)"
            grades = input('Nombre del archivo de calificaciones (.xls): ')
            # grades = 'calificaciones.xls'

            wb = xlrd.open_workbook(f'{script_directory}/{grades}')
            sheet = wb.sheet_by_index(0)
            sheet.cell_value(0, 0)
            IDmateria = sheet.cell_value(1,2)
            sheet.cell_value(0,0)

            connection = DBconnection()
            mycursor = connection.cursor()
            for i in range(3,sheet.nrows):
                boleta, name, calificacion = sheet.row_values(i)
                byteGrades = f"{calificacion}".encode('utf-8')

                encryptedGrades = encrypto.encrypt(byteGrades)
                b64g = str(b64.b64encode(encryptedGrades))

                # print(byteGrades)
                # print(encryptedGrades)
                # print(b64g)
                # print('\n')

                valuesAlumno = (int(boleta), name)
                mycursor.execute(insertAlumno, valuesAlumno)
                valuesNota = (IDmateria, b64g, int(boleta))
                mycursor.execute(insertNota, valuesNota)
            
            connection.commit()
            print("\nInformación registrada exitosamente")

            input("\nTeclea cualquier letra para continuar. ")

        elif menuOpcion == '4':
            script_directory = os.path.dirname(__file__)

            keyFile = input('Nombre del archivo de la llave de AES: ')
            counterFile = input('Nombre del archivo del contador de AES: ')
            # keyFile, counterFile = 'llave', 'contador'

            key = b64.b64decode(GetData(f'{keyFile}.txt'))
            countf = eval(b64.b64decode(GetData(f'{counterFile}.txt')).decode('utf-8'))
            myPrefix = countf['prefix']
            # print(f'key: {key} \ncounter: {countf} \ntipo: {type(countf)} \nprefijo: {myPrefix}\n')

            connection = DBconnection()
            mycursor = connection.cursor()
            query = "select alumno.Nombre, asignatura.nombreMat, nota.calificacion from ((nota inner join alumno on nota.idAlumno=alumno.Boleta) inner join asignatura on asignatura.ID=nota.idAsig)"
            mycursor.execute(query)
            myResult = mycursor.fetchall()

            counterCreado = Counter.new(64, prefix= myPrefix, suffix=b'', initial_value=1, little_endian=False, allow_wraparound=False)
            decrypto = AES.new(key, AES.MODE_CTR, counter = counterCreado)

            for x in myResult:
                # b64.b64encode(encrypto.encrypt(byteGrades))
                a = eval(x[2])
                b = b64.b64decode(a)
                c = decrypto.decrypt(b)
                # d = b64.b64decode(b)
                # e = b64.b64encode(d)

                # print(f'cal: {a} \t tipo: {type(a)}')
                # print(f'cal: {b} \t tipo: {type(b)}')
                # print(f'cal: {c} \t tipo: {type(c)}')
                # print(f'cal: {d} \t tipo: {type(d)}')
                # print(f'cal: {e} \t tipo: {type(e)}')
                print(f'Alumno: {x[0]} \tMateria: {x[1]} \tCalificación: {c}\n')
                # print('\n')

            input("\nTeclea cualquier letra para continuar. ")

        else:
            print('\nFinalizando aplicación ... ')
            break

# GradesMenu()