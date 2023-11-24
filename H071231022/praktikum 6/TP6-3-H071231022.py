def kategori_angka(input_angka):
    list_angka = list(map(int, input_angka.split()))

    ganjil = set()
    genap = set()
    habis_dibagi_5 = set()

    for i in list_angka:
        if i % 2 == 1:
            ganjil.add(i)
        elif i % 2 == 0:
            genap.add(i)
        if i % 5 == 0:
            habis_dibagi_5.add(i)

    return ganjil, genap, habis_dibagi_5

input_angka = input("Masukkan beberapa angka: ")

ganjil, genap, habis_dibagi_5 = kategori_angka(input_angka)

print("Angka yang habis dibagi 5:", list(habis_dibagi_5))
print("Angka genap:",list (genap))
print("Angka ganjil:",list (ganjil))