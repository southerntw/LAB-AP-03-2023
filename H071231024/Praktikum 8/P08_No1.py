import re


def for_in_str(str_input):
    if len(str_input) != 45:
        return False

    if not re.match(r"^[a-zA-Z0-9]*$", str_input[:40]):
        return False

    if not re.match(r"^[13579\s]*$", str_input[40:]):
        return False

    return True


str_input = input("Masukkan string: ")

if for_in_str(str_input):
    print("True")
else:
    print("False")


# 2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57
# x4202v2A22A8a6aaaaaa2G2222m222qwertyYuIo1395779
