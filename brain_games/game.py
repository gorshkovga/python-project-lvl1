"""Game module."""

from random import randint

from brain_games.is_even import is_even
from prompt import string


def game(name):
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
        even_answer = is_even(number)
        if answer == even_answer:
            print('Correct!')
            counter += 1
            if counter == 3:
                print(f'Congratulations, {name}!')
        elif answer != even_answer:
            # avoiding linter error :)
            long_message = (
                f"'{answer}' is wrong answer ;(. "
                +  # noqa: W503, W504
                f"Correct answer was '{even_answer}'."
            )
            print(long_message)
            print(f"Let's try again, {name}!")
            break
