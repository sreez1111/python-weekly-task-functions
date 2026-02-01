library = []

def add_book(book):
    library.append(book)
    print(book, "added")

def issue_book(book):
    if book in library:
        library.remove(book)
        print(book, "issued")
    else:
        print(book, "not available")

def return_book(book):
    library.append(book)
    print(book, "returned")

def search_book(book):
    if book in library:
        print(book, "is available")
    else:
        print(book, "not available")

# 🔽 FUNCTION CALLS
add_book("Python")
add_book("Java")

issue_book("Python")
search_book("Python")

return_book("Python")
search_book("Python")
