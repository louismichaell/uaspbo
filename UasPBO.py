from abc import ABC, abstractmethod

class IPenumpang(ABC):
    @abstractmethod
    def viewPenumpang(self):
        pass

class Penumpang(IPenumpang):
    def __init__(self, idPenumpang, nmPenumpang, noTelp):
        self.idPenumpang = idPenumpang
        self.nmPenumpang = nmPenumpang
        self.noTelp = noTelp

    def viewPenumpang(self):
        print(f"ID Penumpang   : {self.idPenumpang}")
        print(f"Nama Penumpang : {self.nmPenumpang}")
        print(f"Nomor Telepon  : {self.noTelp}")

class Tiket:
    def __init__(self):
        self.noTiket = ""
        self.asal = ""
        self.tujuan = ""
        self.kelas = ""

  
    def pilihKelas(self, kelas: str) -> str:
        self.kelas = kelas.upper()
        if self.kelas == 'B':
            return "Bisnis"
        elif self.kelas == 'E':
            return "Ekonomi"

    def viewTiket(self):
        print(f"Nomor Tiket : {self.noTiket}")
        print(f"Asal        : {self.asal}")
        print(f"Tujuan      : {self.tujuan}")
        print(f"Kelas       : {self.pilihKelas(self.kelas)}")

class Bisnis(Tiket):
    def __init__(self):
        super().__init__()
        self.fasilitasTambahan = ""

    def viewTiket(self):
        super().viewTiket()
        print(f"Fasilitas Tambahan: {self.fasilitasTambahan}")

class Ekonomi(Tiket):

    def viewTiket(self):
        super().viewTiket()
        print("Fasilitas Tambahan tidak tersedia")


def main():
    print("=" * 45)
    print("SISTEM INFORMASI RESERVASI TIKET MASKAPAI AL")
    print("=" * 45)

    idPenumpang = input("ID Penumpang: ")
    nmPenumpang = input("Nama Penumpang: ")
    noTelp = input("Nomor Telepon: ")

    tiket = Tiket()
    tiket.noTiket = input("Nomor Tiket: ")
    tiket.asal = input("Asal: ")
    tiket.tujuan = input("Tujuan: ")
    kelas = input("Kelas ([B]isnis/[E]konomi): ")
    fasilitas_tambahan = ""
    if kelas.upper() == 'B':
        fasilitas_tambahan = input("Fasilitas tambahan: ")

    penumpang = Penumpang(idPenumpang, nmPenumpang, noTelp)

    if kelas.upper() == 'B':
        tiket_bisnis = Bisnis()
        tiket_bisnis.noTiket = tiket.noTiket
        tiket_bisnis.asal = tiket.asal
        tiket_bisnis.tujuan = tiket.tujuan
        tiket_bisnis.kelas = kelas
        tiket_bisnis.fasilitasTambahan = fasilitas_tambahan
        print("\n---DATA PENUMPANG---")
        penumpang.viewPenumpang()
        print("\n---DATA TIKET---")
        tiket_bisnis.viewTiket()
    elif kelas.upper() == 'E':
        tiket_ekonomi = Ekonomi()
        tiket_ekonomi.noTiket = tiket.noTiket
        tiket_ekonomi.asal = tiket.asal
        tiket_ekonomi.tujuan = tiket.tujuan
        tiket_ekonomi.kelas = kelas
        print("\n---DATA PENUMPANG---")
        penumpang.viewPenumpang()
        print("\n---DATA TIKET---")
        tiket_ekonomi.viewTiket()
    else:
        print("Kelas Tidak Valid. Pengisian Data Tidak Dapat Dilanjutkan")

if __name__ == "__main__":
    main()
