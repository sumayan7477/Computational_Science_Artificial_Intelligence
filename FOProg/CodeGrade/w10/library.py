BOOKS = {
    "9780135166307":("Python Basics","Jane Smith"),
    "9781492051367":("Programming Fundamentals","Jone Doe"),
    "9780134853987":("Think Python","Allen Downey")
    }
def print_books(books):
    for isbn in books:
        print("ISBN:", isbn , end = "," )
        print(" Title:", books[isbn][0], end=",")
        print(" Author:", books[isbn][1])

def search_book(books , isbn):
    if isbn in books:
        return books[isbn]
    else:
        return None
    
def add_book(books, isbn, title, author):
    if isbn in books:
        return (False , books)
    else:
        books[isbn]=(title, author)
        return(True , books)
    
def count_books(books):
    return len(books)

def main():
    print("All books")
    print_books(BOOKS)

    result = search_book(BOOKS , "9780135166307")
    print(f"Search for : {result}")

    result = search_book(BOOKS , "0000000000")
    print(f"Search for : {result}")
    print()

    added, books = add_book(
        BOOKS, "9780135166307" , "Duplicate Book", "Test author"
        )
    print(f"Added duplicate: {added}")

    added, book = add_book(
        BOOKS, "1234567890", "DSA" , "Maria"
        )
    
    print(f"Total books: {count_books(BOOKS)}")

    print("All books after adding:")
    print_books(BOOKS)






















    
