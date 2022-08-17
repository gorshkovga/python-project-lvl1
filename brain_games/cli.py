"""Module with greeting function."""
import prompt


def welcome_user():
    """Ask username and print greeting."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
