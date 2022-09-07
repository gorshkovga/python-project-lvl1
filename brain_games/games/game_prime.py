"""Game module."""

from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game():
    """Do game.

    Returns:
    return true answer
    """
    number = randint(0, 100)  # noqa: S311
    print(f'Question: {number}')
    ind = 2
    while ind < number:
        if number % ind == 0:
            return 'no'
        ind += 1
    return 'yes' if number > 1 else 'no'
