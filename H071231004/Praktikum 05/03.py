# Anagram 
kata1 = input("Masukkan Kata Pertama : ") # Nen e
kata2 = input("Masukkan Kata Kedua : ") # Nan a
kata1, kata2 = kata1.replace(" ", "").lower(), kata2.replace(" ", "").lower() # Nene
list1 = []
list2 = []

for i in kata1:
    x = kata1.count(i)
    y = kata2.count(i)
    list1.append(x)
    list2.append(y)
if len(kata1) == len(kata2):
    if list2 == list1:
        print('True')
    else:
        print('False')
else:
    print('False')