from types import NoneType
from User import User
from admin import Admin
import exceptions as ex
import unittest

class TestUser(unittest.TestCase):
    
    def test_creation(self):
        User("Hamid", "Rezaei", "0123456789", "myPass123", "09122224444")
        self.assertRaises(ex.InstantiateError, User, "Hamid", "Rezaei", "0123456789", "myPass123")
    
    def test_instantiation(self):
        test_user = User("Hamid", "Rezaei", "0123456799", "myPass123", "09122224444")
        self.assertEqual(test_user.first_name, "Hamid")
        self.assertEqual(test_user.last_name, "Rezaei")
        self.assertEqual(test_user.id_number, "0123456799")
        self.assertEqual(test_user.password, "myPass123")
        self.assertEqual(test_user.phone_number, "09122224444")
    
    def test_id_number(self):
        self.assertRaises(ex.IDNumberError, User, "Hamid", "Rezaei", "0123456", "123")
    
    def test_password(self):
        self.assertRaises(ex.PasswordError, User, "Hamid", "Rezaei", "0123256781", "pas")
    
    def test_phone_number(self):
        # Must start with "09":
        self.assertRaises(ex.PhoneError, User, "Hamid", "Rezaei", "0123456581", "myPass123", "56122224444")
        # Must be 1 chars:
        self.assertRaises(ex.PhoneError, User, "Hamid", "Rezaei", "0123456581", "myPass123", "56122")

    
class TestAdmin(unittest.TestCase):
    def test_creation(self):
        Admin("Saeed", "Rezaei", "0123456781", "myPass123", "09122224444")
        self.assertRaises(ex.InstantiateError, Admin, "Hamid", "Rezaei", "0123456781", "myPass123")
    
    def test_instantiation(self):
        test_admin = Admin("Saeed", "Rezaei", "0123654781", "myPass123", "09122224444")
        self.assertEqual(test_admin.first_name, "Saeed")
        self.assertEqual(test_admin.last_name, "Rezaei")
        self.assertEqual(test_admin.id_number, "0123654781")
        self.assertEqual(test_admin.password, "myPass123")
        self.assertEqual(test_admin.phone_number, "09122224444")
    
    def test_id_number(self):
        self.assertRaises(ex.IDNumberError, Admin, "Saeed", "Rezaei", "0123256", "123")
    
    def test_password(self):
        self.assertRaises(ex.PasswordError, Admin, "Saeed", "Rezaei", "3213256781", "pas")
    
    def test_phone_number(self):
        # Must start with "09":
        self.assertRaises(ex.PhoneError, Admin, "Saeed", "Rezaei", "0123456121", "myPass123", "56122224444")
        # Must be 1 chars:
        self.assertRaises(ex.PhoneError, Admin, "Saeed", "Rezaei", "0123456121", "myPass123", "56122")   

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
    


if __name__ == '__main__':
    unittest.main()