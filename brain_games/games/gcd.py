"""Game module."""

from random import randint

RULES = 'Find the greatest common divisor of given numbers.'


def find_gcd(number_one, number_two):
    """Find GCD for two numbers.

    Parameters:
    number_one and number_two -- numbers for GCD finding
    Returns:
    return GCD
    """
    min_number = min(number_one, number_two)
    max_number = max(number_one, number_two)
    if max_number % min_number == 0:
        return min_number
    return find_gcd(min_number, max_number % min_number)


def generate_question_and_answer():
    """Generate question and answer.

    Returns:
    return question, correct answer
    """
    number_one = randint(1, 100)
    number_two = randint(1, 100)
    return f'{number_one} {number_two}', str(find_gcd(number_one, number_two))
