import sqlite3

DB_PATH = "database/kasir.db"


def get_connection():

    return sqlite3.connect(DB_PATH)