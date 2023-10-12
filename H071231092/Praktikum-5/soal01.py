def campur_string(s1, s2):
    s3 = ''
    min_len = min(len(s1), len(s2))
    
    for i in range(min_len):
        s3 += s1[i] + s2[-(i+1)]

    if len(s1) > len(s2):
        s3 += s1[min_len:]
    else:
        s3 += s2[min_len:]

    return s3

s1 = 'Abcdefg'
s2 = 'Xyz'
hasil = campur_string(s1, s2)
print(hasil)