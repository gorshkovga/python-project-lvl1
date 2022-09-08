"""Game making module."""
from prompt import string


def make_game(game_module):
    """Do game levels iterations.

    Parameters:
    game_module -- module with game logics and attributes
    """
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_module.RULES)
    LEVELS = 3
    counter = 0
    while counter < LEVELS:
        question, true_answer = game_module.game()
        print(f'Question: {question}')
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
                + f"Correct answer was '{true_answer}'."  # noqa: W503
            )
            print(f"Let's try again, {name}!")
            break
