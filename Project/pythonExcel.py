# Reading an excel file using Python
from sys import hexversion
import xlrd
import os
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto import Random
from xlrd.biffh import hex_char_dump
import mysql.connector



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="gradesCrypto"
)


# Give the location of the file
loc ="calificaciones.xls"
# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

# Set up the counter with a nonce.
# 64 bit nonce + 64 bit counter = 128 bit output
nonce = Random.get_random_bytes(8)
countf = Counter.new(64, nonce)
key = Random.get_random_bytes(32) # 256 bits key

# Instantiate a crypto object first
#for encryption
encrypto = AES.new(key, AES.MODE_CTR, counter = countf)

#encrypted = encrypto.encrypt(bin())

# Reset counter and instantiate a new crypto object
#for decryption
countf = Counter.new(64, nonce)
print(countf)
decrypto = AES.new(key, AES.MODE_CTR, counter = countf)
#print (decrypto.decrypt(encrypted)) # prints "asdk"
#encrypted=encrypto.encrypt(f'{8.5}'.encode('utf-8'))
#print(encrypted)



#para la conexion con la DB
mycursor=mydb.cursor()
#querys
insertAlumno="INSERT INTO alumno (Boleta, Nombre) VALUES (%s, %s)"
#insertMateria=""
insertNota="INSERT INTO nota (idAsig,calificacion,idAlumno) VALUES (%s,%s,%s)"
"""


"""


IDmateria=sheet.cell_value(1,2)
sheet.cell_value(0,0)
#este ciclo extrae informacion del excel, meter los query aqui
for i in range(3,sheet.nrows):
  boleta,name,calificacion=sheet.row_values(i)
  encrypted = encrypto.encrypt(f'{calificacion}'.encode('utf-8'))
  valuesAlumno=(int(boleta),name)
  mycursor.execute(insertAlumno, valuesAlumno)
  valuesNota=(IDmateria,encrypted,int(boleta))
  mycursor.execute(insertNota, valuesNota)

mydb.commit()
print("Registros insertados exitosamente")
print("haciendo una consulta a la DB utilizando CTR")
print(countf)

queryConsulta="select calificacion from nota"
mycursor.execute(queryConsulta)
myResult=mycursor.fetchall()
for x in myResult:
  print (float(decrypto.decrypt(x[0])))
    