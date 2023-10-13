def maksimum(*number):
    if not number:
        return None

    maks = number[0]
    for angka_terbesar in number:  # at =8
        if angka_terbesar > maks:  # 8 > 5
            maks = angka_terbesar  # 8
    return maks


input_angka = input("\nMasukkan Beberapa Angka (Pisahkan Dengan Spasi): ")
angka = [int(x) for x in input_angka.split()]
terbesar = maksimum(*angka)

if terbesar is not None:
    print(f">> {terbesar}")
else:
    print("Invalid. Masukkan Angka")
print(angka)
