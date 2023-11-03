def CatAndMouse(CatA, CatB, MosC):
    a = abs(CatA - MosC)
    b = abs(CatB - MosC)
    if a < b:
        print("Cat A")
    elif a > b:
        print("Cat B")
    elif a == b:
        print("Mouse C")
        
CatAndMouse(CatA = 16, CatB = 24, MosC = 15)