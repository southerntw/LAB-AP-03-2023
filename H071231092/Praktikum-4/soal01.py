# membuat fungsi
def nilaiPermutasi(kata:str):
    try:
        permutasi = ' '
        for i in range(len(kata)):
            berputar_kata = kata[-1] + kata[:-1]
            permutasi = permutasi + berputar_kata + ' | '
            kata = berputar_kata

        return permutasi
    
    except:
        x = "Data bukan merupakan string"
        return x
    


# Input kata
hasil1 = nilaiPermutasi(10)
hasil2 = nilaiPermutasi('ayam')
print(hasil1)
print(hasil2)