def terbesar(x):
          palingbesar = x[0]
          for i in x:
                  if palingbesar < i:
                          palingbesar = i
          return palingbesar


x = [1, 2, 4, 6, 9, 3, 1, 9, 10]
print(terbesar(x))
