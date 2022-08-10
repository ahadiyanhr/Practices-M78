from types import NoneType
import exceptions as ex
import unittest

from User import User
from Admin import Admin
from Trip import Trip
from BankAccount import BankAccount
from MetroCard import CreditCard, LimitedCard, SingleCard

class TestUser(unittest.TestCase):
    
    def test_user_creation(self):
        # Users with the same National ID Number must not created:
        User("Hamid", "Rezaei", "0123456789", "myPass123", "09122224444")
        self.assertRaises(ex.InstantiateError, User, "Hamid", "Rezaei", "0123456789", "myPass123")
    
    def test_user_instantiation(self):
        # Check the new user instantiate correctly:
        test_user = User("Hamid", "Rezaei", "0123456799", "myPass123", "09122224444")
        self.assertEqual(test_user.first_name, "Hamid")
        self.assertEqual(test_user.last_name, "Rezaei")
        self.assertEqual(test_user.id_number, "0123456799")
        self.assertEqual(test_user.password, "myPass123")
        self.assertEqual(test_user.phone_number, "09122224444")
        self.assertEqual(test_user.is_admin, False)
    
    def test_user_id_number(self):
        # National ID Number must be 10 characters:
        self.assertRaises(ex.IDNumberError, User, "Hamid", "Rezaei", "0123456", "123")
    
    def test_user_password(self):
        # Password must be at least 4 characters:
        self.assertRaises(ex.PasswordError, User, "Hamid", "Rezaei", "0123256781", "pas")
    
    def test_user_phone_number(self):
        # Phone number must start with "09":
        self.assertRaises(ex.PhoneError, User, "Hamid", "Rezaei", "0123456581", "myPass123", "56122224444")
        # Phone number must be 11 chars:
        self.assertRaises(ex.PhoneError, User, "Hamid", "Rezaei", "0123456581", "myPass123", "56122")

    
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

class TestBankAccount(unittest.TestCase):
    
    def test_bankaccount_creation(self):
        # A User with an National ID Number can have only one bank account:
        test_user = User("Hamid", "Rezaei", "8826656799", "myPass123", "09122224444")
        test_account = BankAccount(test_user, 1000000)
        self.assertRaises(ex.InstantiateError, BankAccount, test_user, 1000000)
    
    def test_bankaccount_instantiation(self):
        # Check the new bank account instantiate correctly:
        test_user = User("Hamid", "Rezaei", "8823456799", "myPass123", "09122224444")
        test_account = BankAccount(test_user, 1000000)
        self.assertEqual(test_account.owner, test_user)
        self.assertEqual(test_account.balance, 1000000)
    
    def test_bankaccount_owner(self):
        # Check the owner be an user object:
        self.assertRaises(ex.OwnerInstanceError, BankAccount, "test_user", 1000000)
        
    def test_bankaccount_balance(self):
        # Check the new account has a balance more than minimum:
        test_user = User("Hamid", "Rezaei", "8821456799", "myPass123", "09122224444")
        self.assertRaises(ex.AccountBalanceError, BankAccount, test_user, 10000) 
    
    def test_bankaccount_deposite(self):
        # Check deposite method:
        test_user = User("Hamid", "Rezaei", "8821456719", "myPass123", "09122224444")
        test_account = BankAccount(test_user, 1000000)
        self.assertEqual(test_account.deposite(1000000, test_user.auth_code), 2000000)
        # Check the correct Authentication Code for deposition:
        with self.assertRaises(ex.DepositeError):
            test_account.deposite(10000, 'wrong_authcode')
    
    def test_bankaccount_withdraw(self):
        # Check withdrawal method:
        test_user = User("Hamid", "Rezaei", "8876556719", "myPass123", "09122224444")
        test_account = BankAccount(test_user, 1000000)
        self.assertEqual(test_account.withdraw(1000, test_user.auth_code), 998400)
        # Check the enough account balance for withdrawal:
        with self.assertRaises(ex.NotEnoughBalance):
            test_account.withdraw(999500, test_user.auth_code)
        # Check the correct Authentication Code for withdrawal:
        with self.assertRaises(ex.WithdrawError):
            test_account.withdraw(10000, 'wrong_authcode')
            
    def test_bankaccount_transfer(self):
        # Check transfer method:
        test_user1 = User("Hamid", "Rezaei", "8876336729", "myPass123", "09122224444")
        test_account1 = BankAccount(test_user1, 1000000)
        test_user2 = User("Saeed", "Rezaei", "8876336720", "myPass123", "09122224444")
        test_account2 = BankAccount(test_user2, 1000000)
        self.assertEqual(test_account1.transfer(test_account2, 5000, test_user1.auth_code), 995000)
        # Check the raising error:
        with self.assertRaises(ex.TransferingError):
            # Check the correct Authentication Code for transfering:
            test_account1.transfer(test_account2, 5000, "wrong_authcode")
        with self.assertRaises(ex.IsNotBankAccount):
            # Check the input destination account exist for transfering:
            test_account1.transfer("test_account3", 5000, test_user1.auth_code)


