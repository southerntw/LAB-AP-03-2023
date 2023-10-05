def geserhuruf (n):
    for i in range(len(n)):
        n = n[-1] + n[:-1]
        print(n, end='|')
try:
    # geserhuruf ('Mobil')

    geser = (input('Masukkan kata: '))
    geserhuruf (geser)
except ValueError:
    print('Terjadi error, n harus berupa tipe data string')
