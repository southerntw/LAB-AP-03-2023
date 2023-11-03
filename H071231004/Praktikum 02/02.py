print('Menerima TIga Inputan String')

ip = str(input('Masukkan inputan pertama: '))
id = str(input('Masukkan inputan kedua: '))
it = str(input('Masukkan inputan ketiga: '))

vi = ('vertebrado')
iv = ('invertebrado')
ac = ('ave')
mm = ('mamifero')
ie = ('inseto')
an = ('anelideo')
co = ('carnivoro')
oc = ('onivoro')
he = ('herbivoro')
ht = ('hematofago')

if ip in vi:
    if id in ac:
        if it in co:
            print('aguia')
        elif it in oc:
            print('pomba')
        else:
            print('Data tidak valid')
    elif id in mm:
        if it in oc:
            print('homem')
        elif it in he:
            print('vaca')
        else:
            print('Data tidak valid')
    else: 
        print('Data tidak valid')
if ip in iv:
    if id in ie:
        if it in ht:
            print('pulga')
        elif it in he:
            print('lagarta')
        else: 
            print('Data tidak valid')
    elif id in an:
        if it in ht:
            print('sanguessuga')
        elif it in oc:
            print('minhoca')
        else:
            print('Data tidak valid')
    else:
        print('Data tidak valid')
else:
    print('Data tidak valid')