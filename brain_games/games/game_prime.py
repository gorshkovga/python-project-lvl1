"""Game module."""

from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game():
    """Do game.

    Returns:
    return question, true answer
    """
    number = randint(0, 100)
    ind = 2
    while ind < number:
        if number % ind == 0:
            return number, 'no'
        ind += 1
    return number, 'yes' if number > 1 else 'no'
