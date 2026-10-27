def status_lulus(nilai):
    if nilai > 60:
        return "Lulus"
    return "Tidak lulus"

print("--- Hasil Kasus 1 ---")
print("Nilai 75:", status_lulus(75))
print("Nilai 60:", status_lulus(60))
print("Nilai 59:", status_lulus(59))