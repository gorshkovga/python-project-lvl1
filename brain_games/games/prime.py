"""Game module."""

from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Check is number is prime or not.
    Arguments:
    number -- nuber for checking
    Returns:
    return logical answer
    """
    ind = 2
    while ind < number:
        if number % ind == 0:
            return False
        ind += 1
    return True if number > 1 else False


def make_question():
    """Make question and answer.

    Returns:
    return question, true answer
    """
    number = randint(0, 100)
    result = is_prime(number)
    return number, 'yes' if result else 'no'
