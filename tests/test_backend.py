import unittest
from backend import HealthCheck  # Import the class from backend.py

class TestHealthCheck(unittest.TestCase):
    def setUp(self):
        """Create a fresh instance before each test"""
        self.health = HealthCheck()

    def test_add_record(self):
        """Test adding a record"""
        self.health.add_record("Alice", 28, "Headache, Cough")
        records = self.health.get_records()
        self.assertGreater(len(records), 0)  # Ensure at least 1 record exists

    def test_get_records(self):
        """Test fetching records"""
        self.health.add_record("Bob", 35, "Fever, Sore throat")
        records = self.health.get_records()
        self.assertEqual(records[-1][1], "Bob")  # Check last inserted name

if __name__ == "__main__":
    unittest.main()
