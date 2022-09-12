"""Game running module."""
from prompt import string


def run(game, number_of_levels=3):
    """Run game levels iterations.

    Parameters:
    game -- module with game logics and attributes
    """
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)
    for _ in range(number_of_levels):
        question, true_answer = game.make_question()
        print(f'Question: {question}')
        user_answer = string('Your answer: ')
        if user_answer == true_answer:
            print('Correct!')
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                + f"Correct answer was '{true_answer}'."  # noqa: W503
            )
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
