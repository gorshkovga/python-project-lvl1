"""Game module."""

from random import randint

RULES = 'What number is missing in the progression?'


def make_question():
    """Make question and answer.

    Returns:
    return question, true answer
    """
    start = randint(0, 100)
    step = randint(1, 10)
    length = randint(5, 15)
    hidden_member_index = randint(1, length)
    ind = 1
    progression = ''
    for ind in range(length):
        if ind == hidden_member_index:
            progression = f'{progression} ..'
            hidden_member = str(start + (ind - 1) * step)
        else:
            member = str(start + (ind - 1) * step)
            progression = f'{progression} {member}'
    return progression.strip(), hidden_member
