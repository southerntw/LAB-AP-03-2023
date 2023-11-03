#Menentukan jumlah tagihan
G = str(input("Golongan = "))
D = int(input("Daya (VA) = "))
P = int(input("Pemakaian (Jam) = "))
T = 0

match G, D:
    case "R1", 900:
        T = P * 1352
    case "R1", 1300:
        T = P * 1444.70
    case "R1", 2200:
        T = P * 1444.70
    case "R1", 2200:
        T = P * 1444.70
    case "R2", D:
        if 3.500 <= D <= 5.500:
            T = P * 1699.53
        else:
            print("Data tidak valid")
    case "R3", D:
        if D >= 6600:
            T = P * 1699.53
        else:
            print("Data tidak valid")
    case "B2", D:
        if 6600 <= D <= 200000:
            T = P * 1444.70
        else:
            print("data tidak valid")
    case "B3", D:
        if D > 200000:
            T = P * 1114.74
        else:
            print("data tidak valid")
    case "I3", D:
        if D >= 200000:
            T = P * 1314.12
        else:
            print("data tidak valid")
    case "P1", D:
        if 6600 <= D <= 200000:
            T = P * 1523.28
        else:
            print("data tidak valid")
    case _ :
        print("data tidak valid")

if T != 0:
    tagihan = f"{T:,.1f}".replace(",", "x").replace(".",",").replace("x", ".")
    output = f"Pemakaian = Jumlah tagihan Anda sebesar: Rp. {tagihan}"
    print(output)