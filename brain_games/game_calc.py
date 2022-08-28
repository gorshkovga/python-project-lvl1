"""Game module."""

from brain_games.check_answer import check_answer
from brain_games.make_equation import make_equation
from prompt import string


def game(user_name):
    """Do game.

    Parameters:
    user_name -- user name
    Returns:
    return logical result of level passing
    """
    equation = make_equation()
    print(f'Question: {equation}')
    answer = string('Your answer: ')
    true_answer = str(int(eval(equation)))  # noqa: S307
    return check_answer(user_name, answer, true_answer)
