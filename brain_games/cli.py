"""Empty docstring."""

import prompt


def welcome_user():
    """Return welcome message with username."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
