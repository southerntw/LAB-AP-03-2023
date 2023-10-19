dict = {}
print("Selamat datang, untuk memulai silahkan input data Anda!")

x = input("Input Nama: ")
dict["Nama"] = x
y = int(input("Input Umur: "))
dict["Umur"] = y
z = input("Input Alamat: ")
dict["Alamat"] = z

while True:
    print(f"""
===================================================
Selamat datang {dict["Nama"]} Silahkan pilih opsi:
===================================================
1. Detail Anda
2. Ubah Nama
3. Ubah Umur
4. Ubah Alamat
5. Keluar
===================================================""")

    opsi = int(input("Input opsi: "))
    match opsi:
        case 1:
            print(f"""===================================================
Data Anda adalah
Nama: {dict["Nama"]}
Umur: {dict["Umur"]}
Alamat: {dict["Alamat"]}""")
        case 2:
            dict["Nama"] = input("Silahkan input nama baru: ")
            print("Data Anda sukses diperbarui!")
        case 3:
            dict["Umur"] = input("Silahkan input umur baru: ")
            print("Data Anda sukses diperbarui!")
        case 4:
            dict["Alamat"] = input("Silahkan input alamat baru: ")
            print("Data Anda sukses diperbarui!")
        case 5:
            print(f"Selamat tinggal {dict['Nama']}")
            break
        case _:
            print("Inputan tidak valid")
            break