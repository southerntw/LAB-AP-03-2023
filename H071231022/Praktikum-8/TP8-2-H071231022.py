import re

def cek_IPaddress(address):
    IPv4_Address = r"^(\d{1,3}\.){3}\d{1,3}$"
    IPv6_Address = r"^(\d|([0-9a-fA-F]{1,4}:)){7}(\d|[0-9a-fA-F]{1,4})$"
    if re.match(IPv4_Address, address):
        return "IPv4"
    elif re.match(IPv6_Address, address):
        return "IPv6"
    else:
        return "Bukan IPv4 and IPv6"

address = input("Masukkan alamat IP: ")
hasil = cek_IPaddress(address)
print(hasil)

# 999.255.12.123 1-255
# P:Q:R:S:T:U:V:W 0-9 A-F a-f
# AA12:11FF:92FA: