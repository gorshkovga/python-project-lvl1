"""Equation generator module."""

from random import choice, randint


def make_equation():
    """Make random equation.

    Returns:
    return equation
    """
    number_one = randint(0, 100)  # noqa: S311
    number_two = randint(0, 100)  # noqa: S311
    operations = (' + ', ' - ', ' * ')
    return str(number_one) + choice(operations) + str(number_two)  # noqa: S311
