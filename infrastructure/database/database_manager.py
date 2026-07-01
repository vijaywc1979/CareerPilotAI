import sqlite3
from pathlib import Path


class DatabaseManager:

    def __init__(self):

        db_path = Path("database/careerpilot.db")

        self.connection = sqlite3.connect(db_path)

        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS resume_profile(

            id INTEGER PRIMARY KEY,

            name TEXT,

            email TEXT,

            phone TEXT,

            designation TEXT,

            experience INTEGER,

            summary TEXT
        )
        """)

        self.connection.commit()

    def execute(self, query, params=()):

        self.cursor.execute(query, params)

        self.connection.commit()

    def fetchone(self, query, params=()):

        self.cursor.execute(query, params)

        return self.cursor.fetchone()

    def close(self):

        self.connection.close()