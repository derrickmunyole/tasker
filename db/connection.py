import sqlite3
import logging


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        logging.error("Error while connecting to sqlite", e)
        return None
