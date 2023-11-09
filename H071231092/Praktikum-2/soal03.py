# Input Golongan, Daya, dan Pemakaian
golongan = input("Golongan = ")
daya = int(input("Daya = "))
pemakaian = int(input("Pemakaian = "))

# Conditional Statement Golongan dan daya
if golongan == 'R1':
    if daya == 900:
        tarif = 1352
    elif daya == 1300 or daya == 2200:
        tarif = 1444.70
    else:
        print("Data tidak valid")
elif golongan == 'R2':
    if daya >= 3500 and daya <= 5500:
        tarif = 1699.53
    else:
        print("Data tidak valid")
elif golongan == 'R3':
    if daya >= 6600:
        tarif = 1699.53
    else:
        print("Data tidak valid")
elif golongan == 'B2':
    if daya >= 6600 and daya <= 200000:
        tarif = 1444.70
    else:
        print("Data tidak valid")
elif golongan == 'B3':
    if daya > 200000:
        tarif = 1114.74
    else:
        print("Data tidak valid")
elif golongan == 'I3':
    if daya >= 200000:
        tarif = 1314.12
    else:
        print("Data tidak valid")
elif golongan == 'P1':
    if daya >= 6600 and daya <= 200000:
        tarif = 1523.28
    else:
        print("Data tidak valid")
else:
    print("Tidak ada golongannya")

# Rumus tagihan
tagihan = pemakaian*tarif

# Output(Hasil)
print(f'pemakaian = Jumlah tagihan anda sebesar : Rp, {tagihan:,.2f}'.replace('.', 'x').replace(',', '.').replace('x', ','))