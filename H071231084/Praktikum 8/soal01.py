import re

string = input("Input string: ")
pola = r"^[A-Za-z02468]{40}[13579\s]{5}$"
if re.match(pola, string):
    print("True")
else:
    print("False")