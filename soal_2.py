mahasiswa = ["mahasiswa_1", "mahasiswa_2", "mahasiswa_3"]
algoritma_dan_struktur_data_2 = [90, 50, 65]
matematika_numerik = [80, 60, 70]

rata_rata_algoritma = sum(algoritma_dan_struktur_data_2) / len(algoritma_dan_struktur_data_2)
rata_rata_matematika = sum(matematika_numerik) / len(matematika_numerik)

print("Rata-rata nilai untuk setiap mata kuliah:")
print(f"Algoritma dan Struktur Data 2: {rata_rata_algoritma:.2f}")
print(f"Matematika Numerik: {rata_rata_matematika:.2f}")

print("Rata-rata nilai untuk setiap mahasiswa:")
for i in range(len(mahasiswa)):
    rata_rata_mahasiswa = (algoritma_dan_struktur_data_2[i] + matematika_numerik[i]) / 2
    print(f"{mahasiswa[i]}: {rata_rata_mahasiswa:.2f}")
