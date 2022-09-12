#!/usr/bin/env python3
"""Main module."""

from brain_games.games import gcd
from brain_games.engine import run


def main():
    """Call functions from other module."""
    run(gcd)


if __name__ == '__main__':
    main()
