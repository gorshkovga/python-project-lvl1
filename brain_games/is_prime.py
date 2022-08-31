"""Prime cheking module."""


def is_prime(number):
    """Check number for prime.

    Parameters:
    number -- number for checking
    Returns:
    return string 'yes' or 'no'
    """
    ind = 2
    while ind < number:
        if number % ind == 0:
            return 'no'
        ind += 1
    return 'yes'
