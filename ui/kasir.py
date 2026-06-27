import customtkinter as ctk
from tkinter import ttk

from services.barang_service import cari_barang
from services.keranjang_service import (
    tambah_barang,
    keranjang,
    hitung_total,
)


class KasirApp:

    def __init__(self):

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.app = ctk.CTk()

        self.app.title("Sistem Kasir")

        self.app.geometry("1100x700")

        self.buat_tampilan()

        self.app.mainloop()

    def buat_tampilan(self):

        judul = ctk.CTkLabel(
            self.app,
            text="SISTEM KASIR",
            font=("Arial", 30, "bold")
        )

        judul.pack(pady=20)

        self.entry = ctk.CTkEntry(
            self.app,
            width=450,
            height=40,
            placeholder_text="Scan Barcode..."
        )

        self.entry.pack(pady=10)

        self.entry.bind("<Return>", lambda e: self.scan_barang())

        tombol = ctk.CTkButton(
            self.app,
            text="Scan",
            command=self.scan_barang
        )

        tombol.pack()

        # ==========================
        # TABEL
        # ==========================

        kolom = (
            "No",
            "Barcode",
            "Nama Barang",
            "Qty",
            "Harga",
            "Total"
        )

        self.tabel = ttk.Treeview(
            self.app,
            columns=kolom,
            show="headings",
            height=15
        )

        for k in kolom:
            self.tabel.heading(k, text=k)

        self.tabel.column("No", width=50, anchor="center")
        self.tabel.column("Barcode", width=180)
        self.tabel.column("Nama Barang", width=300)
        self.tabel.column("Qty", width=70, anchor="center")
        self.tabel.column("Harga", width=120, anchor="e")
        self.tabel.column("Total", width=120, anchor="e")

        self.tabel.pack(fill="both", padx=20, pady=20)

        # ==========================
        # FRAME TOTAL
        # ==========================

        bawah = ctk.CTkFrame(self.app)

        bawah.pack(fill="x", padx=20)

        self.label_total = ctk.CTkLabel(
            bawah,
            text="TOTAL BELANJA : Rp0",
            font=("Arial", 22, "bold")
        )

        self.label_total.pack(side="left", padx=20, pady=15)

        # ==========================
        # BAYAR
        # ==========================

        frame_bayar = ctk.CTkFrame(self.app)

        frame_bayar.pack(fill="x", padx=20, pady=15)

        ctk.CTkLabel(
            frame_bayar,
            text="Bayar",
            width=100
        ).pack(side="left")

        self.entry_bayar = ctk.CTkEntry(
            frame_bayar,
            width=200
        )

        self.entry_bayar.pack(side="left")

        self.entry_bayar.bind(
            "<Return>",
            lambda e: self.hitung_kembalian()
        )

        self.label_kembali = ctk.CTkLabel(
            frame_bayar,
            text="Kembalian : Rp0",
            font=("Arial",18,"bold")
        )

        self.label_kembali.pack(side="left", padx=30)

        # ==========================
        # TOMBOL
        # ==========================

        tombol_frame = ctk.CTkFrame(self.app)

        tombol_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkButton(
            tombol_frame,
            text="Bayar",
            width=120,
            command=self.bayar
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            tombol_frame,
            text="Kosongkan",
            width=120,
            command=self.kosongkan
        ).pack(side="left", padx=5)

    # ==================================

    def scan_barang(self):

        barcode = self.entry.get().strip()

        if barcode == "":
            return

        barang = cari_barang(barcode)

        if barang:

            tambah_barang(barang)

            self.refresh_tabel()

        self.entry.delete(0, "end")

    # ==================================

    def refresh_tabel(self):

        for item in self.tabel.get_children():
            self.tabel.delete(item)

        nomor = 1

        for barang in keranjang:

            total = barang["harga"] * barang["qty"]

            self.tabel.insert(
                "",
                "end",
                values=(
                    nomor,
                    barang["barcode"],
                    barang["nama"],
                    barang["qty"],
                    f"Rp {barang['harga']:,}",
                    f"Rp {total:,}"
                )
            )

            nomor += 1

        self.label_total.configure(
            text=f"TOTAL BELANJA : Rp {hitung_total():,}"
        )

    # ==================================

    def hitung_kembalian(self):

        try:

            bayar = int(self.entry_bayar.get())

            total = hitung_total()

            kembali = bayar - total

            self.label_kembali.configure(
                text=f"Kembalian : Rp {kembali:,}"
            )

        except:

            self.label_kembali.configure(
                text="Input salah"
            )

    # ==================================

    def kosongkan(self):

        keranjang.clear()

        self.refresh_tabel()

        self.entry_bayar.delete(0, "end")

        self.label_kembali.configure(
            text="Kembalian : Rp0"
        )

    # ==================================

    def bayar(self):

        self.hitung_kembalian()