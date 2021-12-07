import os
import time
from DigitalSignature import *

def menu():
	os.system('clear') 
	print ("Selecciona una opción")
	print ("\n1 - Generar LLaves")
	print ("\n2 - Cifrar")
	print ("\n3 - Comparar")
	print ("\n4 - Salir")

while True:
	menu()
	opcionMenu = input("\nInserta una opcion >> ")

	if opcionMenu == "1":
		privateKey = input('Nombre del archivo para la llave privada: ')
		publicKey = input('Nombre del archivo para la llave publica: ')
		KeyGenerator(f'{privateKey}.pem', f'{publicKey}.pem')
		print('\nLlaves generadas exitosamente.')
		input("\nTeclea cualquier letra para continuar.")

	elif opcionMenu == "2":
		fileGrades = input('Nombre del archivo de calificaciones: ')
		publicKey = input('Nombre del archivo de la llave publica: ')
		encyptedFile = input('Nombre del archivo para el mensaje cifrado: ')

		grades = GetBytesFromFile(fileGrades)
		HASHgrades = Hash256(grades)
		RSAEncrypt(HASHgrades, f'{encyptedFile}.bin',  f'{publicKey}.pem')
		print('\nArchivo de calificaciones cifrado correctamente.')
		input("\nTeclea cualquier letra para continuar.")

	elif opcionMenu == "3":
		fileGrades = input('Nombre del archivo de calificaciones: ')
		privateKey = input('Nombre del archivo para la llave privada: ')
		encyptedFile = input('Nombre del archivo del mensaje cifrado: ')
		
		grades = GetBytesFromFile(fileGrades)
		HASHgrades = Hash256(grades)
		DecryptedGrades = RSADecrypt(f'{encyptedFile}.bin', f'{privateKey}.pem')
		print('\nHash de calificaciones decrifrado correctamente.')
		
		if HASHgrades == DecryptedGrades:
			print('\nLas calificaciones NO sufrieron modificaciones')
			input("\nTeclea cualquier letra para continuar.")
		else:
			print('\nLas calificaciones SI sufrieron modificaciones')
			input("\nTeclea cualquier letra para continuar.")
	else:
		print('\nFinalizando aplicación ...')
		time.sleep(5)
		break