from database import Database

class HealthCheck:
    def __init__(self):
        self.db = Database()

    def add_record(self, name, age, symptoms):
        self.db.insert_record(name, age, symptoms)

    def get_records(self):
        return self.db.fetch_records()

# Testing the backend
if __name__ == "__main__":
    health = HealthCheck()
    health.add_record("Jane Doe", 25, "Headache, Fatigue")
    records = health.get_records()
    for record in records:
        print(record)

