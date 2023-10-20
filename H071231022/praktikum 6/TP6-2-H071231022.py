array1 = set(map(int,input("masukan array").split()))
array2 = set(map(int, input("masukan array").split()))

duplikat = array1&array2

if len(duplikat) > 1:
    print(f"terdapat {len(duplikat)} buah duplikat yaitu {tuple(duplikat)}")
elif len(duplikat) ==1:
    print("terdapat 1 buah duplikat yaitu (%d)" %(tuple(duplikat)[0]))
    
   