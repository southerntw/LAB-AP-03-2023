input_angka = input("Masukkan Beberapa Angka : ").split()

angka_genap = set()
angka_ganjil = set()
angka_habis_dibagi_5 = set()

for angka in input_angka:
    angka = int(angka)

    if angka % 2 == 0:
        angka_genap.add(angka)
    else:
        angka_ganjil.add(angka)

    if angka % 5 == 0:
        angka_habis_dibagi_5.add(angka)

print("Angka Genap:", angka_genap)
print("Angka Ganjil:", angka_ganjil)
print("Angka Yang Habis Dibagi 5:", angka_habis_dibagi_5)
