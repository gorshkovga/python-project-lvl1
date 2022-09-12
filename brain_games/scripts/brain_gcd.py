#!/usr/bin/env python3
"""Main module."""

import brain_games.games.gcd as game_module
from brain_games.engine import run


def main():
    """Call functions from other module."""
    run(game_module)


if __name__ == '__main__':
    main()
