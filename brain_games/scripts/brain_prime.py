#!/usr/bin/env python3
"""Main module."""

from brain_games.games.game_prime import RULES, game
from brain_games.make_game import make_game


def main():
    """Call functions from other modules."""
    make_game(game, RULES)


if __name__ == '__main__':
    main()


