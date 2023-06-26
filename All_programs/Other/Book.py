"""__str__ method is called (if defined in the class) to print information about the class
object to the console using the print() and str() functions"""

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return (f"Книга: {self.title}; {self.author}; {self.pages}")

book = Book('Python ООП', 'Balakirev', 1024)

print(book)