"""Game module."""


from random import randint
from prompt import string

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

def game():
    """Do game and make question.

    Parameters:
    Returns:
    return true answer
    """
    number = randint(0, 100)  # noqa: S311
    print(f'Question: {number}')
    true_answer = 'yes' if (number % 2 == 0) else 'no'
    return true_answer
