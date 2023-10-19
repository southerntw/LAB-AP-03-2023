angka = input("Masukkan Beberapa Angka : ").split()
angka = list(map(int, angka))
genap, ganjil, habis5 = set(), set(), set()
for i in angka:
    if i % 2 == 0:
        genap.add(i)
    if i % 2 != 0:
        ganjil.add(i)
    if i % 5 == 0:
        habis5.add(i)
print(f"\nAngka Genap : {genap}\nAngka Ganjil : {ganjil}\nAngka yang habis dibagi 5 : {habis5}")