def stringPermutation(n:str): 
    try:
        for i in range(len(n)):
            n = n[-1] + n[:-1]
            print(n, end=" | ")
    except:
        print("Inputan tidak valid")

n = 5
stringPermutation(n)

n = "Mobil"
stringPermutation(n)