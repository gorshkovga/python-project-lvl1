#!/usr/bin/env python3
"""Main module."""

import brain_games.games.gcd as game_module
from brain_games.run_game import run_game


def main():
    """Call functions from other module."""
    run_game(game_module)


if __name__ == '__main__':
    main()
