#alsya agniatu zaha

class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.__buku = [] # Encapsulation: Data buku disembunyikan

    def tambah_buku(self, buku):
        self.__buku.append(buku)
                          
    def tampilkan_buku(self):
        for buku in self.__buku:
            print(buku.info())

    def __str__(self):
        return f"Perpustakaan: {self.nama}"

class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def info(self):
        return f"Buku: {self.judul} oleh {self.penulis}"

class BukuFiksi(Buku):
    def __init__(self, judul, penulis, genre):
        super().__init__(judul, penulis)
        self.genre = genre

    def info(self):
        return f"Buku Fiksi: {self, judul} oleh {self.penulis}, Genre: {self.genre}"
                                                                        
class BukuNonFiksi(Buku):
    def __init__(self. judul, penulis, topik):
    super().__init__(judul, penulis)
    self.topik = topik

    def info(self):
        return f"Buku Non-Fiksi: {self.judul} oleh {self.penulis}, Topik: {self.Topik}"
    
Perpustakan = Perpustakaan ("Perpustakaan Kota")

buku1 = bukuFiksi ("Harry Potter", "J.K. Rowling", "Fantasi")
buku2 = bukuNonFiksi ("Sapiens", "Yuval Noah Harari", "Sejarah")
     
perpustakaan.tambah_buku(buku1)
perpustakaan.tambah_buku(buku2)
       
print(perpustakaan)
perpustakaan.tampilkan_buku()