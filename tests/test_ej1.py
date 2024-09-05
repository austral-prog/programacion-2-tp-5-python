import pytest
from src.library import Library

@pytest.fixture
def library():
    return Library()


def test_add_book(library):
    library.add_book("The Great Gatsby", "Fitzgerald", "9780743273565")
    assert len(library.books) == 1
    assert library.books[0] == ["9780743273565", "The Great Gatsby", "Fitzgerald", True, 0]
    library.add_book("The Great Gatsby 2", "Fitzgerald", "9780743273566")
    assert len(library.books) == 1
    assert library.books[1] == ["9780743273566", "The Great Gatsby 2", "Fitzgerald", True, 0]

def test_list_all_books(capsys, library):
    library.add_book("1984", "Orwell", "9780451524935")
    library.add_book("To Kill a Mockingbird", "Lee", "9780061120084")
    library.list_all_books()

    captured = capsys.readouterr()
    assert "ISBN: 9780451524935, Title: 1984, Author: Orwell" in captured.out
    assert "ISBN: 9780061120084, Title: To Kill a Mockingbird, Author: Lee" in captured.out


def test_check_out_book(library):
    library.add_book("Moby Dick", "Melville", "9781503280786")
    library.add_user(11111111, "John Doe")

    assert library.check_out_book("9781503280786", 11111111, "10/09/2024") == True
    assert library.books[0][3] == False  # The book should now be unavailable
    assert len(library.checked_out_books) == 1


def test_check_out_unavailable_book(library):
    library.add_book("Moby Dick", "Melville", "9781503280786")
    library.add_user(11111111, "John Doe")
    library.check_out_book("9781503280786", 11111111, "10/09/2024")

    # Try to check out the same book again
    assert library.check_out_book("9781503280786", 11111111, "11/09/2024") == False


def test_return_book(library):
    library.add_book("Moby Dick", "Melville", "9781503280786")
    library.add_user(11111111, "John Doe")
    library.check_out_book("9781503280786", 11111111, "10/09/2024")

    assert library.return_book("9781503280786", 11111111, "15/09/2024") == True
    assert library.books[0][3] == True  # The book should now be available again
    assert len(library.checked_out_books) == 0
    assert len(library.checked_in_books) == 1
