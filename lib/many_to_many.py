class Author:
    all = []

    def __init__(self, name):
        if not isinstance (name, str):
            print ("Title must be a string.")

        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if self == contract.author]
    
    def books(self):
        return [contract.book for contract in Contract.all if self == contract.author]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        return sum([contract.royalties for contract in Contract.all if self == contract.author])


class Book:
    all = []

    def __init__(self, title):
        if not isinstance (title, str):
            print ("Title must be a string.")
        else:
            self.title = title
            Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if self == contract.book]
            
    def authors(self):
        return [contract.author for contract in Contract.all if self == contract.book]

class Contract:
    all = []

    def __init__ (self, author, book, date, royalties):
        if not isinstance (date, str):
            raise Exception ("Date must be a string.")
        elif not isinstance (author, Author):
            raise Exception ("Author must be an instance of the 'Author' class.")
        elif not isinstance (book, Book):
            raise Exception ("Book must be an instance of the 'Book' class.")
        elif not isinstance (royalties, int):
            raise Exception ("Royalties must be an integer.")
        else:
            self.author = author
            self.book = book
            self.date = date
            self.royalties = royalties
            Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if date == contract.date]
   
