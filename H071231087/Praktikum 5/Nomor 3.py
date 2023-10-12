kata1 = input("Masukkan String Pertama : ").lower() #anak band
kata2 = input("Masukkan String Kedua : ").lower() # dakan ba
kata1 = kata1.replace(" ", "") # anakband
kata2 = kata2.replace(" ", "") #dakanba

x1 = []
x2 = []

for i in kata1: # i = a
          x, y = kata1.count(i), kata2.count(i)
          x1.append(x) # x1 = []
          x2.append(y)
if len(kata1) != len(kata2):
        print("False")
elif x1 == x2:
        print("True")
else:
        print("False")
