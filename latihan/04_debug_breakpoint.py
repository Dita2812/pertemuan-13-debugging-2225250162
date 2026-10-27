def rata_rata_perbaikan(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

# Pemanggil (Biar muncul di terminal)
print("--- Hasil Latihan 4 ---")
print("Data 3 item:", rata_rata_perbaikan([80, 90, 70]))
print("Data kosong:", rata_rata_perbaikan([]))