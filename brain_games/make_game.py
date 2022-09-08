"""Game making module."""
from prompt import string


def make_game(game_function, rules):  # noqa: WPS210
    """Do game levels iterations.

    Parameters:
    game_function -- function with game logics
    rules -- game rules
    """
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print(rules)
    LEVELS = 3
    counter = 0
    while counter < LEVELS:
        true_answer = game_function()
        user_answer = string('Your answer: ')
        level_result = (user_answer == true_answer)
        if level_result:
            print('Correct!')
            counter += 1
            if counter == 3:
                print(f'Congratulations, {name}!')
        elif not level_result:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                +  # noqa: W503, W504
                f"Correct answer was '{true_answer}'."
            )
            print(f"Let's try again, {name}!")
            break
