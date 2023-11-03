import os
import random
from datetime import datetime

garis = "=" * 100

# 1 Membuat Id Transaksi
def IDtransaksi():
    now = datetime.now()
    waktu = now.strftime("%y%m%d%H%M")
    nomor = random.randint(100, 999)
    return f'KTM{waktu}{nomor}'

# 2 Membuat File Invoice
def print_invoice(nama_kasir, semua_produk, id_transaksi):
    nama_invoice = f"{id_transaksi}.txt"
    with open(os.path.join("Invoices", nama_invoice), "w") as file:
        garis2 = "=" * 80
        baris1 = f'|{"Nama":^25}|{"Harga":^20}|{"Jumlah":^10}|{"Total":^20}|'
        waktu_transaksi = (datetime.now()).strftime("%d/%m/%y %H:%M")
        format_file = f'''
{"TOKO CACA".center(len(garis))}

{garis}
Nama Kasir: {nama_kasir}
Waktu Transaksi: {waktu_transaksi}
{garis}

{"Daftar Produk".center(len(garis))}

{garis2.center(len(garis))}
{baris1.center(len(garis))}
{garis2.center(len(garis))}
'''
        file.write(format_file)

        total_belanja = 0
        for produk in semua_produk:
            nama_produk, harga_produk, jumlah_produk = produk
            if (len(nama_produk)) > 20:
                nama_produk = nama_produk[:20] + "... "
            total_produk = harga_produk * jumlah_produk
            harga_produk = f'Rp{harga_produk}'
            total_belanja += total_produk
            total_produk = f'Rp{total_produk}'
            format_isi = f'| {nama_produk:24}|{harga_produk:>19} |{jumlah_produk:^10}|{total_produk:>19} |'
            file.write(format_isi.center(len(garis)) + "\n")
        file.write(garis2.center(len(garis)))
        total_belanja = f'Rp{total_belanja}'
        baris_total = f'|{"TOTAL":^57}|{total_belanja:>19} |'
        format_total = f'''
{baris_total.center(len(garis))}
{garis2.center(len(garis))}

{garis}
{"TERIMA KASIH TELAH BERBELANJA".center(len(garis))}
{garis}'''
        file.write(format_total)
    riwayat(id_transaksi, waktu_transaksi, total_belanja)

# Membuat Riwayat Transaksi
def riwayat(id_transaksi, waktu_transaksi, total_belanja):
    isi_ket = f'|{waktu_transaksi:^28}|{id_transaksi:^34}|{total_belanja:^34}|'
    format_ket = f"{isi_ket}\n{garis}"
    his = f'|{"RIWAYAT TRANSAKSI":^98}|'
    ket = f"|{'Waktu':^28}|{'ID Transaksi':^34}|{'Nominal Transaksi':^34}|"
    format_his = f'''{garis}
{his}
{garis}
{ket}
{garis}
'''
    if not os.path.exists("trx_history.txt"):
        with open("trx_history.txt", "w") as file:
            file.write(format_his)
            file.write(format_ket)
    else:
        with open("trx_history.txt", "a") as file:
            file.write("\n" + format_ket)

# 4 Main Program
def main():
    print(garis + "\n" + "SELAMAT DATANG".center(len(garis)) + "\n" + garis)
    nama_kasir = str(input("Masukkan nama kasir\t: "))

    while True:
        try:
            print(garis + "\nPilih opsi:\n1. Transaksi baru\n2. Cari Transaksi\n3. Keluar\n" + garis)
            opsi = int(input("Masukkan opsi pilihan\t: "))
            print(garis)
            match opsi:
                case 1:
                    semua_produk = []
                    while True:
                        id_transaksi = IDtransaksi()
                        nama_produk = input("Masukkan nama produk\t: ")
                        harga_produk = int(input("Masukkan harga produk\t: "))
                        jumlah_produk = int(input("Masukkan jumlah produk\t: "))
                        semua_produk.append((nama_produk, harga_produk, jumlah_produk))
                        print(garis)
                        tambah = input("Tambah produk? (y/t)\t: ")
                        print(garis)
                        if tambah != "y":
                            os.makedirs("Invoices", exist_ok=True)
                            print_invoice(nama_kasir, semua_produk, id_transaksi)
                            if tambah == "t":
                                print("TRANSAKSI BERHASIL".center(len(garis)))
                                break
                            else:
                                print("INPUTAN TIDAK VALID")
                                break
                case 2:
                    input_id = input("Masukkan ID Transaksi\t: ")
                    with open (os.path.join("Invoices", f'{input_id}.txt'), "r") as file:
                        baca_file = file.read()
                        garis3 = "\u2500" * 100
                        opsi_2 = garis3 + "\n" + baca_file + (2 * "\n") + garis3 
                        print(opsi_2)
                case 3:
                    opsi_3 = "SAMPAI JUMPA".center(len(garis)) + "\n" + garis
                    print(opsi_3)
                    break
                case _ :
                    print("Pilihan Opsi Tidak Tersedia")
                    break
        except ValueError:
            print(garis)
            print("Masukkan Angka yang Tepat!".center(len(garis)))

# Memanggil fungsi main
main()