import re
# Meminta mau berapa ip yang di cek
banyak_ip = int(input("Input berapa IP Address yang ingin di cek : "))
list_ip = []
for i in range (banyak_ip) :
    ip_cek = input()
    list_ip.append(ip_cek)

for i in range(len(list_ip)):
    if len(list_ip[i]) <= 500:
        # print(len(list_ip[i]))
        ipv4 = re.match(r'^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}$',list_ip[i])
        ipv6 = re.match(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$',list_ip[i])
        if ipv4:
            print('IPv4')
        elif ipv6:
            print('IPv6')
        else:
            print('Bukan IP Address')

# This line has trailing whitespace
# 121.203.197.20
# 2001:0db8:0000:0000:0000:ff00:0042:8329