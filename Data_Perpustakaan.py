from Program_perpustakaan import Buku, Anggota, Perpustakaan


##LIST BUKU DI PERPUSTAKAAN
# LIST BUKU PENDIDIKAN KOMPUTER
Python = Buku("Pemrograman Python", "Ridho", "UINSUSKA", "pekanbaru", "Pendidikan Komputer", 2024)
Java = Buku("Pemrograman Java", "Dewi", "Andi Publisher", "Yogyakarta", "Pendidikan Komputer", 2020)
Robot = Buku("Kecerdasan Buatan", "Budi", "Erlangga", "Bandung", "Pendidikan Komputer", 2023)
Jaringan = Buku("Dasar-Dasar Jaringan Komputer", "Citra", "Informatika", "Yogyakarta", "Pendidikan Komputer", 2021)
BasisData = Buku("Pengantar Basis Data", "Eko", "Salemba", "Jakarta", "Pendidikan Komputer", 2019)
SistemOperasi = Buku("Sistem Operasi", "Fajar", "Deepublish", "Yogyakarta", "Pendidikan Komputer", 2022)
WebPHP = Buku("Pemrograman Web dengan PHP", "Gina", "Gramedia", "Jakarta", "Pendidikan Komputer", 2023)
MachineLearning = Buku("Machine Learning", "Hadi", "Erlangga", "Bandung", "Pendidikan Komputer", 2024)
Keamanan = Buku("Keamanan Jaringan", "Indra", "Andi Publisher", "Yogyakarta", "Pendidikan Komputer", 2021)
DataScience = Buku("Data Science dengan Python", "Joko", "Informatika", "Yogyakarta", "Pendidikan Komputer", 2024)
# LIST BUKU PENDIDIKAN KEAGAMAAN ISLAM
Fiqh = Buku("Fiqh Ibadah", "KH. Ahmad Dahlan", "Pustaka Islam", "Jakarta", "Pendidikan Keagamaan Islam", 2021)
Aqidah = Buku("Aqidah Islamiyah", "Dr. Yusuf Al-Qaradawi", "Mizan", "Bandung", "Pendidikan Keagamaan Islam", 2020)
Tafsir = Buku("Tafsir Al-Qur'an Kontemporer", "Prof. Quraish Shihab", "Lentera Hati", "Jakarta", "Pendidikan Keagamaan Islam", 2022)
Hadis = Buku("Pengantar Studi Hadis", "Dr. Musthafa Al-Bugha", "Pustaka Azzam", "Yogyakarta", "Pendidikan Keagamaan Islam", 2019)
SejarahIslam = Buku("Sejarah Peradaban Islam", "Ali Murtadha", "Pustaka Ilmu", "Surabaya", "Pendidikan Keagamaan Islam", 2023)
# LIST BUKU NOVEL
LaskarPelangi = Buku("Laskar Pelangi", "Andrea Hirata", "Bentang Pustaka", "Yogyakarta", "Novel", 2005)
Negeri5Menara = Buku("Negeri 5 Menara", "Ahmad Fuadi", "Gramedia", "Jakarta", "Novel", 2009)
AyatAyatCinta = Buku("Ayat-Ayat Cinta", "Habiburrahman El Shirazy", "Republika", "Jakarta", "Novel", 2004)
BumiManusia = Buku("Bumi Manusia", "Pramoedya Ananta Toer", "Hasta Mitra", "Jakarta", "Novel", 1980)
Hujan = Buku("Hujan", "Tere Liye", "Republika", "Jakarta", "Novel", 2016)

## LIST ANGGOTA
Daffa = Anggota("R. Daffa", "20250001")
Radish = Anggota("Radish Al Sudais", "20250002")
Ronald = Anggota("M. Ronald Albert", "20250003")
Ridho = Anggota("Ridho Utama", "20250004")
Prasetio = Anggota("Prasetio Tri Haryadi", "20250005")
Rafiq = Anggota("Muhammad Rafiq Al-Ghifari", "20250006")
Farhan = Anggota("Ahmad Farhan Rantisi", "20250007")
Musthofa = Anggota("M. Musthofa Masyhur", "20250008")
Gilang = Anggota("Gilang Rifki Pratama", "20250009")
Dimas = Anggota("Dimas Andre Prasetya", "20250010")


perpus = Perpustakaan() #variabel A = B

# Tambahkan semua buku ke dalam perpustakaan
perpus.tambah_buku(Python)
perpus.tambah_buku(Java)
perpus.tambah_buku(Robot)
perpus.tambah_buku(Jaringan)
perpus.tambah_buku(BasisData)
perpus.tambah_buku(SistemOperasi)
perpus.tambah_buku(WebPHP)
perpus.tambah_buku(MachineLearning)
perpus.tambah_buku(Keamanan)
perpus.tambah_buku(DataScience)
perpus.tambah_buku(Fiqh)
perpus.tambah_buku(Aqidah)
perpus.tambah_buku(Tafsir)
perpus.tambah_buku(Hadis)
perpus.tambah_buku(SejarahIslam)
perpus.tambah_buku(LaskarPelangi)
perpus.tambah_buku(Negeri5Menara)
perpus.tambah_buku(AyatAyatCinta)
perpus.tambah_buku(BumiManusia)
perpus.tambah_buku(Hujan)


perpus.tampilkan_buku()

Ridho.pinjam_buku(Python)
Ridho.pinjam_buku(Java)
Ridho.pinjam_buku(LaskarPelangi)

perpus.tampilkan_buku_tersedia()

Farhan.pinjam_buku(Jaringan)

Daffa.pinjam_buku(MachineLearning)

Ridho.kembalikan_buku(LaskarPelangi)

perpus.tampilkan_buku_terpinjam()