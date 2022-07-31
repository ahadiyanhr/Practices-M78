import unittest

class TestUser(unittest.TestCase):
    pass
    # user creation
    # store user info in users.pickle
    # create a user only by program interface
    # must have a private_unique_id that produce by program and show it when a user create
    # ... works as Authentication id to have a trip or use bank account
    
class TestAdmin(unittest.TestCase):
    pass
    # a subclass of user for create admins
    # store admin info in admins.pickle
    # only admins can control the program
    # must have a private_unique_id that produce by program and show it when a user create
    # ... works as Authentication id to have a trip or use bank account
    

class TestBankAccount(unittest.TestCase):
    pass
    # create a bank account for a user-defined by program interface
    # ask Authentication id for each transaction
    # withdrawal
    # deposit

class MetroCard(unittest.TestCase):
    pass
    # a card must belong to a user and his/her bank account
    # charge a card with bank account
    
