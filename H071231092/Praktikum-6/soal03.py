# Mengambil input angka-angka
input_string = input("Masukkan beberapa angka: ")
input_values = input_string.split()  # Membaca input sebagai string dan memisahkan berdasarkan spasi

# Inisialisasi tiga list kosong untuk masing-masing kelompok
angka_genap = []
angka_ganjil = []
angka_habis_dibagi_5 = []

# Mengkategorikan angka-angka
for input_value in input_values:
    angka = int(input_value)
    if angka % 2 == 0 and angka != 0:
        angka_genap.append(angka)
    elif angka % 2 == 1:
        angka_ganjil.append(angka)
    if angka % 5 == 0 and angka != 0:
        angka_habis_dibagi_5.append(angka)

# Menampilkan hasil kategorisasi
print(f"Angka Genap: {list(set(angka_genap))}")
print(f"Angka Ganjil: {set(angka_ganjil)}".replace("{", "[").replace("}", "]"))
print(f"Angka yang habis dibagi 5: {set(angka_habis_dibagi_5)}".replace("{", "[").replace("}", "]"))

