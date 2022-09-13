"""Game module."""


from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_and_answer():
    """Generate question and answer..

    Returns:
    return question, correct answer
    """
    number = randint(0, 100)
    return number, 'yes' if (number % 2 == 0) else 'no'
