data_detail = {"Nama": "", "Umur": "", "Alamat": ""}

data_detail["Nama"] = input("Input Nama: ")
data_detail["Umur"] = input("Input Umur: ")
data_detail["Alamat"] = input("Input Alamat: ")

while True:
    print("==================================================")
    print("Selamat Datang", data_detail["Nama"], "Silahkan Pilih Opsi")
    print("==================================================")
    print("1. Detail Anda")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")
    print("==================================================")

    opsi = input("Input Opsi: ")

    if opsi == "1":
        print("==================================================")
        print("Data Anda Adalah")
        print("Nama:", data_detail["Nama"])
        print("Umur:", data_detail["Umur"])
        print("Alamat:", data_detail["Alamat"])
        print("==================================================")
    elif opsi == "2":
        namaBaru = input("Silahkan Input Nama Baru: ")
        data_detail["Nama"] = namaBaru
        print("Data Anda Sukses Diperbarui")
    elif opsi == "3":
        umurBaru = input("Silahkan Input Umur Baru: ")
        data_detail["Umur"] = umurBaru
        print("Data Anda Sukses Diperbarui")
    elif opsi == "4":
        alamatBaru = input("Silahkan Input Alamat Baru: ")
        data_detail["Alamat"] = alamatBaru
        print("Data Anda Sukses Diperbarui")
    elif opsi == "5":
        print("==================================================")
        print("Selamat Tinggal", data_detail["Nama"])
        break
    else:
        print("Opsi Tidak Valid. Silahkan Masukkan Angka 1-5.")
