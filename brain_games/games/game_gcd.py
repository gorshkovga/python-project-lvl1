"""Game module."""

from random import randint

RULES = 'Find the greatest common divisor of given numbers.'

def game(user_name):
    """Do game.

    Parameters:
    user_name -- user name
    Returns:
    return logical result of level passing
    """
    number_one = randint(1, 100)  # noqa: S311
    number_two = randint(1, 100)  # noqa: S311
    print(f'Question: {number_one} {number_two}')
    return find_gcd(number_one, number_two)
