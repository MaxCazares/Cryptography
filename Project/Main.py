import os
import time 
from DigitalSignature import *
from AES_Excel import *

def menu():
	os.system('clear') 
	print ("Selecciona una opción")
	print ("\n1 - Generar llaves")
	print ("\n2 - Firma digital")
	print ("\n3 - Verificar firma")
	print ("\n4 - Salir")

while True:
	menu()
	opcionMenu = input("\nInserta una opcion >> ")

	if opcionMenu == "1":
		privateKey = input('Nombre del archivo para la llave privada: ')
		publicKey = input('Nombre del archivo para la llave publica: ')
		KeyGenerator(f'{privateKey}.pem', f'{publicKey}.pem')
		print('\nLlaves generadas exitosamente.')
		input("\nTeclea cualquier letra para continuar ")

	elif opcionMenu == "2":
		fileGrades = input('Nombre del archivo de calificaciones: ')
		publicKey = input('Nombre del archivo de la llave publica: ')
		encryptedFile = input('Nombre del archivo para la firma digital: ')

		grades = GetBytesFromFile(fileGrades)
		HASHgrades = Hash256(grades)
		RSAEncrypt(HASHgrades, f'{encryptedFile}.bin',  f'{publicKey}.pem')

		print('\nFirma realizada correctamente.')
		input("\nTeclea cualquier letra para continuar ")

	elif opcionMenu == "3":
		fileGrades = input('Nombre del archivo de calificaciones: ')
		privateKey = input('Nombre del archivo para la llave privada: ')
		encryptedFile = input('Nombre del archivo de la firma digital: ')
		
		grades = GetBytesFromFile(fileGrades)
		HASHgrades = Hash256(grades)
		DecryptedGrades = RSADecrypt(f'{encryptedFile}.bin', f'{privateKey}.pem')
		print('\nVerificación de firma realizada correctamente. ')
		
		if HASHgrades == DecryptedGrades:
			print('\nLas calificaciones NO sufrieron modificaciones')
			time.sleep(3)
			print('\nLlevando al siguiente menu ...')
			time.sleep(3)
			GradesMenu()
			input("\nTeclea cualquier letra para continuar.")
		else:
			print('\nLas calificaciones SI sufrieron modificaciones')
			input("\nTeclea cualquier letra para continuar ")
	else:
		print('\nFinalizando aplicación ... ')
		break