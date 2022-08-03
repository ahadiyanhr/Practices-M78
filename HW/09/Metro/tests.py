from types import NoneType
import exceptions as ex
import unittest

from User import User
from Admin import Admin
from BankAccount import BankAccount
from MetroCard import CreditCard

# class TestUser(unittest.TestCase):
    
#     def test_user_creation(self):
#         # Users with the same National ID Number must not created:
#         User("Hamid", "Rezaei", "0123456789", "myPass123", "09122224444")
#         self.assertRaises(ex.InstantiateError, User, "Hamid", "Rezaei", "0123456789", "myPass123")
    
#     def test_user_instantiation(self):
#         # Check the new user instantiate correctly:
#         test_user = User("Hamid", "Rezaei", "0123456799", "myPass123", "09122224444")
#         self.assertEqual(test_user.first_name, "Hamid")
#         self.assertEqual(test_user.last_name, "Rezaei")
#         self.assertEqual(test_user.id_number, "0123456799")
#         self.assertEqual(test_user.password, "myPass123")
#         self.assertEqual(test_user.phone_number, "09122224444")
    
#     def test_user_id_number(self):
#         # National ID Number must be 10 characters:
#         self.assertRaises(ex.IDNumberError, User, "Hamid", "Rezaei", "0123456", "123")
    
#     def test_user_password(self):
#         # Password must be at least 4 characters:
#         self.assertRaises(ex.PasswordError, User, "Hamid", "Rezaei", "0123256781", "pas")
    
#     def test_user_phone_number(self):
#         # Phone number must start with "09":
#         self.assertRaises(ex.PhoneError, User, "Hamid", "Rezaei", "0123456581", "myPass123", "56122224444")
#         # Phone number must be 11 chars:
#         self.assertRaises(ex.PhoneError, User, "Hamid", "Rezaei", "0123456581", "myPass123", "56122")

    
# class TestAdmin(unittest.TestCase):
    
#     def test_admin_creation(self):
#         # Admins with the same National ID Number of other users or admins must not created:
#         Admin("Saeed", "Rezaei", "0123456781", "myPass123", "09122224444")
#         self.assertRaises(ex.InstantiateError, Admin, "Hamid", "Rezaei", "0123456781", "myPass123")
    
#     def test_admin_instantiation(self):
#         # Check the new admin instantiate correctly:
#         test_admin = Admin("Saeed", "Rezaei", "0123654781", "myPass123", "09122224444")
#         self.assertEqual(test_admin.first_name, "Saeed")
#         self.assertEqual(test_admin.last_name, "Rezaei")
#         self.assertEqual(test_admin.id_number, "0123654781")
#         self.assertEqual(test_admin.password, "myPass123")
#         self.assertEqual(test_admin.phone_number, "09122224444")
    
#     def test_admin_id_number(self):
#         # National ID Number must be 10 characters:
#         self.assertRaises(ex.IDNumberError, Admin, "Saeed", "Rezaei", "0123256", "123")
    
#     def test_admin_password(self):
#         # Password must be at least 4 characters:
#         self.assertRaises(ex.PasswordError, Admin, "Saeed", "Rezaei", "3213256781", "pas")
    
#     def test_admin_phone_number(self):
#         # Phone number must start with "09":
#         self.assertRaises(ex.PhoneError, Admin, "Saeed", "Rezaei", "0123456121", "myPass123", "56122224444")
#         # Phone number must be 11 chars:
#         self.assertRaises(ex.PhoneError, Admin, "Saeed", "Rezaei", "0123456121", "myPass123", "56122")   

# class TestBankAccount(unittest.TestCase):
    
#     def test_bankaccount_creation(self):
#         # A User with an National ID Number can have only one bank account:
#         test_user = User("Hamid", "Rezaei", "8826656799", "myPass123", "09122224444")
#         test_account = BankAccount(test_user, 1000000)
#         self.assertRaises(ex.InstantiateError, BankAccount, test_user, 1000000)
    
#     def test_bankaccount_instantiation(self):
#         # Check the new bank account instantiate correctly:
#         test_user = User("Hamid", "Rezaei", "8823456799", "myPass123", "09122224444")
#         test_account = BankAccount(test_user, 1000000)
#         self.assertEqual(test_account.owner, test_user)
#         self.assertEqual(test_account.balance, 1000000)
    
