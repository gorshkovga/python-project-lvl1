"""Game running module."""
from prompt import string

NUMBER_OF_LEVELS = 3


def run(game):
    """Run game levels iterations.

    Parameters:
    game -- module with game logics and attributes
    """
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)
    for _ in range(NUMBER_OF_LEVELS):
        question, correct_answer = game.generate_question_and_answer()
        print(f'Question: {question}')
        user_answer = string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
