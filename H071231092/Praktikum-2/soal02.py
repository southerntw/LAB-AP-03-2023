# Input
input01 = input('Masukkan Input Pertama : ')
input02 = input('Masukkan Input Kedua : ')
input03 = input('Masukkan Input Ketiga : ')

# Conditional Statement 
match input01, input02, input03:

    case 'vertebrado','ave','carnivo':
        hasil = 'aguia'

    case 'vertebrado','ave','onivoro':
        hasil = 'pomba'
    
    case 'vertebrado','mamifero','onivoro':
        hasil = 'homem'

    case 'vertebrado','mamifero','herbivoro':
        hasil = 'vaca'

    case 'invertebrado','inseto','hematofago':
        hasil = 'pulga'

    case 'invertebrado','inseto','herbivoro':
        hasil = 'lagarta'

    case 'invertebrado','anelideo','hematofago':
        hasil = 'sanguessuga'

    case 'invertebrado','anelideo','onivoro':
        hasil = 'minhoca'
    
    case _:
        hasil = "Data tidak valid"

# Output (hasil)
print(f'{hasil}')