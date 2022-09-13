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
    for num in range(number)[2:]:
        if number % num == 0:
            return False
    return True if number > 1 else False


def generate_question_and_answer():
    """Generate question and answer.

    Returns:
    return question, true answer
    """
    number = randint(1, 100)
    return number, 'yes' if is_prime(number) else 'no'
