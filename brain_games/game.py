"""Game module"""

from random import randint
from prompt import string
from brain_games.is_even import is_even

def game(name):
    """Do game."""
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        number = randint(0, 100)
        print(f'Question: {number}')
        answer = string('Your answer: ')
        even_answer = is_even(number)
        if answer == even_answer:
            print('Correct!')
            counter += 1
            if counter == 3:
                print(f'Congratulations, {name}!')
        elif answer != even_answer:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was '{even_answer}'.
Let's try again, {name}!""")
            break
