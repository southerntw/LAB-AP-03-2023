def anagram(kata1, kata2):
    # Menghilangkan spasi da mengubah menjadi huruf kecil
    kata1 = kata1.replace(" ", "").lower() # nana
    kata2 = kata2.replace(" ", "").lower() # nene

    for karakter in kata1:
        hasil1 = kata1.count(karakter)
        hasil2 = kata2.count(karakter)

        if hasil1 == hasil2:
            continue
        else:
            return False
            break
        
    else:
        return True


kata1 = input("")
kata2 = input("")
hasil = anagram(kata1, kata2)
print(hasil)
