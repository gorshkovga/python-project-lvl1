"""Game module."""

from random import randint

from brain_games.check_answer import check_answer
from brain_games.is_even import is_even
from prompt import string


def game(user_name):
    """Do game.

    Parameters:
    name -- user name
    """
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        number = randint(0, 100)  # noqa: S311
        print(f'Question: {number}')
        answer = string('Your answer: ')
        true_answer = is_even(number)
        check_result = check_answer(user_name, answer, true_answer)
        if check_result:
            counter += 1
            if counter == 3:
                print(f'Congratulations, {user_name}!')
        elif not check_result:
            break
