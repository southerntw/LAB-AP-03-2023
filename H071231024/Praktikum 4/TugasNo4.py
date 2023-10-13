def catAndMouse(catA, catB, MosC):
    jarak_kucing_A = abs(catA - MosC)
    jarak_kucing_B = abs(catB - MosC)

    if jarak_kucing_B < jarak_kucing_A:
        print("Cat B")
    elif jarak_kucing_B > jarak_kucing_A:
        print("Cat A")
    else:
        print("Mouse C")


catA = int(input("\nCatA : "))
catB = int(input("CatB : "))
MosC = int(input("MouseC : "))
(catAndMouse(catA, catB, MosC))
