"""Game making module."""
from prompt import string


def make_game(game_function, RULES):
    """Do game levels iterations.

    Parameters:
    game_function -- function with game logics
    rules -- game rules
    """
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print(RULES)

    counter = 0
    while counter < 3:
        true_answer = game_function()
        user_answer = string('Your answer: ')
        level_result = (user_answer == true_answer)
        if level_result:
            print('Correct!')
            counter += 1
            if counter == 3:
                print(f'Congratulations, {name}!')
        elif not level_result:
            long_message = (
                f"'{user_answer}' is wrong answer ;(. "
                +  # noqa: W503, W504
                f"Correct answer was '{true_answer}'."
            )
            print(long_message)
            break
