import re
import os

class Data:
    def __init__(self):
        self.data = {'Nama': '', 'Email': '', 'Password': ''}
        self.garis = "=" * 100

    def tampilkan_menu(self):
        print(self.garis)
        print("""Selamat Datang! Silahkan Pilih Opsi Menu Anda:
1. Detail Anda
2. Ubah Nama
3. Jumlah Data pada File
4. Save Data pada File
5. Buat Data Baru
6. Keluar""")
        print(self.garis)

    def detail_anda(self):
        if not any(self.data.values()):
            print(self.garis + "\nData saat ini kosong")
        else:
            print(self.garis + "\nData Anda adalah:")
            for key, value in self.data.items():
                print(f"{key}: {value}")

    def ubah_nama(self):
        if not any(self.data.values()):
            print(self.garis + "\nData saat ini kosong")
        else:
            nama_baru = input("Silahkan Input Nama Baru: ")
            self.data['Nama'] = nama_baru
            print(self.garis + "\nNama berhasil diubah")

    def jumlah_data(self):
        print(self.garis)
        nama_file = input("Silahkan Masukkan Nama File: ")
        try:
            with open(f"{nama_file}.txt", 'r') as file:
                hitung_data = sum(1 for baris in file)
                hitung_data -= 3
                hitung_data //= 4 
                print(f"Jumlah Data pada File: {hitung_data} Data")
        except FileNotFoundError:
            print(f"Tidak Terdapat File dengan Nama {nama_file}.txt")
            print("Jumlah Data pada File: 0 Data")

    def save_data(self):
        if not any(self.data.values()):
            print(self.garis + "\nData saat ini kosong")
        else:
            print(self.garis)
            nama_file = input("Silahkan Masukkan Nama File: ")
            with open(f'{nama_file}.txt', 'a') as file:
                isi_data = f"""
| Nama\t\t: {self.data['Nama']}
| Email\t\t: {self.data['Email']}
| Password\t: {self.data['Password']}
{self.garis}"""
                if os.path.getsize(f'{nama_file}.txt') == 0:
                    file.write(self.garis + "\nData yang Tersimpan\n" + self.garis)                
                file.write(isi_data)
            self.data = {}
            print("Berhasil menyimpan data!")

    def validasi_email(self, email):
        pattern = r'^[a-z0-9]+@student\.unhas\.ac\.id$'
        return re.search(pattern, email)

    def validasi_password(self, password):
        pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,}$"
        return re.search(pattern, password)

    def buat_data(self):
        print(self.garis)
        nama_baru = input("Silahkan Masukkan Nama Anda: ")
        while True:
            email_baru = input("Silahkan Masukkan Email Anda: ")
            if not self.validasi_email(email_baru):
                print(self.garis + "\nEmail yang Anda masukkan salah\n" + self.garis)
            else:
                break
        while True:
            password_baru = input("Silahkan Masukkan Password Anda: ")
            if not 8 <= len(password_baru) <= 20:
                print(self.garis + "\nPassword Harus Memiliki Panjang 8-20\n" + self.garis)
            elif not self.validasi_password(password_baru):
                print(self.garis + "\nPassword yang Anda Masukkan terlalu lemah")
                print("Gunakan Minimal 1 Huruf Kapital, Huruf Kecil, dan Angka\n" + self.garis)
            else:
                break

        self.data = {'Nama': nama_baru, 'Email': email_baru, 'Password': password_baru}
        print(self.garis + "\nData baru berhasil dibuat!")

    def keluar(self):
        print(self.garis + "\nSampai Jumpa Lagi!")
        exit()

    def run_program(self):
        while True:
            self.tampilkan_menu()
            opsi = int(input("Masukkan Opsi Pilihan Anda: "))

            opsi_menu = {
                1 : self.detail_anda,
                2 : self.ubah_nama,
                3 : self.jumlah_data,
                4 : self.save_data,
                5 : self.buat_data,
                6 : self.keluar
            }

            pilihan_menu = opsi_menu.get(opsi)
            if pilihan_menu:
                pilihan_menu()
            else:
                print("Menu tidak valid. Silakan pilih kembali.")

data_manager = Data()
data_manager.run_program()