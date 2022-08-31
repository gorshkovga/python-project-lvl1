"""Module with games rules."""


def print_rules(game_name):  # noqa: WPS231
    """Prrint game rules."""
    if game_name == 'even':  # noqa: WPS223
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif game_name == 'calc':
        print('What is the result of the expression?')
    elif game_name == 'gcd':
        print('Find the greatest common divisor of given numbers.')
    elif game_name == 'progression':
        print('What number is missing in the progression?')
    elif game_name == 'prime':
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
