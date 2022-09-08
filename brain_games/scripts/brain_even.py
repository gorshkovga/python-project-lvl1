#!/usr/bin/env python3
"""Main module."""

import brain_games.games.game_even as game_module
from brain_games.make_game import make_game


def main():
    """Call functions from other module."""
    make_game(game_module)


if __name__ == '__main__':
    main()
