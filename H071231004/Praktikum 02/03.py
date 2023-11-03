print('Menghitung Total Tagihan Listrik')

g = input('Golongan = ').upper()
d = int(input('Daya = '))
p = int(input('Pemakaian = '))

match (g, d):
    case ('R1', 900):
        tagihan = 1352 * p 
    case ('R1', 1300) | ('R1', 2200):
        tagihan = 1444.7 * p
    case ('R2', _) if 3500 <= d <= 5500:
        tagihan = 1699.53 * p
    case ('R3', _) if d >= 6600:
        tagihan = 1699.53 * p
    case ('B2', _) if 6600 <= d <= 200000:
        tagihan = 1444.7 * p 
    case ('B3', _) if d >= 200000:
        tagihan = 1114.74 * p 
    case ('I3', _) if d >= 200000:
        tagihan = 1314.12 * p
    case ('P1', _) if 6600 <= d <= 200000:
        tagihan = 1523.28 * p
    case _:
        print('Data Tidak Valid')

print(f'Jumlah tagihan Anda sebesar: Rp,{tagihan:,.1f}'.replace('.', '|').replace(',', '.').replace('|', ','))