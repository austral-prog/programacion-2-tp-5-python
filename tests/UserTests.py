import unittest

from src.User import User


class TestUser(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        self.user1 = User(12345678, "Alice")
        self.user2 = User(12345678, "Alice")
        self.user3 = User(98765432, "Bob")

    def test_initialization(self):
        """Test the initialization of the User class."""
        self.assertEqual(self.user1.get_dni(), 12345678)
        self.assertEqual(self.user1.get_name(), "Alice")
        self.assertEqual(self.user1.get_number_of_checkouts(), 0)
        self.assertEqual(self.user1.get_number_of_checkins(), 0)

    def test_increment_checkouts(self):
        """Test incrementing the number of checkouts."""
        self.user1.increment_checkouts()
        self.assertEqual(self.user1.get_number_of_checkouts(), 1)
        self.user1.increment_checkouts()
        self.assertEqual(self.user1.get_number_of_checkouts(), 2)

    def test_increment_checkins(self):
        """Test incrementing the number of check-ins."""
        self.user1.increment_checkins()
        self.assertEqual(self.user1.get_number_of_checkins(), 1)
        self.user1.increment_checkins()
        self.assertEqual(self.user1.get_number_of_checkins(), 2)

if __name__ == "__main__":
    unittest.main()
