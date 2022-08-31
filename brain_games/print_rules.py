"""Module with games rules."""


def print_rules(game_name):
    """Prrint game rules."""
    if game_name == 'even':
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif game_name == 'calc':
        print('What is the result of the expression?')
    elif game_name == 'gcd':
        print('Find the greatest common divisor of given numbers.')
    elif game_name == 'progression':
        print('What number is missing in the progression?')
