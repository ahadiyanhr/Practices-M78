class Person():
    def __init__(self, name, email, gender):
        self.name = name
        self.email = email
        self.gender = gender
    
class Author(Person):
    def __init__(self, name, email, gender, authorCode, genre):
        super().__init__(name, email, gender)
        self.authorCode = authorCode
        self.genre = genre
    
class Poet(Person):
    def __init__(self, name, email, gender, type):
        super().__init__(name, email, gender)
        self.type = type
    
class Researcher(Person):
    def __init__(self, name, email, gender, field, affliation):
        super().__init__(name, email, gender)
        self.field = field
        self.affliation = affliation
    

class Work():
    def __init__(self, title, *owners):
        self.title = title
        
        # Check the list of owners is a Person Object:
        for names in owners:   
            # eval for convert str to obj:
            if not isinstance(eval(names), Person):
                raise AttributeError(f"{names} is not in Person list!")
        else:
            self.owners = owners
    
class Book(Work):
    def __init__(self, ISBN, publisher, title, *owners):
        super().__init__(title, *owners)
        self.ISBN = ISBN
        self.publisher = publisher

    def ownersNo(self):
        numbers = len(self.owners)
        return numbers
    
class Poem(Work):
    def __init__(self, type, title, owners):
        # Poems can have only one Owner
        # then we use owners without *
        super().__init__(title, owners)
        self.type = type
    
class Papers(Work):
    def __init__(self, journal, date, title, *owners):
        super().__init__(title, *owners)
        self.journal = journal
        self.date = date

    def ownersNo(self):
        numbers = len(self.owners)
        return numbers
    

'''Example 1:'''
# Define two Author and one researcher:
hamid = Author('Hamid', 'hamid@gmail.com', 'M', '4632154', 'Fiction')
saeed = Author('Saeed', 'saeed@gmail.com', 'M', '8472364', 'Philosophy')
fatemeh = Researcher('Fatemeh', 'fatemeh@gmail.com', 'F', 'Mathematics', 'University of Tehran')
# Define a book belongs to them:
book1 = Book('978-3-16-148410-0', 'Times', 'Theory of math', 'hamid', 'saeed', 'fatemeh')
# Print the owners of book (method of owners):
print('Owners are:', book1.owners)
print('No. of owners:', book1.ownersNo())

'''Example 2:'''
# If define "Fred Hoyle" without "Person() Class":
FredHoyle = 'FredHoyle'
# and set a paper for him you have an Attribute Error:
#paper1 = Papers('Journal of chemistry', '20210501', 'Bigbang Theory', 'FredHoyle')


'''Example 3:'''
# If define a poem with more than one owner you have an error:
poem1 = Poem('Ghazal1', 'My Love1', 'hamid')
print('Poet is:', poem1.owners)

poem2 = Poem('Ghazal2', 'My Love2', 'hamid', 'saeed')
print('Poet is:', poem2.owners)
