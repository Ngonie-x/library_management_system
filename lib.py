import json
from book import Book
# to make a save function first we have to load books thrn make changes
def load_books():
    try:
        file = open("book.dat", 'r')
        books_dict = json.loads(file.read())
        books = []
        # id, name, description, isbn, page_count, issued, author, year
        for book in books_dict:
            book_obj = Book(book['id'], book['name'], book['description'], book['isbn'], book['page_count'], book['issued'], book['author'], book['year'])
            books.append(book_obj)
        return books
    except:
        return []




def save_books(books):
    json_books = []
    for book in books:
        json_books.append(book.to_dict())
    with open("book.dat", "w") as file:
        file.write(json.dumps(json_books, indent=4))


def add_book(book):
    books = load_books()
    new_book = Book(book['id'], book['name'], book['description'], book['isbn'], book['page_count'], book['issued'], book['author'], book['year'])
    save_books([*books, assign_valid_id(books, new_book)])


def assign_valid_id(books, new_book):
    books_ids = []
    for book in books:
        books_ids.append(int(book.id))
    if list(filter(lambda id: id == int(new_book.id), books_ids)) == []:
        return new_book
    else:
        new_book.id = int(max(books_ids)+1)
        return new_book

def get_issued_books():
    books = load_books()
    return list(filter(lambda book: book.issued == True,books))

def get_unissued_books():
    books = load_books()
    return list(filter(lambda book: book.issued == False,books))


def find_book(book_id):
    books = load_books()
    for book in books:
        if int(book.id) == book_id:
            return book

    return None

def update_book(book):
    book = Book(book['id'], book['name'], book['description'], book['isbn'], book['page_count'], book['issued'], book['author'], book['year'])
    books = load_books()
    if book != None:
        books = list(filter(lambda bk: int(bk.id)!=int(book.id), books))
        books.append(book)
        save_books(books)


def delete_book(book_id):
    books = load_books()
    books = list(filter(lambda bk: int(bk.id) != int(book_id), books))
    save_books(books)