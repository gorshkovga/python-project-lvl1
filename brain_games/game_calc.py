"""Game module."""

from brain_games.make_equation import make_equation
from brain_games.check_answer import check_answer
from prompt import string


def game(user_name):
    """Do game.

    Parameters:
    user_name -- user name
    """
    print('What is the result of the expression?')
    counter = 0
    while counter < 3:
        equation = make_equation()
        print(f'Question: {equation}')
        answer = string('Your answer: ')
        true_answer = str(int(eval(equation)))
        check_result = check_answer(user_name, answer, true_answer)
        if check_result:
            counter += 1
            if counter == 3:
                print(f'Congratulations, {user_name}!')
        elif not check_result:
            break
