import sqlite3

class Database:
    def __init__(self, db_name="health_records.db"):
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """Create table if it doesn't exist"""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                symptoms TEXT
            )
        """)
        self.connection.commit()

    def insert_record(self, name, age, symptoms):
        """Insert a new record"""
        self.cursor.execute("""
            INSERT INTO records (name, age, symptoms)
            VALUES (?, ?, ?)
        """, (name, age, symptoms))
        self.connection.commit()

    def fetch_records(self):
        """Retrieve all records"""
        self.cursor.execute("SELECT * FROM records")
        return self.cursor.fetchall()

    def close(self):
        """Close the database connection"""
        self.connection.close()

# Testing the database
if __name__ == "__main__":
    db = Database()
    db.insert_record("John Doe", 30, "Fever, Cough")
    records = db.fetch_records()
    for record in records:
        print(record)
    db.close()
