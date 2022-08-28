"""GCD finder module."""


def find_gcd(number_one, number_two):
    """Find GCD for two numbers.

    Parameters:
    number_one and number_two -- numbers for GCD finding
    Returns:
    return GCD as string
    """
    min_number = min(number_one, number_two)
    max_number = max(number_one, number_two)
    if max_number % min_number == 0:
        return str(min_number)
    return find_gcd(min_number, max_number % min_number)
