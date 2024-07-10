def tambah_data_mahasiswa(data_mahasiswa):
    while True:
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        data_mahasiswa.append({"nim": nim, "nama": nama})
        
        tambah_lagi = input("Ingin tambah lagi? (ya/tidak): ").lower()
        if tambah_lagi != 'ya':
            break

def tampilkan_data_mahasiswa(data_mahasiswa):
    print("Data Mahasiswa:")
    for mahasiswa in data_mahasiswa:
        print(f"NIM: {mahasiswa['nim']}, Nama: {mahasiswa['nama']}")

if __name__ == "__main__":
    data_mahasiswa = []
    tambah_data_mahasiswa(data_mahasiswa)
    tampilkan_data_mahasiswa(data_mahasiswa)
