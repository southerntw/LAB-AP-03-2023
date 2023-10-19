angka = list(map(int, input("Masukkan Beberapa Angka: ").split()))
genap, ganjil, habis5 = set(), set(), set()
for i in angka:
    if i % 2 == 0:
        genap.add(i)
    if i % 2 != 0:
        ganjil.add(i)
    if i % 5 == 0:
        habis5.add(i)

genap = list(genap)
ganjil = list(ganjil)
habis5 = list(habis5)

print(f"Angka Genap: {genap}\nAngka Ganjil:{ganjil}\nAngka yang Habis Dibagi 5:{habis5}")