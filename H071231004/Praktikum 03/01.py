n = int(input('Masukkan niali N: '))
if n <= 0: 
    print('bukan fibonacci')
else: 
    s1 = 0 
    s2 = 1 
    print(s1, s2, end=" ") #end itu agar outputnya ke kanan tidak membuat line baru
    for i in range(n - 2): #perulangan index ke 2 sampai ke n 
        s3 = s1 + s2
        s, s2 = s2, s3
        print(s3, end=" ")