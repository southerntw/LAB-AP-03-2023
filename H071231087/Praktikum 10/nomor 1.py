import re
import os

class Detail:
      def __init__(self):
            self.nama = None
            self.email = None
            self.password = None

      def BuatNama(self, nama):
            self.nama = nama
      def BuatEmail(self, email):
            self.email = email
      def BuatPassword(self, password):
            self.password = password
      def EditNama(self):
            self.nama = input("Masukkan Nama Baru Anda : ")

def SelamatDatang():
          print(f"{'='*50}")
          print(f"Selamat Datang! Silahkan Pilih Opsi Menu Anda")
          print(f"1. Detail Anda\n2. Ubah Nama\n3. Jumlah Data Pada File")
          print(f"4. Save Data Pada File\n5. Buat Data Baru\n6. Keluar")

def Nama():
        nama = input("Silahkan Masukkan Nama Anda : ")
        pattern_nama = re.fullmatch(r"[A-Za-z\s]*", nama)
        if pattern_nama:
               return nama
        else:
               print(f"{'='*50}")
               print("Nama yang anda masukkan salah")
               print(f"{'='*50}")
               Nama()

def Email():
       email = input("Silahkan Masukkan Email Anda : ")
       pattern_email = re.fullmatch(r"[a-z]*([0-9]{2,})?@([a-z]*\.)?([a-z]*)\.(co\.id|ac\.id|com)", email)
       if pattern_email:
               return email
       else:
               print(f"{'='*50}")
               print("email yang anda masukkan salah")
               print(f"{'='*50}")
               Email()

def Password():
      password = input("Silahkan Masukkan Password Anda : ")
      pattern_password = re.fullmatch(r"(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])[a-zA-Z0-9]{8,20}", password)
      if pattern_password:
            return password
      elif len(password) < 8 or len(password) > 20:
            print(f"{'='*50}")
            print("Panjang Password anda harus di rentang 8-20")
            print(f"{'='*50}")
            Password()
      else:
            print(f"{'='*50}")
            print("Password anda terlalu lemah!")
            print("Password harus berisi minimal 1 Huruf Besar, Kecil, dan Angka")
            print(f"{'='*50}")
            Password()
      



detail = Detail()
while True:
          SelamatDatang()
          pilihan = int(input("Silahkan Pilih Opsi Anda : "))
          match pilihan:
                  case 1:
                        print(f"{'='*50}")
                        if detail.nama == None and detail.email == None and detail.password == None:
                              print("Data Kosong!")
                        else:
                              print("Detail Anda:")
                              print(f"Nama     : {detail.nama}")
                              print(f"Email    : {detail.email}")
                              print(f"Password : {detail.password}")
                          
                  case 2:
                        print(f"{'='*50}")
                        if detail.nama == None:
                              print("Data Kosong")
                        else:
                              detail.EditNama()
                  case 3:
                        print(f"{'='*50}")
                        nama_file = input("Masukkan Nama File : ") + ".txt"
                        if os.path.exists(nama_file):
                              with open(nama_file, mode="r") as file:
                                    pattern_jumlah = re.findall(r"Nama         : ", file.read())
                                    jumlah_data = len(pattern_jumlah)
                              print(f"File Bernama {nama_file[:-4]} Ditemukan")
                              print(f"Jumlah Data file yaitu {jumlah_data}")
                        else:
                              print(f"File Bernama {nama_file[:-4]} Tidak Ditemukan")
                              print("Jumlah Data file yaitu 0")
                        
                  case 4:
                        print(f"{'='*50}")
                        if detail.nama == None and detail.email == None and detail.password == None:
                              print("Data Kosong!")
                        else:
                              nama_file = input("Masukkan Nama File : ") + ".txt"
                              if not os.path.exists(nama_file):
                                    with open(nama_file, mode="w") as file:
                                          file.write(f"+{'='*99}\n")
                                          file.write(f"|Data yang tersimpan\n")
                                          file.write(f"+{'='*99}\n")
                                    with open(nama_file, mode="a") as file:
                                          file.write(f"|Nama         : {detail.nama}\n")
                                          file.write(f"|Email        : {detail.email}\n")
                                          file.write(f"|Password     : {detail.password}\n")
                                          file.write(f"+{'='*99}\n")
                                    detail = Detail()
                              else:
                                    with open(nama_file, mode="a") as file:
                                          file.write(f"|Nama         : {detail.nama}\n")
                                          file.write(f"|Email        : {detail.email}\n")
                                          file.write(f"|Password     : {detail.password}\n")
                                          file.write(f"+{'='*99}\n")
                                    detail = Detail()
                  case 5:
                        print(f"{'='*50}")
                        nama = Nama()
                        if nama != None:
                              email = Email()
                              if email != None:
                                    password = Password()
                                    if password != None:
                                          detail.BuatNama(nama)
                                          detail.BuatEmail(email)
                                          detail.BuatPassword(password)
                                    else:
                                          password = Password()
                              else:
                                    email = Email()
                        else:
                              nama = Nama()


                  case 6:
                        print("Sampai Jumpa")
                        break