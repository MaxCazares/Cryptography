from _AES_ import *

GenerationAESKey(16, '16Key.txt')
# GenerationAESKey(24, '24Key.txt')
# GenerationAESKey(32, '32Key.txt')
# GenerationAESiv('iv.txt')

key_filename = '16Key.txt'
# key_filename = '24Key.txt'
# key_filename = '32Key.txt'

iv = bytes.fromhex('80000000000000000000000000000000')
iv = 'iv.txt'

file_to_encrypt = 'secretdata.txt'
file_to_decrypt = 'secretdata.aes'

mode_operation = AES.MODE_OFB
mode_operation = AES.MODE_CFB

AESCipher(file_to_encrypt, key_filename, iv, mode_operation)
AESDecipher(file_to_decrypt, key_filename, iv, mode_operation)