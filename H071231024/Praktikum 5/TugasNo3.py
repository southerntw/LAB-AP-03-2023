def anagram(word1, word2):
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    if len(word1) != len(word2):
        return False

    return sorted(word1) == sorted(word2)


kata1 = input("\nMasukkan Kata Pertama: ")
kata2 = input("Masukkan Kata Kedua: ")

if anagram(kata1, kata2):
    print(True)
else:
    print(False)
