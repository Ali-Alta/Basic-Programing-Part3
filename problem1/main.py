# input
student_score = 80

# Process: Your Solution Code Here
# Input nama siswa
nama_mahasiswa = input("Masukkan nama siswa: ")

# Input nilai siswa
nilai = float(input("Masukkan nilai siswa: "))

# Menentukan nilai huruf berdasarkan kriteria
if 80 <= nilai <= 100:
    nilai_huruf = "A"
    deskripsi = "Sangat Baik"
elif 65 <= nilai < 80:
    nilai_huruf = "B+"
    deskripsi = "Baik"
elif 50 <= nilai < 65:
    nilai_huruf = "B"
    deskripsi = "Cukup"
elif 35 <= nilai < 50:
    nilai_huruf = "C"
    deskripsi = "Kurang"
elif 0 <= nilai < 35:
    nilai_huruf = "D"
    deskripsi = "Sangat Kurang"
else:
    nilai_huruf = "E"
    deskripsi = "Nilai tidak valid"

# Menampilkan hasil
print(f"siswa {nama_mahasiswa} mendapatkan nilai {nilai_huruf} ({deskripsi}).")

# Output "Nilai A"
