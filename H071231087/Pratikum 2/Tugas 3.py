# menghitung total tagihan listrik 

gol = input("Golongan = " ) 
daya = int(input("Daya = " )) 
p = int(input("Pemakaian =  ")) 

match gol, daya:
    case "R1", 900:
        t = p * 1352
    case "R1", 1300:
        t = p * 1444.70
    case "R1", 2200:
        t = p * 1444.70
    case "R2", daya:
        if daya >= 3500 and daya <= 5500:
            t = p * 1699.53
    case "R3", daya:
        if daya >= 6600:
            t = p * 1699.53
    case "B2", daya:
        if daya >= 6600 and daya <= 200000:
            t = p * 1444.70
    case "B3", daya:
        if daya > 200000:
            t = p * 1114.74
    case "I3", daya:
        if daya >= 200000:
            t = p * 1314.12
    case "P1", daya:
        if daya >= 6600 and daya <= 200000:
            t = p * 1523.28
    case _:
        print("Data tidak valid!")

if t != 0:
    tagihan = f"{t:,.1f}".replace(",","x").replace(".",",").replace("x",".")
    output = f"Pemakaian = Jumlah Tagihan Anda Sebesar: Rp. {tagihan}"
    print(output)