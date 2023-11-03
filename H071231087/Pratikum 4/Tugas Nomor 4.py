def CatAndMouse(CatA, CatB, MouseC):
          A = ((CatA - MouseC)**2)**0.5
          B = ((CatB - MouseC)**2)**0.5
          if A > B:
                  print("Cat B")
          elif A < B:
                  print("Cat A")
          else:
                  print("Mouse C")

CatAndMouse(CatA=16, CatB=24, MouseC=15)