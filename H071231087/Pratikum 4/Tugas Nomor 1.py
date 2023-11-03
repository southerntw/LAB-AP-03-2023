def stringPermutation(x):
          for i in range(len(x)):   
                  xbaru = x[-1] + x[:-1]
                  print(xbaru, end=" | ")
                  x = xbaru   
try:
      stringPermutation("Mobil")
except:
      print("Eror")