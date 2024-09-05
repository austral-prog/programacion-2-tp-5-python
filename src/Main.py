books = [
    #  ISBN, TITLE, AUTHOR, AVAILABLE, CHECKOUT_NUM
    ["9788498386561", "Harry Potter", "Rowling", False, 2],
    ["9788493806125", "Don Quijote", "Cervantes", True, 0]
]
users = [
    # DNI, NAME, NUMBER_OF_CHECKOUTS, NUMBER_OF_CHECKINS
    [12345678, "Alice", 3, 2]
    [98765432, "Bob", 5, 1]
]
checked_out_books = [
    # ISBN, DNI, DUE_DATE
    ["9788498386561", 12345678, "1/10/2023"],
    ["9788498386561", 12345678, "23/10/2023"]
]
checked_in_books = [
    # ISBN, DNI, RETURNED_DATE
    ["9788498386561", 12345678, "1/10/2023"]
]
