"""Game module."""


from random import choice, randint

RULES = 'What is the result of the expression?'


def make_question():
    """Make question and unswer.

    Returns:
    return question, true answer
    """
    number_one = randint(0, 100)
    number_two = randint(0, 100)
    operations = '+-*'
    operation = choice(operations)
    equation = (
        str(number_one) + operation.center(3) + str(number_two)
    )
    if operation == '+':
        result = number_one + number_two
    elif operation == '-':
        result = number_one - number_two
    else:
        result = number_one * number_two
    return equation, str(result)
