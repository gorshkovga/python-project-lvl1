#!/usr/bin/env python3
"""Main module."""

from games.game_even import game, RULES
from games.make_game import make_game


def main():
    """Call functions from other modules."""
    make_game(game, RULES)


if __name__ == '__main__':
    main()
