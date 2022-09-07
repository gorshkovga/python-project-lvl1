"""Game module."""


from brain_games.check_answer import check_answer
from brain_games.make_progression import make_progression
from prompt import string


def game(user_name):
    """Do game.

    Parameters:
    user_name -- user name
    Returns:
    return logical result of level passing
    """
    (true_answer, question) = make_progression()
    print(f'Question: {question}')
    answer = string('Your answer: ')
    return check_answer(user_name, answer, true_answer)
