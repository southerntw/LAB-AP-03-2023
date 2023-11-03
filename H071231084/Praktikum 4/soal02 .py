def palindrom(x):
    if x.lower() == x[::-1].lower():
        print("Palindrom")
    else:
        print("Bukan Palindrom")

x = str(input())
palindrom(x)