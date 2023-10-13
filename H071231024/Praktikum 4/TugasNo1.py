inputUser = input("\nMasukkan Kata: ")


def stringpermutation(kata):
    try:
        per = []
        v = len(kata)
        for i in range(v):
            rotasi = kata[i:] + kata[0:i]
            per.append(rotasi)
        print(" | ".join(reversed(per)), "|")
    except TypeError:
        print("Terjadi Kesalahan: Input Tidak Valid")


stringpermutation(inputUser)
