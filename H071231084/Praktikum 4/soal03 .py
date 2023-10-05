def maks(x):
    maks = x[0]
    for i in x:
        if maks < i:
            maks = i
    return maks

x = [1, 2, 4, 9, 3, 1, 9, 10]
print(maks(x))