class Book:
    def __init__(self, bid, author, title, price):
        self.bid = bid
        self.author = author
        self.title = title
        self.price = price


if __name__ == "__main__":
    book1 = Book(101, "George Orwell", "1984", 299)
    print(book1.bid, book1.author, book1.title, book1.price)
