"""Game module."""

from random import randint

RULES = 'What number is missing in the progression?'


def game():
    """Do game.

    Returns:
    return true answer
    """
    def make_progression():  # noqa: WPS210
        """Make random arithmetic progression.

        Returns:
        return hidden progression member
        """
        start = randint(0, 100)  # noqa: S311, WPS432
        step = randint(1, 10)  # noqa: S311, WPS432
        length = randint(5, 15)  # noqa: S311, WPS432
        hidden_member_index = randint(1, length)  # noqa: S311, WP432
        ind = 1
        progression = ''
        while ind <= length:
            if ind == hidden_member_index:
                progression = f'{progression} ..'
                hidden_member = str(start + (ind - 1) * step)
            else:
                member = str(start + (ind - 1) * step)
                progression = f'{progression} {member}'
            ind += 1
        return (hidden_member, progression.strip())

    (true_answer, question) = make_progression()
    print(f'Question: {question}')
    return true_answer
