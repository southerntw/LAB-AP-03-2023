def ambil_huruf_tengah(string):
    if len(string) % 2 != 0:
        awal = string[0]
        tengah = string[len(string) // 2]
        akhir = string[-1]
        return awal + tengah + akhir
    else:
        return "Invalid. Kata/String Harus Ganjil"


input_string = input("\nMasukkan Kata : ")
result = ambil_huruf_tengah(input_string)

if isinstance(result, str):
    print(result)
else:
    print(result)
