class Publisher:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Publisher:", self.name)


class Book(Publisher):
    def __init__(self, title, author, name):
        super().__init__(name)
        self.title = title
        self.author = author

    def display(self):
        super().display()
        print("Title:", self.title)
        print("Author:", self.author)


class Python(Book):
    def __init__(self, title, author, name, price, no_of_pages):
        super().__init__(title, author, name)
        self.price = price
        self.no_of_pages = no_of_pages

    def display(self):
        super().display()
        print("Price:", self.price)
        print("Number of Pages:", self.no_of_pages)


python_book = Python("Python Programming", "John Doe", "ABC Publications", 39.99, 300)
python_book.display()