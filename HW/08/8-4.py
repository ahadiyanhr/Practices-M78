
class DiscountError(Exception):
    """DiscountError raised for errors in the input.

    Attributes:
        result -- the result which caused the error
        message -- explanation of the error
    """

    def __init__(self, result, message="The Result must be bigger than zero"):
        self.result = result
        self.message = message

    def __str__(self):
        return f'{self.message}'


def apply_discount(price: int, discount: float) -> int:
    '''This Function Calculated the Final Price'''
    result = int(price * (1 - discount))
    print(result)
    if not 0 <= result <= price:
        raise DiscountError(result)
    return result


apply_discount(10,-0.1)