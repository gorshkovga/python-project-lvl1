#!/usr/bin/env python3
"""Main module."""

from brain_games.game import game
from brain_games.greeting import great_user


def main():
    """Call functions from other modules."""
    name = great_user()
    game(name)


if __name__ == '__main__':
    main()
