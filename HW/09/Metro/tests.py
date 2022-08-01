from User import User
import unittest

class TestUser(unittest.TestCase):
    
    def test_user_creation(self):
        print("sd13535f")
        test_user = User("Hamid", "Rezaei", "myPass123", '09122224444')
        self.assertEqual(test_user.first_name, "Hamid")
        self.assertEqual(test_user.last_name, "Rezaei")
        self.assertEqual(test_user.password, "myPass123")
        self.assertEqual(test_user.phone_number, "09122224444")
    
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
    # show error if card has not enough credit
    # single-credit-limited
    # save in cards.pickle and its owner

class TestTrip(unittest.TestCase):
    pass

    # create trip (origin, destination, Fare)
    # each trip can do by one until end

class TestMain(unittest.TestCase):
    pass
    # 1. user register ==> pickle it, show Authentication id
    # 2. bank account management ==> with Authentication id
    # 3. record a trip to a dict (key: trip_number, value: info): get A_id, select MetroCard (ask about charge it?), Pay for ticket and record it
    # 4. Management: get Admin_id and password, go to admin control:
    #   record a metro trip
    #   edit a trip that has already been made 
    
