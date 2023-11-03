import os
import datetime
import random

def awal_trx_history():
    '''MEMBUAT JUDUL ATAU KEPALA DARI HISTORI TRANSAKSI'''
    with open(trx_history, mode="a") as history:
        history.write(f"{'='*70}\n|{'RIWAYAT TRANSAKSI'.center(68)}|\n{'='*70}\n")
        history.write(f"|{'Waktu'.center(16)}|{'ID Transaksi'.center(25)}|{'Nominal Transaksi'.center(25)}|\n{'='*70}\n")
        
def isi_trx_history():
    '''MEMBUAT ISI ATAU BAGIAN DARI HISTORI TRANSAKSI'''
    global total_keseluruhan #Global : Berguna untuk dapat mengambil variabel yang dari luar, dan dipanggil kedalam tanpa menjadikannya parameter
    waktu_struk = datetime.datetime.now()
    total_keseluruhan = "Rp" + str(total_keseluruhan)
    with open(trx_history, mode="a") as isi:
        isi.write(f"|{waktu_struk.strftime('%y/%m/%d %H:%M').center(16)}|{id_transaksi.ljust(25)}|{total_keseluruhan.center(25)}|\n{'='*70}\n")
        
def opsi():
    '''OPSI'''
    print(f"{'='*70}\nPilih opsi:\n1. Transaksi baru\n2. Cari transaksi\n3. Keluar\n{'='*70}")

def awal_struk(FileStruk, NamaKasir, tampung):
    '''DISINI MERUPAKAN AWAL STRUK ATAU KEPALA STRUKNYA'''
    global total_keseluruhan
    waktu_kasir = datetime.datetime.now()
    with open(FileStruk, mode="a") as struk:
        struk.write(f"\n{'TOKO BERKAH DUNIA AKHIRAT'.center(70)}\n\n")
        struk.write(f'{"="*70}\n')
        struk.write(f"Nama kasir      : {NamaKasir}\n")
        struk.write(f"Waktu transaksi : {waktu_kasir.strftime('%y/%m/%d %H:%M')}\n")
        struk.write(f'{"="*70}\n')
        struk.write(f"\n{'Daftar Produk'.center(70)}\n\n")
        struk.write(f"{('='*60).center(70)}\n")
        struk.write(f"|{'Nama'.center(14)}|{'Harga'.center(14)}|{'Jumlah'.center(13)}|{'Total'.center(14)}|".center(70))
        struk.write(f"\n{('='*60).center(70)}\n")

        for barang in tampung:
            total_perbarang = barang['Harga'] * barang['Jumlah']
            total_keseluruhan += total_perbarang
            if len(barang['Produk']) > 14:
                barang['Produk'] = barang['Produk'][:11] + "..."
            struk.write(f"|{str(barang['Produk']).ljust(14)}|{('Rp' +str(barang['Harga'])).rjust(14)}|{str(barang['Jumlah']).center(13)}|{('Rp' + str(total_perbarang)).rjust(14)}|".center(70) + "\n") 
            # struk.write("\n")
        struk.write(f"{('='*60).center(70)}\n")
        struk.write(f"|{'TOTAL'.center(43)}|{('Rp' + str(total_keseluruhan)).rjust(14)}|".center(70))
        struk.write(f"\n{('='*60).center(70)}\n\n")
        struk.write(f'{"="*70}\n')
        struk.write(f"{'TERIMA KASIH TELAH BERBELANJA'.center(70)}")
        struk.write(f'\n{"="*70}\n')
    return total_keseluruhan

waktu            = datetime.datetime.now()
trx_history      = "trx_history.txt"
folder_invoice   = "Invoice"
print(f'{"="*70}\n{"SELAMAT DATANG".center(70)}\n{"="*70}')
kasir       = input("Masukkan nama kasir : ").title()
## Inisial Nama 
inisial = ""
x       = kasir.split()

for i in x:
    inisial += i[0]
tampung_barang = []

while True:
    opsi()
    pilihan = int(input("Masukkan opsi pilihan  : "))
    match pilihan:
        case 1:
            total_keseluruhan = 0   
            while True:
                print("="*70)
                one_item = {
                    'Produk' : input("Masukkan nama produk   : "),
                    'Harga' : int(input("Masukkan harga produk  : ")),
                    'Jumlah' : int(input("Masukkan jumlah produk : "))
                }
                tampung_barang.append(one_item)
                print("="*70)
                lanjut = input("Tambah produk? (y/t)   : ")
                if lanjut == "y":
                    continue
                else:
                    id_transaksi    = f"{inisial}{waktu.strftime('%y%m%d%H%M')}{random.randint(100, 999)}"
                    print(f"{'='*70}\n{'TRANSAKSI BERHASIL'.center(70)}")
                    if not os.path.exists(folder_invoice):
                        os.mkdir(folder_invoice)
                    if not os.path.exists(trx_history):
                        awal_trx_history()
                    file_struk = os.path.join(folder_invoice, f"{id_transaksi}.txt")
                    total_keseluruhan += awal_struk(file_struk, kasir, tampung_barang)
                    tampung_barang.clear()
                    isi_trx_history()
                    break
        case 2:
            print(f"{'='*70}")
            cari = input("Masukkan ID transaksi  : ")
            pathfolder = folder_invoice + "/" + cari + ".txt"
            with open(pathfolder, mode="r") as cari:
                print(cari.read())
        case 3:
            print(f"{'='*70}\n{'SAMPAI JUMPA'.center(70)}\n{'='*70}")
            break