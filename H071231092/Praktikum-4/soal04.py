def catAndMouse(catA, catB, mouseC):
    distanceA = abs(catA - mouseC)
    distanceB = abs(catB - mouseC)
    
    if distanceA < distanceB:
        return "Cat A"
    elif distanceB < distanceA:
        return "Cat B"
    else:
        return "Mouse C"

# # Test Case 1
# result1 = catAndMouse(catA=16, catB=24, mouseC=17)
# print(result1)  # Output: "Cat A"

# # Test Case 2
# result2 = catAndMouse(catA=20, catB=10, mouseC=15)
# print(result2)  # Output: "Mouse C"

while True:
    try:
        catA = int(input("Jarak Kucing A : "))
        catB = int(input("Jarak Kucing B : "))
        mouseC = int(input("Jarak tikus C : "))

        hasil = catAndMouse(catA, catB, mouseC)
        print(hasil)
    except:
        break
