import os
import re


def clear():
    os.system("cls")


def Grishias(n):
    return f'{"=" * n}'


def Gristgh(kata):
    return f"|{kata.center(60)}|"


def Grisujung(kata):
    return f"|{kata.ljust(60)}|"


class Data_User:
    def __init__(self, nama, email, password):
        self.Nama = nama
        self.Email = email
        self.__Password = password

    def get_Password(self):
        return self.__Password

    def set_Password(self, passbaru):
        self.__Password = passbaru


clear()
while True:
    print(
        f"""+{Grishias(60):^60}+
{Gristgh("Selamat Datang! Silahkan Pilih Opsi Menu Anda")}
|{("-" * 60):^60}|
{Grisujung("1. Detail Anda")}
{Grisujung("2. Ubah Nama")}
{Grisujung("3. Jumlah Data Pada File")}
{Grisujung("4. Save Data Pada File")}
{Grisujung("5. Buat Data Baru")}
{Grisujung("6. Keluar")}
+{Grishias(60):^60}+"""
    )

    Milih = int(input(" Masukan Opsi Pilihan: "))
    print(f"+{Grishias(60):^60}+")

    match Milih:
        case 1:
            try:
                if User.Nama:
                    pass
                elif User.Nama == None:
                    raise NameError
                clear()

                print(
                    f'+{Grishias(60):^60}+\n{Gristgh("Detail Anda")}\n+{Grishias(60):^60}+'
                )
                print(f'{Grisujung(f"Nama     : {User.Nama}")}')
                print(f'{Grisujung(f"Email    : {User.Email}")}')
                print(f'{Grisujung(f"Password : {User.get_Password()}")}')

            except:
                print(f'{"-" * 62}\n{"Data Saat Ini Kosong":^62}\n{"-" * 62}')

        case 2:
            try:
                if User.Nama:
                    pass
                elif User.Nama == None:
                    raise NameError
                clear()

                print(
                    f'+{Grishias(60):^60}+\n{Gristgh("Ubah Nama")}\n+{Grishias(60):^60}+'
                )

                while True:
                    Nama_Baru = input("Masukkan Nama Baru : ")

                    if (
                        Nama.replace(" ", "").replace(".", "").isalpha()
                        and len(Nama.replace(" ", "").replace(".", "")) > 0
                    ):
                        break
                    else:
                        print(
                            f'{"-" * 62}\n{"Nama Tidak Valid. Coba lagi":^62}\n{"-" * 62}'
                        )

                User.Nama = Nama_Baru

                print(
                    f'+{Grishias(60):^60}+\n|{f"Berhasil":^60}|\n|{f"Nama telah diubah":^60}|\n+{Grishias(60):^60}+'
                )

            except:
                print(f'{"-" * 62}\n{"Data Saat Ini Kosong":^62}\n{"-" * 62}')

        case 3:
            clear()
            print(
                f'+{Grishias(60):^60}+\n{Gristgh("Jumlah Data Pada File")}\n+{Grishias(60):^60}+'
            )

            path = "D:\Algoritma dan Pemrograman\Praktikum 10"
            os.chdir(path)

            Files = input("Masukkan Nama file : ") + ".txt"

            if not os.path.exists(Files):
                print(
                    f'{"-" * 62}\n{f"Tidak Terdapat File Dengan Nama {Files}":^62}\n{"Jumlah Data Pada File : 0 Data":^62}\n{"-" * 62}'
                )
            else:
                with open(Files, "r") as R:
                    baris = len(R.readlines())
                    Banyak_Data = (baris - 3) // 4

                    print(
                        f'+{Grishias(60):^60}+\n|{f"Berhasil":^60}|\n|{f"Jumlah Data Pada File : {Banyak_Data} Data":^60}|\n+{Grishias(60):^60}+'
                    )

        case 4:
            path = "D:\Algoritma dan Pemrograman\Praktikum 10"
            os.chdir(path)
            try:
                if User.Nama:
                    pass
                clear()

                print(
                    f'+{Grishias(60):^60}+\n{Gristgh("Save Data Pada File")}\n+{Grishias(60):^60}+'
                )

                Files = input("Masukkan Nama File : ") + ".txt"

                if not os.path.exists(Files):
                    with open(Files, "w") as F:
                        F.write(f"+{Grishias(60):^60}+\n")
                        F.write(f'{Gristgh("DATA YANG TERSIMPAN")}\n')
                        F.write(f"+{Grishias(60):^60}+\n")
                        F.write(f'{Grisujung(f"Nama         : {User.Nama}")}\n')
                        F.write(f'{Grisujung(f"Email        : {User.Email}")}\n')
                        F.write(
                            f'{Grisujung(f"Password     : {User.get_Password()}")}\n'
                        )
                        F.write(f"+{Grishias(60):^60}+")

                        User = Data_User(nama=None, email=None, password=None)
                else:
                    with open(Files, "a") as F:
                        F.write(f'\n{Grisujung(f"Nama         : {User.Nama}")}\n')
                        F.write(f'{Grisujung(f"Email        : {User.Email}")}\n')
                        F.write(
                            f'{Grisujung(f"Password     : {User.get_Password()}")}\n'
                        )
                        F.write(f"+{Grishias(60):^60}+")

                        User = Data_User(nama=None, email=None, password=None)

                print(
                    f'+{Grishias(60):^60}+\n{Gristgh("Berhasil")}\n+{Grishias(60):^60}+'
                )

            except:
                print(f'{"-" * 62}\n{"Data Saat Ini Kosong":^62}\n{"-" * 62}')

        case 5:
            clear()
            print(
                f'+{Grishias(60):^60}+\n{Gristgh("Buat Data Baru")}\n+{Grishias(60):^60}+'
            )

            while True:
                Nama = str(input("Masukkan Nama Anda \t : "))

                if (
                    Nama.replace(" ", "").replace(".", "").isalpha()
                    and len(Nama.replace(" ", "").replace(".", "")) > 0
                ):
                    break
                else:
                    print(
                        f'{"-" * 62}\n{"Nama Tidak Valid. Coba Lagi":^62}\n{"-" * 62}'
                    )

            while True:
                Email = str(input("Masukkan Email Anda \t : "))
                Ses_email = re.match(r"^[a-z0-9]{2,}@student\.unhas\.ac\.id$", Email)

                if Ses_email:
                    break
                else:
                    print(
                        f'{"-" * 62}\n{"Email yang Anda Masukkan Salah. Coba Lagi":^62}\n{"-" * 62}'
                    )

            while True:
                Password = str(input("Masukkan Password Anda : "))
                Panjang_Password = re.match(r".{8,20}", Password)
                Ses_pass = re.match(
                    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]+$", Password
                )

                if Panjang_Password:
                    if Ses_pass:
                        break
                    else:
                        print(
                            f'{"-" * 62}\n{"Password yang Anda Masukkan Terlalu Lemah":^62}\n{" Gunakan Minimal 1 Huruf Kapital, Huruf Kecil, dan Angka":^62}\n{"-" * 62}'
                        )
                else:
                    print(
                        f'{"-" * 62}\n{"Password Harus Memiliki Panjang 8-20":^62}\n{"-" * 62}'
                    )

            User = Data_User(Nama, Email, Password)
            print(
                f'+{Grishias(60):^60}+\n{Gristgh("Data Telah Dibuat, Silahkan Save!")}\n+{Grishias(60):^60}+'
            )

        case 6:
            clear()
            print(
                f'+{Grishias(60):^60}+\n{Gristgh("Sampai Jumpa Bro/Sis")}\n+{Grishias(60):^60}+'
            )
            break

        case _:
            print(f'{"-" * 62}\n{"Opsi Tidak Valid. Coba Lagi":^62}\n{"-" * 62}')
