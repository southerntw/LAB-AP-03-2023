golongan = input("Golongan = ")
daya = int(input("Daya = "))
pemakaian = int(input("Pemakaian = "))
tagihan = None

match (golongan, daya):
    case ("R1", 900):
        tagihan = 1352 * pemakaian
    case ("R1", 1300):
        tagihan = 1444.7 * pemakaian
    case ("R1", 2200):
        tagihan = 1444.7 * pemakaian
    case ("R2", _) if 3500 <= daya <= 5500:
        tagihan = 1699.53 * pemakaian 
    case ("R3", _) if daya >= 6600:
        tagihan = 1699.53 * pemakaian 
    case ("B2", _) if 6600 <= daya <= 200000:
        tagihan = 1444.7 * pemakaian
    case ("B3", _) if daya > 200000:
        tagihan = 1114.74 * pemakaian
    case ("I3", _) if daya >= 200000:
        tagihan = 1314.12 * pemakaian
    case ("P1", _) if 6600 <= daya <= 200000:
        tagihan = 1523.28 * pemakaian 
    case _:
        print("data tidak valid")

if tagihan is not None:
    print(f"Jumlah tagihan Anda sebesar: Rp, {tagihan:,.1f}".replace('.', '|').replace(',', '.').replace('|', ','))