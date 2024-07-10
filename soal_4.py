class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

    def display_info(self):
        return f"Nama: {self.nama}, Warna: {self.warna}, Rasa: {self.rasa}"

class Mangga(Buah):
    def __init__(self, nama, warna, rasa, vitamin):
        super().__init__(nama, warna, rasa)
        self.vitamin = vitamin

    def display_info(self):
        parent_info = super().display_info()
        return f"{parent_info}, Vitamin: {self.vitamin}"

class Apel(Buah):
    def __init__(self, nama, warna, rasa, jenis):
        super().__init__(nama, warna, rasa)
        self.jenis = jenis

    def display_info(self):
        parent_info = super().display_info()
        return f"{parent_info}, Jenis: {self.jenis}"

class Jeruk(Buah):
    def __init__(self, nama, warna, rasa, asal):
        super().__init__(nama, warna, rasa)
        self.asal = asal

    def display_info(self):
        parent_info = super().display_info()
        return f"{parent_info}, Asal: {self.asal}"

buah1 = Buah("Stroberi", "Merah", "Asam")
mangga1 = Mangga("Mangga Harum Manis", "Hijau", "Manis", "Vitamin C")
apel1 = Apel("Apel Fuji", "Merah", "Manis", "Apel Jepang")
jeruk1 = Jeruk("Jeruk Bali", "Hijau", "Asam", "Indonesia")

print(buah1.display_info())
print(mangga1.display_info())
print(apel1.display_info())
print(jeruk1.display_info())
