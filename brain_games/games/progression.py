"""Game module."""

from random import randint

RULES = 'What number is missing in the progression?'


def generate_question_and_answer():
    """Generate question and answer.

    Returns:
    return question, correct answer
    """
    start = randint(0, 100)
    step = randint(1, 10)
    length = randint(5, 15)
    hidden_member_index = randint(0, length - 1)
    progression = []
    for ind in range(length):
        progression.append(str(start + ind * step))
    correct_answer = progression[hidden_member_index]
    progression[hidden_member_index] = '..'
    return ' '.join(progression), correct_answer