class TestCreditCard(unittest.TestCase):
        
    def test_creditcard_creation(self):
        # A User with an National ID Number can have only one CreditCard:
        test_user = User("Hamid", "Rezaei", "8826656700", "myPass123", "09122224444")
        test_card = CreditCard(test_user, 1000000)
        self.assertRaises(ex.InstantiateError, CreditCard, test_user, 1000000)
    
    def test_creditcard_instantiation(self):
        # Check the new CreditCard instantiate correctly:
        test_user = User("Hamid", "Rezaei", "5423416799", "myPass123", "09122224444")
        test_card = CreditCard(test_user, 1000000)
        self.assertEqual(test_card.owner, test_user)
        self.assertEqual(test_card.balance, 1000000)
    
    def test_creditcard_owner(self):
        # Check the owner be an user object:
        self.assertRaises(ex.OwnerInstanceError, CreditCard, "test_user", 1000000)
        
    def test_creditcard_balance(self):
        # Check the new CreditCard has a negative balance:
        test_user = User("Hamid", "Rezaei", "0821456799", "myPass123", "09122224444")
        self.assertRaises(ex.CardBalanceError, CreditCard, test_user, -1) 

    def test_creditcard_charge(self):
        # Check charge method:
        test_user = User("Hamid", "Rezaei", "0021456719", "myPass123", "09122224444")
        test_account = BankAccount(test_user, 520000)
        test_card = CreditCard(test_user)
        self.assertEqual(test_card.charge(1000, test_user.auth_code), 1000)
        # Check the correct bank account has not enough money:
        with self.assertRaises(ex.NotEnoughBalance):
            test_card.charge(530000, test_user.auth_code)
        # Check the correct Authentication Code for charging:
        with self.assertRaises(ex.ChargeCardError):
            test_card.charge(10000, 'wrong_authcode')
            
    def test_creditcard_payticket(self):
        # Check pay_ticket method:
        test_user = User("Hamid", "Rezaei", "8876056719", "myPass123", "09122224444")
        test_account = CreditCard(test_user, 2000)
        self.assertEqual(test_account.pay_ticket(1000, test_user.auth_code), 1000)
        # Check the enough account balance for payticket:
        with self.assertRaises(ex.NotEnoughBalance):
            test_account.pay_ticket(3000, test_user.auth_code)
        # Check the correct Authentication Code for payticket:
        with self.assertRaises(ex.PayTicketError):
            test_account.pay_ticket(1000, 'wrong_authcode')

