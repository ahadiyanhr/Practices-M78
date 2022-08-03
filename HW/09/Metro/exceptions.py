class IDNumberError(ValueError):
    pass

class PasswordError(ValueError):
    pass

class PhoneError(ValueError):
    pass

class InstantiateError(UserWarning):
    pass

class AccountBalanceError(ValueError):
    pass

class OwnerInstanceError(TypeError):
    pass

class AuthenticationCodeError(ValueError):
    pass

class NotEnoughBalance(ValueError):
    pass

class IsNotBankAccount(TypeError):
    pass

class AccountNotExist(LookupError):
    pass

class DepositeError(Exception):
    pass

class WithdrawError(Exception):
    pass
class TransferingError(Exception):
    pass

class CardBalanceError(ValueError):
    pass