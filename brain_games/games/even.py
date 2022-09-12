"""Game module."""


from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_question_and_answer():
    """Make question and answer..

    Returns:
    return question, true answer
    """
    number = randint(0, 100)
    return number, 'yes' if (number % 2 == 0) else 'no'
