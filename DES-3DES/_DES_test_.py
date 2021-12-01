from _DES_ import *
from _3DES_ import *

# 3DES: Predefined
# file_to_encrypt = 'Triple/lorem.txt'
# key_filename = 'Triple/key.txt'
# iv_filename = 'Triple/IV.txt'
# file_to_decrypt = 'Triple/lorem.des'

# Generation3DESKey(key_filename)
# Generation3DESIV(iv_filename)
# Predefined3DESCipher(file_to_encrypt, key_filename, iv_filename)
# Predefined3DESDecipher(file_to_decrypt, key_filename, iv_filename)

# 3DES: EEE DES
file_to_encrypt = 'Single/ejemplo.txt'
key_filename = 'Single/keys.txt'
iv_filename = 'Single/IVs.txt'
file_to_decrypt = 'Single/ejemplo.des'

GenerationDESKey(key_filename)
GenerationDESIV(iv_filename)
DESEEECipher(file_to_encrypt, key_filename, iv_filename)
DESEEEDecipher(file_to_decrypt, key_filename, iv_filename)