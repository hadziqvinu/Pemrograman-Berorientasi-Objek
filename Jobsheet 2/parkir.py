

class Motor:
    def __init__(self, plat_nomor, jam_masuk):
        self.plat_nomor = plat_nomor
        self.jam_masuk = jam_masuk
        self.tarif_per_jam = 2000
        self.status = "Parkir"

    def tampilkan_detail(self):
        print(f"--- Detail Parkir ---")
        print(f"Plat Nomor : {self.plat_nomor}")
        print(f"Jam Masuk  : {self.jam_masuk}:00")
        print(f"Status     : {self.status}")
        print("-" * 20)

    def hitung_biaya(self, jam_keluar):
        durasi = jam_keluar - self.jam_masuk
        
        if durasi <= 0:
            durasi = 1 # Minimal bayar 1 jam
            
        total_bayar = durasi * self.tarif_per_jam
        self.status = "Selesai"
        
        return durasi, total_bayar