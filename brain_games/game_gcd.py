"""Game module."""

from random import randint

from brain_games.check_answer import check_answer
from brain_games.find_gcd import find_gcd
from prompt import string


def game(user_name):
    """Do game.

    Parameters:
    user_name -- user name
    Returns:
    return logical result of level passing
    """
    number_one = randint(1, 100)  # noqa: S311
    number_two = randint(1, 100)  # noqa: S311
    print(f'Question: {number_one} {number_two}')
    answer = string('Your answer: ')
    true_answer = find_gcd(number_one, number_two)
    return check_answer(user_name, answer, true_answer)
