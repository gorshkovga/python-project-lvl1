#!/usr/bin/env python3
"""Main module."""

from brain_games.game_even import game
from brain_games.greeting import great_user
from brain_games.make_game import make_game
from brain_games.print_rules import print_rules


def main():
    """Call functions from other modules."""
    user_name = great_user()
    print_rules('even')
    make_game(game, user_name)


if __name__ == '__main__':
    main()
