import sqlite3
import logging


class DatabaseOperations:
    def __init__(self, db_name):
        self.db_name = db_name

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def create_user(self, user):
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                sql = """INSERT INTO users (username, password_hash, email)
                                         VALUES (?, ?, ?)"""
                cursor.execute(sql, user)
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"An error occurred: {e}")
            return None

    def update_user(self, user_id, **kwargs):
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                for key, value in kwargs.items():
                    sql = f"UPDATE users SET {key}=? WHERE id=?"
                    cursor.execute(sql, (value, user_id))
                conn.commit()
                return cursor.rowcount
        except sqlite3.Error as e:
            logging.error(f"An error occurred: {e}")
            return None

    def get_user_by_id(self, user_id):
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                sql = "SELECT * FROM users WHERE id=?"
                cursor.execute(sql, (user_id,))
                conn.commit()
                return cursor.fetchone()
        except sqlite3.Error as e:
            logging.error(f"An error occurred: {e}")
            return None

    def create_task(self, task):
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                sql = """INSERT INTO tasks (title, description, status, due_date, user_id
                    VALUES (?, ?, ?, ?, ?)"""
                cursor.execute(sql, (task,))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"An error occurred: {e}")
            return None
