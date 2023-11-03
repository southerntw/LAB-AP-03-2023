kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

kata1 = kata1.lower().replace(" ", "")
kata2 = kata2.lower().replace(" ", "")

list_kata1 = sorted(kata1)
list_kata2 = sorted(kata2)

anagram = list_kata1 == list_kata2

print(anagram)