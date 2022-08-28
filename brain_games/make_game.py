"""Game making module."""


def make_game(game_function, user_name):
    """Do game levels iterations.

    Parameters:
    game_function -- function with game logics
    user_name -- user name
    """
    counter = 0
    while counter < 3:
        level_result = game_function(user_name)
        if level_result:
            counter += 1
            if counter == 3:
                print(f'Congratulations, {user_name}!')
        elif not level_result:
            break
