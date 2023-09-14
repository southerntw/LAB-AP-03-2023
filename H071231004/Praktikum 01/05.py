print('Merubah Detik ke Jam:Menit:Detik')

#masukkan detik yang di mau 
detik= float(input("Masukan nilai detik ="))

#rumus mencari jam, menit, dan detik
menit= (detik%3600) //60
jam= detik / 3600
detik = detik % 60

print("%02u:%02u:%02u"%(jam,menit,detik))