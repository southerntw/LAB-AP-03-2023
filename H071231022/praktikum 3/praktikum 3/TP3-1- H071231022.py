n = int(input())

x,y = 0,1 #dua anggota pertama dari deret fibonacci selalu 0 dan 1

for i in range(n):
    print(x, end=" ")
    z = x + y
    x = y #nanti nilai x itu akan berubah dengan nilai y
    y = z #kalau sdh ada suku z nanti y akan berubah nilai nya