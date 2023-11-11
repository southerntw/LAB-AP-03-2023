import re


def IPv4(coba):
    pola = (
        r"^((\d|\d{2}|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d|\d{2}|1\d{2}|2[0-4]\d|25[0-5])$"
    )
    return re.search(pola, coba)


def IPv6(coba):
    pola = r"^([\da-f]{0,4}:){7}[\da-f]{0,4}[\da-f]{0,4}$"
    return re.search(pola, coba)


vl = int(input("Jumlah Inputan : "))

var = []
for i in range(vl):
    var.append(input(f"Masukkan Input ke {i + 1} : "))

for s in var:
    if IPv4(s):
        print("IPv4")
    elif IPv6(s):
        print("IPv6")
    else:
        print("Bukan IP Address")

# 213.214.111.564
# 1050:0:0a:0:5:600:300c:326b
# 121.203.197.20