#     def test_bankaccount_owner(self):
#         # Check the owner be an user object:
#         self.assertRaises(ex.OwnerInstanceError, BankAccount, "test_user", 1000000)
        
#     def test_bankaccount_balance(self):
#         # Check the new account has a balance more than minimum:
#         test_user = User("Hamid", "Rezaei", "8821456799", "myPass123", "09122224444")
#         self.assertRaises(ex.AccountBalanceError, BankAccount, test_user, 10000) 
    
#     def test_bankaccount_deposite(self):
#         # Check deposite method:
#         test_user = User("Hamid", "Rezaei", "8821456719", "myPass123", "09122224444")
#         test_account = BankAccount(test_user, 1000000)
#         self.assertEqual(test_account.deposite(1000000, test_user.auth_code), 2000000)
#         # Check the correct Authentication Code for deposition:
#         with self.assertRaises(ex.DepositeError):
#             test_account.deposite(10000, 'wrong_authcode')
    
#     def test_bankaccount_withdraw(self):
#         # Check withdrawal method:
#         test_user = User("Hamid", "Rezaei", "8876556719", "myPass123", "09122224444")
#         test_account = BankAccount(test_user, 1000000)
#         self.assertEqual(test_account.withdraw(1000, test_user.auth_code), 998400)
#         # Check the enough account balance for withdrawal:
#         with self.assertRaises(ex.NotEnoughBalance):
#             test_account.withdraw(999500, test_user.auth_code)
#         # Check the correct Authentication Code for withdrawal:
#         with self.assertRaises(ex.WithdrawError):
#             test_account.withdraw(10000, 'wrong_authcode')
            
#     def test_bankaccount_transfer(self):
#         # Check transfer method:
#         test_user1 = User("Hamid", "Rezaei", "8876336729", "myPass123", "09122224444")
#         test_account1 = BankAccount(test_user1, 1000000)
#         test_user2 = User("Saeed", "Rezaei", "8876336720", "myPass123", "09122224444")
#         test_account2 = BankAccount(test_user2, 1000000)
#         self.assertEqual(test_account1.transfer(test_account2, 5000, test_user1.auth_code), 995000)
#         # Check the raising error:
#         with self.assertRaises(ex.TransferingError):
#             # Check the correct Authentication Code for transfering:
#             test_account1.transfer(test_account2, 5000, "wrong_authcode")
#         with self.assertRaises(ex.IsNotBankAccount):
#             # Check the input destination account exist for transfering:
#             test_account1.transfer("test_account3", 5000, test_user1.auth_code)


class CreditCard(unittest.TestCase):
    def test_creditcard_creation(self):
        # A User with an National ID Number can have only one CreditCard:
        test_user = User("Hamid", "Rezaei", "8826656700", "myPass123", "09122224444")
        CreditCard(test_user, 1000000)
    #     # A User with an National ID Number can have only one bank account:
    #     test_user = User("Hamid", "Rezaei", "8826656700", "myPass123", "09122224444")
        # card1 = CreditCard(test_user, 1000000)
        # test_card = CreditCard(test_user, 50000)
        # self.assertRaises(ex.InstantiateError, CreditCard, test_user, 1000000)
    
    # def test_bankaccount_instantiation(self):
    #     # Check the new bank account instantiate correctly:
    #     test_user = User("Hamid", "Rezaei", "8823456799", "myPass123", "09122224444")
    #     test_card = CreditCard(test_user, 1000000)
    #     self.assertEqual(CreditCard.owner, test_user)
    #     self.assertEqual(CreditCard.balance, 1000000)
    
    # def test_bankaccount_owner(self):
    #     # Check the owner be an user object:
    #     self.assertRaises(ex.OwnerInstanceError, BankAccount, "test_user", 1000000)
        
    # def test_bankaccount_balance(self):
    #     # Check the new account has a balance more than minimum:
    #     test_user = User("Hamid", "Rezaei", "8821456799", "myPass123", "09122224444")
    #     self.assertRaises(ex.AccountBalanceError, BankAccount, test_user, 10000) 

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