class Mobil:
    def __init__(self, id_mobil, merk, model, tahun, biaya_sewa):
        self.id_mobil = id_mobil
        self.merk = merk
        self.model = model
        self.tahun = tahun
        self.biaya_sewa = biaya_sewa
        self.is_available = True

    def display_info(self):
        return f"{self.merk} {self.model} ({self.tahun}) - Biaya Sewa: {self.biaya_sewa} per hari"

class RentalMobil:
    def __init__(self):
        self.mobil_list = []

    def tambah_mobil(self, mobil):
        self.mobil_list.append(mobil)

    def lihat_mobil_tersedia(self):
        mobil_tersedia = [mobil for mobil in self.mobil_list if mobil.is_available]
        if not mobil_tersedia:
            return "Tidak ada mobil tersedia."
        return "\n".join([mobil.display_info() for mobil in mobil_tersedia])

    def sewa_mobil(self, id_mobil, jumlah_hari):
        mobil = next((mobil for mobil in self.mobil_list if mobil.id_mobil == id_mobil), None)
        if mobil and mobil.is_available:
            total_biaya = mobil.biaya_sewa * jumlah_hari
            mobil.is_available = False
            return f"Mobil {mobil.merk} {mobil.model} berhasil disewa selama {jumlah_hari} hari. Total biaya: {total_biaya}"
        elif not mobil:
            return "Mobil tidak ditemukan."
        else:
            return "Mobil sudah tidak tersedia."

# Contoh penggunaan
mobil1 = Mobil(1, 'Toyota', 'Camry', 2022, 200000)
mobil2 = Mobil(2, 'Honda', 'Accord', 2021, 180000)
mobil3 = Mobil(3, 'Ford', 'Mustang', 2020, 250000)
mobil4 = Mobil(4, 'Chevrolet', 'Camaro', 2021, 220000)
mobil5 = Mobil(5, 'Tesla', 'Model S', 2022, 300000)

rental = RentalMobil()
rental.tambah_mobil(mobil1)
rental.tambah_mobil(mobil2)
rental.tambah_mobil(mobil3)
rental.tambah_mobil(mobil4)
rental.tambah_mobil(mobil5)

print("Mobil yang Tersedia:")
print(rental.lihat_mobil_tersedia())

id_mobil_sewa = 2
jumlah_hari_sewa = 3
pesan_sewa = rental.sewa_mobil(id_mobil_sewa, jumlah_hari_sewa)
print(pesan_sewa)

print("\nMobil yang Tersedia Setelah Disewa:")
print(rental.lihat_mobil_tersedia())
