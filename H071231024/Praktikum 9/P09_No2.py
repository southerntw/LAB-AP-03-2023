class Mahasiswa:
    def __init__(self, nama, nim, prodi, ipk):
        self.nama = nama
        self.NIM = nim
        self.prodi = prodi
        self.IPK = ipk

    def info(self, nama, nim, prodi, ipk):
        print(
            f"Nama Mahasiswa     : {nama}\nNIM                : {nim}\nProdi              : {prodi}\nIPK                : {ipk} \n{'='*50}"
        )

    def for_predikat(self):
        if self.IPK >= 3.5:
            print("CUMLAUDE")
        elif self.IPK >= 3.0:
            print("Sangat Memuaskan")
        elif self.IPK >= 2.5:
            print("Memuaskan")
        elif self.IPK >= 2.0:
            print("Cukup")
        else:
            print("Kurang")

        print("=" * 50)


def Pilihan(nama, nim, prodi, ipk):
    Variable = Mahasiswa(nama, nim, prodi, ipk)

    while True:
        print(
            f"Opsi Pilihan       :\n1.  Tampilkan Data\n2.  Tampilkan Predikat\n3.  Keluar\n{'='*50}"
        )
        opsi = int(input("Pilih Opsi         : "))
        print("=" * 50)

        if opsi == 3:
            print(f"Selamat Tinggal {nama}\n{'='*50}")
            exit()
        elif opsi == 1 or opsi == 2:
            if opsi == 1:
                Variable.info(nama, nim, prodi, ipk)
                Pilihan(nama, nim, prodi, ipk)

            elif opsi == 2:
                Variable.for_predikat()
                Pilihan(nama, nim, prodi, ipk)
        else:
            print("Invalid. Mohon Masukkan Angka Yang Benar!")


Nama = input("Masukkan Nama      : ")
Nim = input("Masukkan NIM       : ")
prodi = input("Masukkan Prodi     : ")
while True:
    try:
        Ipk = float(input("Masukkan IPK       : "))
        break
    except:
        print("Invalid. Masukkan Angka Desimal!")

print("=" * 50)
Pilihan(Nama, Nim, prodi, Ipk)
