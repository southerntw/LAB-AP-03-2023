def palindrom(kata: str) -> str:
    kata = kata.lower().replace(" ","")

    if (kata == kata[::-1]):
        return "Palindrom"
    else:
        return "Bukan palindrom"
    
kata = input("Kata : ")
hasil = palindrom(kata)
print(f'palindrom ("{kata}")')
print(hasil)

