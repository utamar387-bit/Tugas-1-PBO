class Buku:
    def __init__(self, judul, penulis, penerbit, kota, kategori, tahun):
        self.judul = judul
        self.penulis = penulis
        self.penerbit = penerbit
        self.kota = kota
        self.kategori = kategori
        self.tahun = tahun
        
        self.status = "tersedia"

    def dipinjam(self):
        self.status = "dipinjam"

    def dikembalikan(self):
        self.status = "tersedia"

class Anggota:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.daftar_pinjam = []

    def pinjam_buku(self, buku):
        print()
        if buku.status == "tersedia":
            buku.dipinjam()
            self.daftar_pinjam.append(buku)
            print(f"{self.nama} meminjam buku {buku.judul}")
        else:
            print(f"Buku {buku.judul} sedang dipinjam")

    def kembalikan_buku(self, buku):
        print()
        if buku in self.daftar_pinjam:
            buku.dikembalikan()
            self.daftar_pinjam.remove(buku)
            print(f"{self.nama} mengembalikan buku {buku.judul}")
        else:
            print("Buku tidak ada dalam daftar pinjaman")



class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, buku):
        print()
        self.daftar_buku.append(buku)
        print(f"Buku {buku.judul} telah berhasil ditambahkan")

    def hapus_buku(self, buku):
        print()  # jarak atas
        if buku not in self.daftar_buku:
            print("Buku tidak ditemukan di perpustakaan")
        elif buku.status == "dipinjam":
            print(f"Buku {buku.judul} sedang dipinjam, tidak dapat dihapus")
        else:
            self.daftar_buku.remove(buku)
            print(f"Buku {buku.judul} berhasil dihapus")


    def tampilkan_buku(self): # menampilkan buku yang terdaftar di Perpustakaan
        print()
        print("=" * 110)
        print(f"{'Judul':35} {'Penulis':25} {'Kategori':30} {'Status':10}")
        print("=" * 110)
        for buku in self.daftar_buku:
            print(f"{buku.judul:35} {buku.penulis:25} {buku.kategori:30} {buku.status:10}")
        print("=" * 110)
        print()

    def tampilkan_buku_tersedia(self): # menampilkan Buku yang lagi tersedia di perpustakaan
        print()
        print("=" * 125)
        print(" " * 49 + " DAFTAR BUKU YANG TERSEDIA " + " " * 49)
        print("=" * 125)
        print(f"{'No':<4} {'Judul':35} {'Penulis':25} {'Kategori':30} {'Tahun':6}")
        print("=" * 125)

        no = 1
        for buku in self.daftar_buku:
            if buku.status == "tersedia":
                print(f"{no:<4} {buku.judul:35} {buku.penulis:25} "
                    f"{buku.kategori:30} {buku.tahun:<6}")
                no += 1

        if no == 1:
            print("Tidak ada buku yang tersedia saat ini")

        print("=" * 125)
        print()
    
    def tampilkan_buku_terpinjam(self): # menampilkan Buku Perpustakaan yang lagi yang lagi dipinjam 
        print()
        print("=" * 125)
        print(" " * 49 + " DAFTAR BUKU YANG DIPINJAM " + " " * 49)
        print("=" * 125)
        print(f"{'No':<4} {'Judul':35} {'Penulis':25} {'Kategori':30} {'Tahun':6}")
        print("=" * 125)

        no = 1
        for buku in self.daftar_buku:
            if buku.status == "dipinjam":
                print(f"{no:<4} {buku.judul:35} {buku.penulis:25} "
                    f"{buku.kategori:30} {buku.tahun:<6}")
                no += 1

        if no == 1:
            print("Tidak ada buku yang tersedia saat ini")

        print("=" * 125)
        print()



