from abc import ABC, abstractclassmethod
from re import I

class Repository:
    '''
    1. len() = no of books
    '''
    pass

class Bookshelf:
    '''
    1. like a list
    2. capacity < 10000 pages
    3. tag = category id-n
    '''
    pass


class Book:
    
    def __init__(self, name, no_of_pages, ISBN, price, category, *authors):
        # read only, not editable
        self.name = name
        self.no_of_pages = no_of_pages
        self.ISBN = ISBN
        self.price = price
        self.category = category ## ?? class cat.
        self.authors = authors # ??? one or more & class author

    pass


class Human(ABC):
    persons = set()
    def __init__(self, name, age, id_num):
        self.name = name
        self.age = age
        self.id_num = id_num
        
    @property
    def id_num(self):
        return self._id_num
    
    @id_num.setter
    def id_num(self, id_num:str):
        if id_num in Human.persons:
            raise ValueError(f"There is a author or librarian with ID Number of {id_num}.")
        self._id_num = id_num
        Human.persons.add(id_num)


class Author(Human):
    authors = {}
    def __init__(self, name: str, age: int, id_num: str, *books: list) -> None:
        super().__init__(name, age, id_num)
        self.books = books
        Author.authors[self.id_num] = (self.name, self.books)
        
    
    # Calculate the no. of books of specific author
    def __len__(self, id_num: str):
        if id_num in Author.authors.keys():
            return len(Author.authors[id_num][1])
        return f"There is not any author with ID Number of {id_num}."


class Librarian(Human):
    librarians = set()
    
    def __inin__(self, name: str, age: int, id_num: str) -> None:
        super().__init__(name, age, id_num)
        Librarian.librarians.add(id_num)
    
    
    def search_book(self, info):
        pass
    
    def create_category(self, name:str) -> object:
        return Category(name)
    '''
    Methods:
    1. search (name/id/author(code,name)) -> list of books(name, bookshelf, author, id)
    2. take a book with id
    4. take back a book (cat. id/ id/ name/ author)
    
    '''
class Category:
    '''
    must add by librarian
    '''
    cat_names = set() # Sets of category names which its names are unique
    
    def __init__(self, name:str):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, cat_name:str):
        if cat_name in Category.cat_names:
            raise ValueError(f"{cat_name} is not unique. Please enter another one.")
        self._name = cat_name
        Category.cat_names.add(cat_name)
    
    def __len__(self):
        return len(Category.cat_names)

cat1 = Category("hamid")

lib1 = Librarian('hamid', 15)
lib1.create_category("hamid1")
print(Category.cat_names)









