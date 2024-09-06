import unittest

from src.Book import Book


class TestBook(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        self.book1 = Book("9788498386561", "Harry Potter", "Rowling")
        self.book2 = Book("9788498386561", "Harry Potter", "Rowling")
        self.book3 = Book("9788493806125", "Don Quijote", "Cervantes")

    def test_initialization(self):
        """Test the initialization of the Book class."""
        self.assertEqual(self.book1.get_isbn(), "9788498386561")
        self.assertEqual(self.book1.get_title(), "Harry Potter")
        self.assertEqual(self.book1.get_author(), "Rowling")
        self.assertTrue(self.book1.is_available())
        self.assertEqual(self.book1.get_checkout_num(), 0)

    def test_set_available(self):
        """Test setting the availability of the book."""
        self.book1.set_available(False)
        self.assertFalse(self.book1.is_available())
        self.book1.set_available(True)
        self.assertTrue(self.book1.is_available())

    def test_increment_checkout_num(self):
        """Test incrementing the checkout number."""
        self.book1.increment_checkout_num()
        self.assertEqual(self.book1.get_checkout_num(), 1)
        self.book1.increment_checkout_num()
        self.assertEqual(self.book1.get_checkout_num(), 2)

    def test_eq_method(self):
        """Test the equality comparison of Book objects."""
        self.assertEqual(self.book1, self.book2)  # Same ISBN
        self.assertNotEqual(self.book1, self.book3)  # Different ISBN

    def test_str_method(self):
        """Test the string representation of the Book object."""
        expected_str = "ISBN: 9788498386561, Title: Harry Potter, Author: Rowling"
        self.assertEqual(str(self.book1), expected_str)

if __name__ == "__main__":
    unittest.main()
