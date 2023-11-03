import re

def cek_nama_pengguna(nama):
    pettes = r"^(?=.*[a-zA-Z0-9])[a-zA-Z0-9]{5,20}$"
    return re.match(pettes, nama) is not None
    # username
def cek_email(email):
    pettes = r"^[a-z]+[0-9]{2,}@[a-z]+\.(com|co\.id)$"
    return re.match(pettes, email) is not None
    # username234@gmail.co.id
def cek_password(password):
    pettes = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z0-9]{8,}$"
    return re.match(pettes, password) is not None
    # UserUame123

nama = input("Masukkan Nama: ")
if cek_nama_pengguna(nama): 
    email = input("masukkan email anda : ")
    if cek_email(email) :
        password = input ("masukkan password : ")
        if cek_password(password) :
            print (f"Registrasi berhasil! Selamat datang {nama}")
        else : 
            print ("password yang anda masukkan tidak valid")
    else :
        print("email yang anda masukkan tidak valid")
else : 
    print("Username yang anda masukkan tidak valid")