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