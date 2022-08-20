"""Answer cheking module."""


def check_answer(user_name, user_answer, true_answer):
    """Compare user's answer with target..

    Parameters:
    user_answer -- user answer
    true_answer -- game answer
    Returns:
    return True or False
    """
    if user_answer == true_answer:
        print('Correct!')
        return True
    # avoiding linter error :)
    long_message = (
        f"'{user_answer}' is wrong answer ;(. "
        +  # noqa: W503, W504
        f"Correct answer was '{true_answer}'."
    )
    print(long_message)
    print(f"Let's try again, {user_name}!")
    return False
