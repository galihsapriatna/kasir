import sqlite3
from datetime import datetime

DB_PATH = "database/kasir.db"


def generate_no_transaksi():

    sekarang = datetime.now()

    return sekarang.strftime("%Y%m%d%H%M%S")


def simpan_transaksi(keranjang, total):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    no = generate_no_transaksi()

    tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS transaksi(
            no TEXT PRIMARY KEY,
            tanggal TEXT,
            total INTEGER
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS detail_transaksi(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            no TEXT,
            barcode TEXT,
            nama TEXT,
            qty INTEGER,
            harga INTEGER,
            subtotal INTEGER
        )
        """
    )

    cursor.execute(
        """
        INSERT INTO transaksi
        VALUES(?,?,?)
        """,
        (no, tanggal, total)
    )

    for item in keranjang:

        subtotal = item["harga"] * item["qty"]

        cursor.execute(
            """
            INSERT INTO detail_transaksi(
                no,
                barcode,
                nama,
                qty,
                harga,
                subtotal
            )
            VALUES(?,?,?,?,?,?)
            """,
            (
                no,
                item["barcode"],
                item["nama"],
                item["qty"],
                item["harga"],
                subtotal
            )
        )

    conn.commit()

    conn.close()

    return no