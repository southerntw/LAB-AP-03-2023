def gabung_kata(s1, s2):
    s3 = ''
    len_s1 = len(s1)
    len_s2 = len(s2)
    for i in range(max(len_s1, len_s2)):
        if i < len_s1:
            s3 += s1[i]
        if i < len_s2:
            s2=s2[::-1]
            s3+=s2[i]
    return s3

s1 = input()
s2 = input()
print(gabung_kata(s1, s2))

