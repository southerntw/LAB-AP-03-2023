import re

def validasi_string(input_string):
    # Memeriksa panjang string
    # if len(input_string) != 15:
    #     return False

    # # Memeriksa 40 karakter pertama
    # if not re.match(r'^[a-zA-Z0-9]*[02468]*$', input_string[:10]):
    #     return False

    # # Memeriksa 5 karakter terakhir
    # if not re.match(r'^[13579\s]*$', input_string[10:]):
    #     return False
    
    if not re.match(r'^[a-zA-Z02468]{40}[13579\s]{5}$'):
        return False

    return True

input_string = input("Masukkan string : ")

if validasi_string(input_string):
    print("String valid sesuai dengan syarat.")
else:
    print("String tidak valid sesuai dengan syarat.")
