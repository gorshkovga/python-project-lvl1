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
    if number <= 1:
        return False
    for num in range(2, number):
        if number % num == 0:
            return False
    return True


def generate_question_and_answer():
    """Generate question and answer.

    Returns:
    return question, correct answer
    """
    number = randint(0, 100)
    return number, 'yes' if is_prime(number) else 'no'
