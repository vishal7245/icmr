import sqlite3

def insert_data(db_path, lab_data):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Insert data
    cursor.executemany('''INSERT INTO Labs(CountryCode, LaboratoryCode, FileName, LabName)
                        VALUES(?, ?, ?, ?)''', lab_data)

    conn.commit()
    conn.close()

def print_data(db_path):
    items = []
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Retrieve data
    cursor.execute('''SELECT * FROM Labs''')
    data = cursor.fetchall()

    # Print data
    for row in data:
        print(row)

    conn.close()

def main():
    db_path = "init_db.sqlite"

    # Sample data
    lab_data = [
        ("USA", "L01", "file1.yaml", "Lab 1"),
        ("UK ", "L02", "file2.yaml", "Lab 2"),
        ("FRA", "L03", "file3.yaml", "Lab 3")
        # Add more data as needed
    ]

    # Insert data into the table
    print_data(db_path)

if __name__ == "__main__":
    main()