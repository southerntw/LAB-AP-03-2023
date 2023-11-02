import re
IPv4 = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
IPv6 = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"

n = int(input("Tentukan jumlah baris inputan: "))
output = ""
for i in range(n):
    teks = input("Masukkan teks: ")
    if re.match(IPv4, teks):
        output += "IPv4\n"
    elif re.match(IPv6, teks):
        output += "IPv6\n" 
    else:
        output += "Bukan IP Adress\n"
print(output.strip())