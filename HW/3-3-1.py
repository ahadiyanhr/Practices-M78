class Book():
    
    # Book attributes:
    def __init__(self, title, price, numbers):
        self.title = title       
        self.price = price
        # Check the numbers of book be positive:
        if numbers > 0 and isinstance(numbers,int):
            self.numbers = numbers
        else:
            raise AttributeError('The numbers of book must be a positive integer.') 
    
    # Description of book in bookstore:  
    def __str__(self):
        return f"There are {self.numbers} of {self.title} in this bookstore. The price of them is about {self.price}$."

    # A method for display a string:
    def display(self, myStr = str):
        return myStr

# Example:    
mathmatics = Book('Mathmatics', 130, 1)
print(mathmatics)
print(mathmatics.display('This my string according to what you want in this problem.'))

    
