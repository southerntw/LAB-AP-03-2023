# Dictionary
data = {
    "nama" : "",
    "umur" : "",
    "alamat" : "",
}


# Menu pilihan
def menu():
    while True:
        print()
        print("="*45)
        print(f"Selamat datang {data['nama']} silahkan pilih opsi")
        print("="*45)
        print("1. Detail Anda\n2. Ubah Nama\n3. Ubah Umur\n4. Ubah Alamat\n5. Keluar")
        print("="*45)
        pilihan = int(input("Pilihan opsi: "))
        print("="*45)

        # melihat dan mengubah data
        if pilihan == 1:
            print("Data anda adalah")
            for x in data:
                print(x,":",data[x])
            input()
        elif pilihan == 2:
            data["nama"] = input("Silahkan Input nama baru: ")
            input("Data anda sukses di diperbarui")
        elif pilihan == 3:
            data["umur"] = input("Silahkan Input umur baru: ")
            input("Data anda sukses di diperbarui")
        elif pilihan == 4:
            data["alamat"] = input("Silahkan Input alamat baru: ")
            input("Data anda sukses di diperbarui")
        elif pilihan == 5:
            print(f"Selamat tinggal {data['nama']}")
            break
        else:
            input("Tidak di opsi")


# Input Data user
print("Selamat datang untuk memulai silahkan input data anda")
data["nama"] = input("Input nama: ")
data["umur"] = input("Input umur: ")
data["alamat"] = input("Input alamat: ")
menu()
