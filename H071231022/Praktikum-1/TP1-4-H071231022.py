karakter = input('masukan karakter: ')

huruf_kapital = (karakter.isupper()) 
huruf_kecil = (karakter.islower()) 
angka = (karakter.isdigit())

print(f'karakter huruf kapital? {huruf_kapital}')
print(f'karakter huruf kecil? {huruf_kecil}')
print(f'Angka? {angka}')
