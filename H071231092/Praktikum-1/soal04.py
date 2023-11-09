# Inputan berupa karakter huruf dan angka
print("Pengujian jenis karakter")
print("-"*24)
karakter = input('karakter = ')

# Menentukan True or False
huruf_kapital = karakter >= 'A' and karakter <= 'Z'
huruf_kecil = karakter >= 'a' and karakter <= 'z'
angka = karakter >= '0' and karakter <= '9'

print(f"huruf Kapital?: {huruf_kapital}")
print(f"huruf Kecil?: {huruf_kecil}")
print(f"Angka?: {angka}")