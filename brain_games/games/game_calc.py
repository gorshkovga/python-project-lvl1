"""Game module."""


from random import choice, randint

RULES = 'What is the result of the expression?'

def game():
    """Do game and make question.

    Returns:
    return true answer
    """
    number_one = randint(0, 100)  # noqa: S311
    number_two = randint(0, 100)  # noqa: S311
    operations = (' + ', ' - ', ' * ')
    equation = str(number_one) + choice(operations) + str(number_two)  # noqa: S311
    print(f'Question: {equation}')
    return str(int(eval(equation)))  # noqa: S307
