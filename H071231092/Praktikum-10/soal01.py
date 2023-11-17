import re, os

class UserData:
    def __init__(self):
        self.data = {}

    def email_valid(self, email):
        # Validasi email dengan regular expression
        return re.match(r"^[a-z0-9]+@student.unhas.ac.id$", email)

    def password_valid(self, password):
        # Validasi password harus memiliki panjang 8-20 karakter, minimal 1 huruf kapital, kecil, dan angka
        return 8 <= len(password) <= 20 and any(char.isupper() for char in password) \
               and any(char.islower() for char in password) and any(char.isdigit() for char in password)

    def melihat_data(self):
        # Menampilkan data jika ada kalo tidak ada menampilkan
        if all(value is None for value in self.data.values()):
            print("="*50)
            print("Data saat ini kosong")
        else:
            
            for key, value in self.data.items():
                print(f"{key}: {value}")
        

    def cari_data(self):
            nama_file = input("Masukkan nama file tanpa format (.txt): ")
            if os.path.exists(f"{nama_file}.txt"):
                with open(f"{nama_file}.txt") as files:
                    teks = files.read()
                    jumlah = teks.count("+===================================================================================")
                    jumlah2 = -2 + jumlah
                print(f'Jumlah Data Pada File : {jumlah2}')
                pass
            else:
                print(f'Tidak Terdapat File dengan nama {nama_file}.txt')

    def ubah_name(self):
        # Mengubah nama
        if not self.data:
            print("="*50)
            print("Data saat ini kosong")
        else:
            new_name = input("Masukkan nama baru: ")
            self.data['Nama'] = new_name
            print("Nama berhasil diubah")

    def save_to_file(self, file_name):
        # Menyimpan data
        if not self.data:
            print("="*50)
            print("Data saat ini kosong")
        else:
            gambar = f'''
            +===================================================================================
            |Data yang Tersimpan
            +===================================================================================
            Nama         : {self.data['Nama']}
            Email        : {self.data['Email']}
            Password     : {self.data['Password']}
            +==================================================================================='''

            tambah_gambar = f'''
            Nama         : {self.data['Nama']}
            Email        : {self.data['Email']}
            Password     : {self.data['Password']}
            +==================================================================================='''
            file_path = f"{file_name}.txt"
            if not os.path.exists(file_path):
                with open(file_path, 'w') as file:
                    file.write(gambar)

            else:
                with open(file_path, 'a') as file2:
                    file2.write(tambah_gambar)

            print("="*50)
            print("Berhasil menyimpan data")

    def membuat_data(self):
        # Membuat data baru
        nama = input("Masukkan Nama: ")
        email = input("Masukkan Email: ")
        password = input("Masukkan Password: ")

        if not self.email_valid(email):
            print("Email yang Anda Masukkan Salah")
            return

        if not self.password_valid(password):
            print("Password yang Anda masukkan terlalu lemah, gunakan minimal 1 huruf kapital, huruf kecil, dan angka")
            return

        self.data = {'Nama': nama, 'Email': email, 'Password': password}
        print("="*50)
        print("Data baru berhasil dibuat")

    def menu_exit(self):
        print("Sampai Jumpa Lagi")
        exit()


def main():
    user_data = UserData()

    while True:
        # Menampilkan menu
        print("="*50)
        print("Selamat Datang Silahkan Pilih Opsi Menu Anda")
        print("a. Detail Anda")
        print("b. Ubah Nama")
        print("c. Jumlah Data Saat Ini")
        print("d. Save Data pada File")
        print("e. Buat Data Baru")
        print("f. Keluar")

        # Menerima pilihan menu dari pengguna
        choice = input("Silahkan Pilih Opsi : ").lower()

        # Memproses pilihan menu
        if choice == 'a':
            user_data.melihat_data()
        elif choice == 'b':
            user_data.ubah_name()
        elif choice == 'c':
            user_data.cari_data()
        elif choice == 'd':
            file_name = input("Masukkan nama file tanpa format (.txt): ")
            user_data.save_to_file(file_name)
        elif choice == 'e':
            user_data.membuat_data()
        elif choice == 'f':
            user_data.menu_exit()
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")


main()
