"""Even cheking module."""


def is_even(number):
    """Check for even parity.

    Parameters:
    number -- number for checking
    Returns:
    return string 'yes' or 'no'
    """
    res = (number % 2 == 0)
    if res:
        return 'yes'
    return 'no'
