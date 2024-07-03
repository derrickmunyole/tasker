# Python function to create SQLite tables for users and tasks with foreign key constraint.
import sqlite3
import logging
from connection import create_connection


def create_tables(conn):
    create_users_table = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            email TEXT
        );
        """
    create_tasks_table = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT,
            due_date TEXT,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users (id)
        );
        """
    try:
        c = conn.cursor()
        c.execute(create_users_table)
        c.execute(create_tasks_table)
    except sqlite3.Error as e:
        logging.error("Error while creating table", e)
