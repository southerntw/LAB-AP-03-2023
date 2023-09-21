ip1 = str(input('Masukkan Inputan Pertama : ')).lower()
ip2 = str(input('Masukkan Inputan Kedua : ')).lower()
ip3 = str(input('Masukkan Inputan Ketiga : ')).lower()

match ip1:
    case 'vertebrado':
        if ip2 == 'ave':
            if ip3 == 'carnivoro':
                print('agula')
            elif ip3 == 'onivoro':
                print('pomba')
            else:
                print('Invalid Data')
        elif ip2 == 'mamifero':
            if ip3 == 'onivoro':
                print('homem')
            elif ip3 == 'herbivoro':
                print('vaca')
            else:
                print('Invalid Data')
        else:
            print('Invalid Data')
    case 'invertebrado':
        if ip2 == 'inseto':
            if ip3 == 'hematofago':
                print('pulga')
            elif ip3 == 'herbivoro':
                print('lagarta')
            else:
                print('Invalid Data')
        elif ip2 == 'anelideo':
            if ip3 == 'hematofago':
                print('sanguessuga')
            elif ip3 == 'onivoro':
                print('minhoca')
            else:
                print('Invalid Data')
        else:
            print('Invalid Data')
    case _:
        print('Invalid Data')
    






