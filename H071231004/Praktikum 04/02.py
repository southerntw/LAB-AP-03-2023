def palindrom(x):
    print(x.lower())
    print(x[::-1].lower())
    if x.lower() == x[::-1].lower():
        print('Palindrom')
    else:
        print('Bukan Palindrom')

palindrom('Radar')
# nama = input('Masukkan nama: ')
# palindrom(nama)