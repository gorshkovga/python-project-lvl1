#!/usr/bin/env python3
"""Main module."""

from brain_games.game_calc import game
from brain_games.greeting import great_user


def main():
    """Call functions from other modules."""
    user_name = great_user()
    game(user_name)


if __name__ == '__main__':
    main()
