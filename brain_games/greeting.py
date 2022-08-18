"""Module with greeting function."""
import prompt


def great_user():
    """Ask username and print greeting."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name