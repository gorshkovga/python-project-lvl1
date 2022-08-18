"""Even cheking module."""

def is_even(number):
    """Check for even parity"""
    res = (number % 2 == 0)
    if res:
        return 'yes'
    else:
        return 'no'
