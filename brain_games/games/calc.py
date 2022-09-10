"""Game module."""


from random import choice, randint

RULES = 'What is the result of the expression?'


def game():
    """Do game and make question.

    Returns:
    return question, true answer
    """
    number_one = randint(0, 100)
    number_two = randint(0, 100)
    operations = (' + ', ' - ', ' * ')
    equation = (
        str(number_one) + choice(operations) + str(number_two)
    )
    return equation, str(int(eval(equation)))
