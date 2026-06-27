class Transaksi:

    def __init__(self, no, tanggal, total):

        self.no = no
        self.tanggal = tanggal
        self.total = total

    def __str__(self):

        return f"{self.no} | {self.tanggal} | {self.total}"