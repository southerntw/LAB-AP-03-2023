def membuat_string_baru(input_str):
    lenght = len(input_str)

    if lenght < 3:
        return "Input teralu pendek, minimal 3 karakter"
    
    if lenght % 2 == 0:
        huruf_tengah1 = (lenght // 2) - 1
    
        # menemukan karakter Tengah
        huruf_tengah2 = lenght // 2
        # Ambil karakter pertama, tengah dan terakhir
        new_str = input_str[0] + input_str[huruf_tengah1] + input_str[huruf_tengah2] + input_str[-1]

    else:
        huruf_tengah2 = lenght // 2
        # Ambil karakter pertama, tengah dan terakhir
        new_str = input_str[0] + input_str[huruf_tengah2] + input_str[-1]
 

    return new_str


input_str = input("")
string_baru = membuat_string_baru(input_str)
print(string_baru)