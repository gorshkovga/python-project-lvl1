"""Game module."""

from random import randint

from brain_games.check_answer import check_answer
from brain_games.is_even import is_even
from prompt import string


def game(user_name):
    """Do game.

    Parameters:
    user_name -- user name
    """
    number = randint(0, 100)  # noqa: S311
    print(f'Question: {number}')
    answer = string('Your answer: ')
    true_answer = is_even(number)
    check_result = check_answer(user_name, answer, true_answer)
    return check_result
