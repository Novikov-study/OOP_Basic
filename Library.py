class Author:
    def __init__(self, first_name, last_name, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def full_name(self):
        return self.first_name + ' ' + self.last_name


class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True

    def book_info(self):
        availability = "доступна" if self.is_available else "недоступна"
        return f"'{self.title}', {self.author.full_name()}, опубликована в {self.publication_year}, книга {availability}"

    def checkout(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            return True
        return False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def find_books_by_author(self, author_name):
        found_books = []
        for book in self.books:
            if book.author.full_name() == author_name:
                found_books.append(book)

        return found_books

class Reader:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.checked_out_books = []

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def checkout_book(self, book):
        if book.is_available:
            book.checkout()
            self.checked_out_books.append(book)
            return True
        else:
            print(f"Книга '{book.title}' недоступна для выдачи")
            return False

    def return_book(self, book):
        if book in self.checked_out_books:
            book.return_book()
            self.checked_out_books.remove(book)
            return True
        else:
            print(f"Книга '{book.title}' не числится за читателем {self.full_name()}")
            return False

class LibrarySystem:
    def __init__(self):
        self.books = []
        self.readers = []

    def add_book(self, book):
        self.books.append(book)

    def add_reader(self, reader):
        self.readers.append(reader)

    def checkout_book(self, reader, book):
        if book in self.books and reader in self.readers:
            if reader.checkout_book(book):
                return True
        print("Выдача книги невозможна")
        return False

    def return_book(self, reader, book):
        if book in self.books and reader in self.readers:
            if reader.return_book(book):
                return True
        print("Возврат книги невозможен")
        return False

    def get_book_info(self, book):
        if book in self.books:
            return book.book_info()
        return "Книга не найдена в библиотеке"

    def get_reader_info(self, reader):
        if reader in self.readers:
            return {
                "Полное имя": reader.full_name(),
                "Выданные книги": [b.title for b in reader.checked_out_books],
            }
        return "Читатель не найден в библиотеке"

def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

def log(func):
    def wrapper(*args, **kwargs):
        print(f"Вызвана функция {func.__name__} с аргументами {args} и {kwargs}")
        return func(*args, **kwargs)
    return wrapper
