def baca_file_nilai(nama_file):
    try:
        with open(nama_file, 'r') as file:
            data = file.readlines()
            return [float(x.strip()) for x in data]
    except FileNotFoundError:
        print(f"Error: File '{nama_file}' tidak ditemukan.")
        return []

# Pemanggil (Biar muncul di terminal)
print("--- Hasil Kasus 3 ---")
nilai = baca_file_nilai("nilai_mahasiswa.txt")
print("Data nilai:", nilai)