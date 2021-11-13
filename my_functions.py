from book import Book
import json
# print options
def print_options():
    print("Press the specific button for that action")
    print("1-create a new book")
    print("2-save books locally")
    print("3-load the books from the disk")
    print("4-issue book")
    print("5-return a book")
    print("6-update a book")
    print("7-show all books")
    print("8-show book")

# create book function

def input_book_info():
    id = input("ID: ")
    name = input("Name: ")
    description = input("Description: ")
    isbn = input("Isbn: ")
    page_count = input("Page Count: ")
    issued = input("Issued: y/Y for True, anything else for False")
    issued = (issued =="y" or issued =="Y")
    author = input("Author name: ")
    year = int(input("Year: "))

    return {
        'id': id,
        'name': name,
        'description': description,
        'isbn': isbn,
        'page_count': page_count,
        'issued': issued,
        'author': author,
        'year': year,
    }


def create_book():
    print("Please enter your information")
    book_input = input_book_info()
    book = Book(book_input['id'], book_input['name'], book_input['description'], book_input['isbn'], book_input['page_count'], book_input['issued'], book_input['author'], book_input['year'])

    print(book.to_dict())
    return book

# defining save books
def save_books(books):
    json_books = []
    for book in books:
        json_books.append(book.to_dict())
    try:
        file = open("books.dat", "w")
        file.write(json.dumps(json_books, indent=4))
    except:
        print("We had an error saving books")


def load_books():
    try: 
        file = open("books.dat", "r")
        loaded_books = json.loads(file.read())
        books = []
        for book in loaded_books:
            new_obj = Book(book['id'], book['name'], book['description'], book['isbn'], book['page_count'], book['issued'], book['author'], book['year'])
            books.append(new_obj)
        print("Successfully loaded books")
        return books
    except:
        print("The file does not exist or an error occurred ducring loading")


# find the book function
# takes books and id
# if found it return the index of the book in the array, if not it returns nothing

def find_book(books, id):
    for index, book in enumerate(books):
        if book.id == id:
            return index
    return None


#issue book
# asks the user for the id input
# finds the id that we're looking for
# sets the value of the issued to true for that book

def issue_book(books):
    id = input("Enter the id of the book you want to issue: ")
    book_index = find_book(books, id)
    if book_index is not None:
        books[book_index].issued = True
        print("Book successfully issued")
    else:
        print("Could not find book with specified id.")

def return_book(books):
    id = input("Enter the id of the book you want to return: ")
    book_index = find_book(books, id)
    if book_index is not None:
        books[book_index].issued = False
        print("Book successfully returned")
    else:
        print("Could not find book with specified id.")


def update_book(books):
    id = input("Enter the id of the book you want to update: ")
    index = find_book(books, id)
    if index is not None:
        new_book = create_book()
        old_book = books[index]
        books[index] = new_book
        del old_book
        print("Book successfully updated")
    else:
        print("We could not find book with specified id.")


def show_all_books(books):
    for book in books:
        print(book.to_dict())

def show_book(books):
    id = input("Enter the id of the book you're looking for: ")
    index = find_book(books, id)
    if index is not None:
        print(books[index].to_dict())
    else:
        print("We could not find your book.")