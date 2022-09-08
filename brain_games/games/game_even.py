"""Game module."""


from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def game():
    """Do game and make question.

    Returns:
    return question, true answer
    """
    number = randint(0, 100)  # noqa: S311
    return number, 'yes' if (number % 2 == 0) else 'no'
