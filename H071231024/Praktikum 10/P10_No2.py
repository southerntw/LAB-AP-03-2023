import os


def clear():
    os.system("cls")


clear()

from abc import ABC, abstractmethod


class InvalidInputError(Exception):
    pass


class Player(ABC):
    def __init__(self, nama, umur):
        self._nama = nama
        self._umur = umur

    def get_nama(self):
        return self._nama

    def get_umur(self):
        return self._umur

    @abstractmethod
    def ke_badakan(self):
        pass


class Immortal(Player):
    def ke_badakan(self):
        return f"{self._nama} Berusia {self._umur}, dan Dia Pro."


class Badak(Player):
    def ke_badakan(self):
        return f"{self._nama} Berusia {self._umur}, dan Dia Beban."


Manusia = []
while True:
    print("\n" + "=" * 40)
    print('---- CEK KE "BEBAN" AN (AKURASI 100%) ----')
    print("=" * 40 + "\n")
    print("Menu:")
    print("1. Tambah Player")
    print("2. Tampilkan Data Player")
    print("3. Keluar")

    try:
        print("=" * 40)
        Milihdong = input("Pilih Menu (Angka 1-3) : ")

        if Milihdong not in ["1", "2", "3"]:
            raise InvalidInputError("Pilihan Tidak Valid. Pilih Angka 1-3")

        if Milihdong == "1":
            clear()
            print("=" * 40)
            while True:
                nama = input("Masukkan Nama: ")
                if all(char.isalpha() or char == "." or char == " " for char in nama):
                    break
                else:
                    print(
                        "Nama Hanya Boleh Mengandung Huruf, Spasi dan Titik. Silakan Coba Lagi."
                    )

            while True:
                try:
                    umur = int(input("Masukkan Umur: "))
                    break
                except ValueError:
                    print("Error: Masukkan Umur Harus Berupa Angka. Silakan Coba Lagi.")

            while True:
                BadakMilih = input("Apakah Player Ini Terlalu Beban? (Y/T): ").upper()
                if BadakMilih in ["Y", "T"]:
                    break
                else:
                    print(
                        "Pilihan Tidak Valid. Harap Masukkan 'Y' atau 'T'. Silakan Coba Lagi."
                    )

            clear()

            if BadakMilih == "Y":
                player = Badak(nama, umur)
            else:
                player = Immortal(nama, umur)

            Manusia.append(player)

            print("Player Telah Ditambahkan")

        elif Milihdong == "2":
            clear()
            print("=" * 40)
            if not Manusia:
                print("Belum Ada Data Player")
                print("=" * 40)
            else:
                Manusia.sort(key=lambda x: isinstance(x, Immortal), reverse=True)

                for orang in Manusia:
                    print(orang.ke_badakan())
                print("=" * 40)

        elif Milihdong == "3":
            print("Program End Bruh")
            print("=" * 40)
            break

    except ValueError:
        clear()
        print("=" * 40)
        print("Error: Masukkan Umur (Harus Berupa Angka!) : ")

    except InvalidInputError as pesan:
        clear()
        print("=" * 40)
        print(f"Error: {pesan}")

    input("Tekan Enter Untuk Melanjutkan!")
    clear()
