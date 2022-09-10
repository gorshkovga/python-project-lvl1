"""Game module."""

from random import randint

RULES = 'Find the greatest common divisor of given numbers.'


def make_question():
    """Make question and answer.

    Returns:
    return question, true answer
    """
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

    number_one = randint(1, 100)
    number_two = randint(1, 100)
    return f'{number_one} {number_two}', find_gcd(number_one, number_two)
