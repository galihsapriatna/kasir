keranjang = []


def tambah_barang(barang):

    for item in keranjang:

        if item["barcode"] == barang["barcode"]:

            item["qty"] += 1

            return

    keranjang.append({
        "barcode": barang["barcode"],
        "nama": barang["nama"],
        "harga": barang["harga"],
        "qty": 1
    })


def hapus_barang(barcode):

    global keranjang

    keranjang = [
        item for item in keranjang
        if item["barcode"] != barcode
    ]


def kosongkan():

    keranjang.clear()


def hitung_total():

    total = 0

    for item in keranjang:

        total += item["harga"] * item["qty"]

    return total


def jumlah_item():

    jumlah = 0

    for item in keranjang:

        jumlah += item["qty"]

    return jumlah