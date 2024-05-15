import os
import sqlite3


def create_init_database():
    db_path = "data/init_db.sqlite"
    db_dir = os.path.dirname(db_path)  # Get directory path

    if not os.path.exists(db_dir):
        os.makedirs(db_dir)  # Create directory if it doesn't exist

    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS Labs
                        (CountryCode CHAR(3),
                        LaboratoryCode CHAR(3),
                        FileName TEXT,
                        LabName TEXT,
                        PRIMARY KEY (CountryCode, LaboratoryCode))''')

        conn.commit()
        conn.close()
        print("Database created successfully.")
    else:
        print("Database already exists.")

