import re
patternIPv4 = (r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[01]?[0-9][0-9]?)$")
patternIPv6 = (r"^(([A-z0-9]?[A-z0-9]?[A-z0-9]?[A-z0-9]?)\:){7}([A-z0-9]?[A-z0-9]?[A-z0-9]?[A-z0-9]?)$")
banyak      = int(input("Ingin Berapa Kali Loop? : "))
List        = []
for i in range(banyak):
    i = input("Masukkan IP : ")
    List.append(i)
for testing in List:
    if re.search(patternIPv4, testing):
        print("IPv4")
    elif re.search(patternIPv6, testing):
        print("IPv6")
    else:
        print("Bukan IP Address")
        
# 1.232.255.0
# 1-255

#00FF:9F:C:D:E:F:G:H
# A = 0 -9 / A-F