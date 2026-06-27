class Barang:

    def __init__(self, barcode, nama, harga, stok):

        self.barcode = barcode
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def __str__(self):

        return f"{self.barcode} - {self.nama}"