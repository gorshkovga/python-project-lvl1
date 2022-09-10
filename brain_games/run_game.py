"""Game running module."""
from prompt import string


def run_game(game, number_of_levels=3):
    """Run game levels iterations.

    Parameters:
    game -- module with game logics and attributes
    """
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)
    counter = 0
    while counter < number_of_levels:
        question, true_answer = game.game()
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
