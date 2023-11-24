def is_anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    return sorted(s1) == sorted(s2)

# Contoh penggunaan
s1 = 'I am Lord Voldemort'
s2 = 'Tom Marvolo Riddle'
print(is_anagram(s1, s2))  # Output: True
print(sorted(s1.replace(' ', '').lower()))