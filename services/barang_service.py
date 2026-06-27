import sqlite3

DB_PATH = "database/kasir.db"


def cari_barang(barcode):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT barcode, nama, harga, stok
        FROM barang
        WHERE barcode = ?
        """,
        (barcode,)
    )

    data = cursor.fetchone()

    conn.close()

    if data:

        return {
            "barcode": data[0],
            "nama": data[1],
            "harga": data[2],
            "stok": data[3]
        }

    return None


def semua_barang():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT barcode,nama,harga,stok
        FROM barang
        """
    )

    data = cursor.fetchall()

    conn.close()

    return data


def tambah_barang(barcode, nama, harga, stok):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO barang
        VALUES(?,?,?,?)
        """,
        (
            barcode,
            nama,
            harga,
            stok
        )
    )

    conn.commit()

    conn.close()


def update_barang(barcode, nama, harga, stok):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE barang
        SET
            nama=?,
            harga=?,
            stok=?
        WHERE barcode=?
        """,
        (
            nama,
            harga,
            stok,
            barcode
        )
    )

    conn.commit()

    conn.close()


def hapus_barang(barcode):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM barang
        WHERE barcode=?
        """,
        (barcode,)
    )

    conn.commit()

    conn.close()