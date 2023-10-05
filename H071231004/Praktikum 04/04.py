def CatAndMouse(CatA, CatB, MouseC):
    a = (CatA - MouseC)**2
    b = (CatB - MouseC)**2
    if a > b:
        return('Cat B')
    elif a < b:
        return('Cat A')
    else:
        return('Mouse C')
try:
    CatA = int(input('Masukkan Jarak Cat A: '))
    CatB = int(input('Masukkan Jarak Cat B: '))
    MouseC = int(input('Masukkan Jarak Mouse C: '))
    # mouse c = mouse C **2
    print(CatAndMouse(CatA, CatB, MouseC))
except ValueError:
    print('Inputan hanya berupa intejer')