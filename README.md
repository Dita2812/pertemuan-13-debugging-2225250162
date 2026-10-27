# Pertemuan 13 - Debugging, Tracing, Testing, dan Test Case

- **Nama:** Dita Amalia Veronica
- **NIM:** 2225250162
- **Kelas:** 3F
- **Mata Kuliah:** Algoritma dan Pemrograman
- **Program Studi:** S1 Pendidikan Matematika FKIP Untirta

---

## 1. Kasus#

Program ini dirancang untuk memproses data nilai mahasiswa, meliputi perhitungan rata-rata nilai, penentuan status kelulusan berdasarkan nilai batas, dan pencarian nilai tertinggi di dalam list. 

Pada versi awal, program mengalami beberapa kesalahan logika (*logical error*) dan ketidaksesuaian penanganan data yang menyebabkan hasil keluaran tidak akurat.

---

## 2. Test Case (Pengujian Awal)

Berikut adalah tabel pengujian awal pada program sebelum dilakukan perbaikan kode:

| ID | Target Fungsi | Input Data | Expected Result | Actual Result Awal | Status |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **T1** | `hitung_rata_rata` | `[80, 60, 90, 70]` | `75.0` | `75.0` | **PASS** |
| **T2** | `hitung_rata_rata` | `[100, 80]` | `90.0` | `36.0` | **FAIL** |
| **T3** | `status` | `60` | `"Lulus"` | `"Tidak lulus"` | **FAIL** |
| **T4** | `status` | `59` | `"Tidak lulus"` | `"Tidak lulus"` | **PASS** |
| **T5** | `nilai_tertinggi` | `[80, 60, 90, 70]` | `90` | `0` | **FAIL** |

---

## 3. Bug Report (Laporan Temuan Bug)

### **Bug 01: Pembagi Nilai Rata-Rata di-Hardcode (Hardcoded Divider)**
- **Gejala:** Hasil perhitungan rata-rata salah ketika jumlah data elemen list bukan 5.
- **Lokasi:** Fungsi `hitung_rata_rata()` pada `praktik/praktik_4_debugging.py`.
- **Akar Penyebab:** Pembagi diisi secara tetap (*hardcoded*) dengan angka `5`, bukan menyesuaikan dengan jumlah elemen yang sebenarnya.
- **Perbaikan:** Mengubah pembagi menjadi `len(nilai)` serta menambahkan pengecekan kondisi list kosong (`len(nilai) == 0`).

---

### **Bug 02: Logika Operator Batas Kelulusan (Boundary Bug)**
- **Gejala:** Nilai tepat `60` dinyatakan `"Tidak lulus"`, padahal syarat lulus adalah minimal `60`.
- **Lokasi:** Fungsi `status()` pada `praktik/praktik_4_debugging.py`.
- **Akar Penyebab:** Operator pembanding yang digunakan adalah `>` (lebih besar dari) bukan `>=` (lebih besar dari atau sama dengan).
- **Perbaikan:** Mengubah kondisi `if nilai > 60:` menjadi `if nilai >= 60:`.

---

### **Bug 03: Logika Pembanding dan Inisialisasi Nilai Tertinggi**
- **Gejala:** Nilai tertinggi yang dikembalikan selalu `0` atau salah.
- **Lokasi:** Fungsi `nilai_tertinggi()` pada `praktik/praktik_4_debugging.py`.
- **Akar Penyebab:** Variabel `tertinggi` diinisialisasi dengan angka `0` dan operator pembanding di dalam loop menggunakan `<` (kurang dari).
- **Perbaikan:** Menginisialisasi `tertinggi = nilai[0]` dan memperbarui kondisi perulangan menggunakan operator `>` (`if x > tertinggi:`).

---

## 4. Retest (Pengujian Ulang)

Setelah dilakukan perbaikan pada seluruh fungsi terkait, dilakukan uji ulang (*retest*) dengan hasil sebagai berikut:

| ID | Target Fungsi | Input Data | Expected Result | Actual Result Setelah Fix | Status |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **T1** | `hitung_rata_rata` | `[80, 60, 90, 70]` | `75.0` | `75.0` | **PASS** |
| **T2** | `hitung_rata_rata` | `[100, 80]` | `90.0` | `90.0` | **PASS** |
| **T3** | `status` | `60` | `"Lulus"` | `"Lulus"` | **PASS** |
| **T4** | `status` | `59` | `"Tidak lulus"` | `"Tidak lulus"` | **PASS** |
| **T5** | `nilai_tertinggi` | `[80, 60, 90, 70]` | `90` | `90` | **PASS** |

---

## 5. Cara Menjalankan Program

Buka Terminal pada direktori utama proyek, lalu jalankan perintah berikut:

```bash
# Menjalankan program praktik utama
python praktik/praktik_4_debugging.py

# Menjalankan program kasus
python kasus/kasus_01_batas_kelulusan.py
python kasus/kasus_02_rata_rata.py
python kasus/kasus_03_file_nilai.py

# Menjalankan program latihan
python latihan/01_trace_loop.py
python latihan/02_trace_fungsi.py
python latihan/03_test_case.py
python latihan/04_debug_breakpoint.py
```

---

## 6. Refleksi

Proses *debugging* berbasis hipotesis dan penggunaan *breakpoint* pada VS Code sangat membantu mengisolasi lokasi terjadinya *bug* logika tanpa perlu menebak-nebak penyebab kesalahan secara acak. Merancang *test case* nilai batas (seperti nilai `60` dan `59`) juga terbukti efektif dalam membongkar kesalahan logika yang tidak memicu *runtime error*.