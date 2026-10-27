def status_lulus_fix(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"

# Pemanggil (Biar muncul di terminal)
print("--- Hasil Latihan 3 ---")
test_inputs = [59, 60, 61]
for val in test_inputs:
    print(f"Input: {val} -> Result: {status_lulus_fix(val)}")