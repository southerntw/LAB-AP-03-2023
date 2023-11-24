import re
pola = r"^[A-Za-z02468]{40}[13579\s]{5}$"
kata = input()
print(bool(re.match(pola,kata)))