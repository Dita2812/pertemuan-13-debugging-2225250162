def hitung_diskon(total, persen):
    diskon = total * persen / 100
    return total - diskon

print("--- Hasil Latihan 2 ---")
hasil = hitung_diskon(200000, 10)
print("Total setelah diskon:", hasil)