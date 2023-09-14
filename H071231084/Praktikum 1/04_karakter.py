#Pengujian Jenis Karakter
print("Pengujian jenis karakter")
x = input("Masukkan karakter: ")

print(f"Huruf Kapital?" , "A" <= x <= "Z")
print(f"Huruf Kecil?" , "a" <= x <= "z")
print(f"Angka?" , "0" <= x <= "9")