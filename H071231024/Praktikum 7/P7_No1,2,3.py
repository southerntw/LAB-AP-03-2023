import os
import random
import datetime


# Fungsi untuk mengambil inisial dari nama
def inisial_nama(nama_kasir):
    nama_pisah = nama_kasir.split()
    inisial = ""
    for kata in nama_pisah:
        inisial += kata[0].upper()
    return inisial


# Fungsi untuk membuat ID transaksi
def buat_idTR(nama):
    s = datetime.datetime.now()
    inisial = inisial_nama(nama)
    tahun = s.strftime("%y")
    bulan = s.strftime("%m")
    tanggal = s.strftime("%d")
    waktu = s.strftime("%H%M%S")
    randomn = str(random.randint(100, 999))

    idtr = f"{inisial}{tahun}{bulan}{tanggal}{waktu}{randomn}"
    return idtr


# Fungsi untuk menampilkan riwayat transaksi
def tampilkan_riwayat_transaksi():
    try:
        with open("trx_history.txt", "r") as file_riwayat:
            isi_riwayat = file_riwayat.read()
            print("Riwayat Transaksi:")
            print(isi_riwayat)
    except FileNotFoundError:
        print("Belum ada riwayat transaksi.")


def tabel():
    transaksi = []  # Daftar transaksi

    while True:
        np = input("Masukkan Nama Produk         : ")
        hp = int(input("Masukkan Harga Barang        : "))
        jp = int(input("Masukkan Jumlah Barang       : "))

        total = hp * jp
        transaksi.append((np, hp, jp, total))

        tambah = input("Tambah Produk ? (y/t)        : ")
        if tambah == "y":
            continue
        elif tambah == "t":
            if not os.path.exists("invoices"):
                os.mkdir("invoices")

            idtr = buat_idTR(nama_kasir)
            nama_file = f"invoices/{idtr}.txt"
            s = datetime.datetime.now()
            tahun = s.strftime("%d/%m/%y")
            jam = s.strftime("%H:%M")

            totalsp = sum(i[3] for i in transaksi)
            waktu = f"{tahun} {jam}"

            with open(nama_file, "w") as file_invoice:
                file_invoice.write(f"\n\n{'TOKO ILHAM'.center(74)}\n\n")
                file_invoice.write(f"{'='*75}\n")
                file_invoice.write(f"Nama Kasir      : {nama_kasir}\n")
                file_invoice.write(f"Waktu Transaksi : {tahun} {jam}\n")
                file_invoice.write(f"{'='*75}\n")
                file_invoice.write(f"\n{'DAFTAR PRODUK'.center(76)}\n\n")
                file_invoice.write(f"{(65*'=').center(75)}\n")
                file_invoice.write(
                    f"{' '*5}| {'Nama'.center(17)} | {'Harga'.center(14)} | {'Jumlah'.center(7)} | {'Total'.center(14)} | {' '*5}\n"
                )

                file_invoice.write(f"{(65*'=').center(75)}\n")

                for p, h, j, t in transaksi:
                    if len(p) > 15:
                        p = p[:12] + "..."

                    file_invoice.write(
                        f"{' '*5}| {p.ljust(17)} | {('Rp.'+ str(h)).center(14)} | {str(j).center(7)} | {('Rp.'+ str(t)).center(14)} | {' '*5}\n"
                    )

                file_invoice.write(f"{(65*'=').center(75)}\n")

                file_invoice.write(
                    f"{' '*5}| {'TOTAL'.center(17)} \t\t\t\t\t  | {('Rp.' + str(totalsp)).center(14)} | {' '*5}\n"
                )
                file_invoice.write(f"{(65*'=').center(75)}\n")
                file_invoice.write(f"\n{'='*75}\n")
                file_invoice.write("TERIMA KASIH TELAH BERBELANJA".center(75))
                file_invoice.write(f"\n{'='*75}\n")

                nama_file = idtr

                file = "trx_history.txt"
                if not os.path.exists(file):
                    file2 = open(file, "w")
                    file2.write(
                        f"{'='*70}\n| {'DAFTAR TRANSAKSI'.center(66)} |\n{'='*70} \n"
                    )
                    file2.write(
                        f"| {'Waktu'.center(17)} | {'ID Transaksi'.center(20)} | {'Nominal Transaksi'.center(23)} |\n{'='*70}\n"
                    )
                    file2.close()
                file2 = open(file, "a")
                file2.write(
                    f"| {waktu.center(17)} | {nama_file.center(20)} | {('Rp.'+str(totalsp)).center(23)} |\n{'='*70}\n"
                )
                file2.close()

            print(75 * "=")
            print("TRANSAKSI BERHASIL".center(75))
            print(75 * "=")
            break

        return nama_file


print(75 * "=")
print("SELAMAT DATANG".center(75))
print(75 * "=")
nama_kasir = input("Masukkan Nama Kasir          : ")
print(75 * "=")
while True:
    print("Pilih Opsi : ")
    print("1. Transaksi Baru")
    print("2. Cari Transaksi")
    print("3. Keluar")
    print(75 * "=")

    pilihan = input("Masukkan Opsi Pilihan        : ")
    print(75 * "=")

    if pilihan == "1":
        print(tabel())

    elif pilihan == "2":
        cari = input("Masukkan ID Transaksi : ")
        print("=" * 75)
        folder_p = "invoices"
        file_read = f"{folder_p}/{cari}.txt"
        if not os.path.exists(file_read):
            print(f"File ID {cari} tidak ditemukan")
            print("=" * 75)
        else:
            with open(file_read, "r") as read:
                print(read.read())
            print("=" * 75)

    elif pilihan == "3":
        print(f"SAMPAI JUMPA {nama_kasir}".center(75))
        print(75 * "=")
        break
