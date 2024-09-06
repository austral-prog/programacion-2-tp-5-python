from src.Book import Book
from src.User import User


class Library:
    def __init__(self):
        self.__books = []
        self.__users = []
        self.__checked_out_books = []
        self.__checked_in_books = []

    # Getters
    def get_books(self):
        return self.__books

    def get_users(self):
        return self.__users

    def get_checked_out_books(self):
        return self.__checked_out_books

    def get_checked_in_books(self):
        return self.__checked_in_books

    # 1.1 Add Book
    def add_book(self, isbn, title, author):
        pass

    # 1.2 List All Books
    def list_all_books(self):
        pass

    # 2.1 Check out book
    def check_out_book(self, isbn, dni, due_date):
        pass

    # 2.2 Check in book
    def check_in_book(self, isbn, dni, returned_date):
        pass

    # Utils
    def add_user(self, dni, name):
        pass
