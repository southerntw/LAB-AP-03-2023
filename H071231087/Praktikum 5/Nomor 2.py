kata = input("Masukkan String : ")
if len(kata) % 2 != 0: #Ganjil
          m = kata[0] + kata[len(kata)//2] + kata[-1]
          print(m)
else: #Genap, kenapa ada kondisi genap? Misal Jamese apakah dia ambil huruf tengahnya satu saja atau dua?
        m = kata[0] + kata[len(kata)//2-1] + kata[len(kata)//2]+ kata[-1]
        print(m)