class TestLimitedCard(unittest.TestCase):
        
    def test_limitedcard_creation(self):
        # A User with an National ID Number can have only one LimitedCard:
        test_user = User("Hamid", "Rezaei", "8826652700", "myPass123", "09122224444")
        test_card = LimitedCard(test_user, 1000000)
        self.assertRaises(ex.InstantiateError, LimitedCard, test_user, 1000000)
    
    def test_limitedcard_instantiation(self):
        # Check the new LimitedCard instantiate correctly:
        test_user = User("Hamid", "Rezaei", "5429426799", "myPass123", "09122224444")
        test_card = LimitedCard(test_user, 1000000, 3)
        self.assertEqual(test_card.owner, test_user)
        self.assertEqual(test_card.balance, 1000000)
        self.assertEqual(test_card.limit_numbers, 3)
    
    def test_limitedcard_owner(self):
        # Check the owner be an user object:
        self.assertRaises(ex.OwnerInstanceError, LimitedCard, "test_user", 1000000, 2)
        
    def test_limitedcard_balance(self):
        # Check the new LimitedCard has a negative balance:
        test_user = User("Hamid", "Rezaei", "0121456799", "myPass123", "09122224444")
        self.assertRaises(ex.CardBalanceError, LimitedCard, test_user, -1) 

    def test_limitedcard_limitnumbers(self):
        # Check the Limited numbers less than 1:
        test_user = User("Hamid", "Rezaei", "0121496799", "myPass123", "09122224444")
        self.assertRaises(ex.LimitedNumbersError, LimitedCard, test_user, 10000, 0)
        
    def test_limitedcard_charge(self):
        # Check charge method:
        test_user = User("Hamid", "Rezaei", "6621456719", "myPass123", "09122224444")
        test_account = BankAccount(test_user, 520000)
        test_card = LimitedCard(test_user)
        self.assertEqual(test_card.charge(1000, test_user.auth_code), 1000)
        # Check the correct bank account has not enough money:
        with self.assertRaises(ex.NotEnoughBalance):
            test_card.charge(530000, test_user.auth_code)
        # Check the correct Authentication Code for charging:
        with self.assertRaises(ex.ChargeCardError):
            test_card.charge(10000, 'wrong_authcode')
            
    def test_limitedcard_payticket(self):
        # Check pay_ticket method:
        test_user = User("Hamid", "Rezaei", "8176050019", "myPass123", "09122224444")
        test_account = LimitedCard(test_user, 2000, 1)
        self.assertEqual(test_account.pay_ticket(1000, test_user.auth_code), 1000)
        # Check the Expiration of Limited Card:
        with self.assertRaises(ex.LimitedCardExpired):
            test_account.pay_ticket(100, test_user.auth_code)
        # Check the enough account balance for payticket:
        test_user2 = User("Hamid", "Rezaei", "0006056719", "myPass123", "09122224444")
        test_account2 = LimitedCard(test_user2, 2000, 1)
        with self.assertRaises(ex.NotEnoughBalance):
            test_account2.pay_ticket(3000, test_user2.auth_code)
        # Check the correct Authentication Code for payticket:
        with self.assertRaises(ex.PayTicketError):
            test_account2.pay_ticket(1000, 'wrong_authcode')


class TestSingleCard(unittest.TestCase):
        
    def test_singlecard_creation(self):
        # A User with an National ID Number can have only one SingleCard:
        test_user = User("Hamid", "Rezaei", "8826652000", "myPass123", "09122224444")
        test_account = BankAccount(test_user, 1000000)
        test_card = SingleCard(test_user)
        self.assertRaises(ex.InstantiateError, SingleCard, test_user)
    
    def test_singlecard_instantiation(self):
        # Check the new SingleCard instantiate correctly:
        test_user = User("Hamid", "Rezaei", "5123426799", "myPass123", "09122224444")
        test_account = BankAccount(test_user, 1000000)
        test_card = SingleCard(test_user)
        self.assertEqual(test_card.owner, test_user)
    
    def test_singlecard_owner(self):
        # Check the owner be an user object:
        self.assertRaises(ex.OwnerInstanceError, SingleCard, "test_user")
            
    def test_singlecard_payticket(self):
        # Check pay_ticket method:
        test_user = User("Hamid", "Rezaei", "8176051019", "myPass123", "09122224444")
        test_account = SingleCard(test_user)
        self.assertEqual(test_account.pay_ticket(test_user.auth_code), True)
        # Check the correct Authentication Code for payticket:
        with self.assertRaises(ex.PayTicketError):
            test_account.pay_ticket('wrong_authcode')

class TestTrip(unittest.TestCase):
    
    def test_trip_instantiation(self):
        # Check the new tripinstantiate correctly:
        test_user = User("Hamid", "Rezaei", "5123111191", "myPass123", "09122224444")
        test_trip = Trip('origin', 'dest', 1000)
        self.assertEqual(test_trip.origin, 'origin')
        self.assertEqual(test_trip.destination, 'dest')
        self.assertEqual(test_trip.fare, 1000)
        
    def test_trip_record(self):
        # Check the new tripinstantiate correctly:
        test_user = User("Hamid", "Rezaei", "5123111190", "myPass123", "09122224444")
        self.assertTrue(Trip.record_trip('origin', 'dest', 1000, test_user.auth_code))

if __name__ == '__main__':
    unittest.main()