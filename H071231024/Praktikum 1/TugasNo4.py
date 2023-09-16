jdl = '\nProgram Menentukan Huruf Kapital dan Angka'
grs = '=========================================='
print(f'{jdl}\n{grs}\n')

character = input('Pengujian Jenis Karakter!\nMasukkan Karakter : ')

uppercase  =  False
lowercase = False
number = False

for ch in character:
    if ch .isupper():
        uppercase = True
    elif ch .islower():
        lowercase = True
    elif ch .isdigit():
        number = True
        
print('Huruf Kapital? -->',uppercase)
print('Huruf Kecil? -->',lowercase)
print('Angka? -->',number)
