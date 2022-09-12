#!/usr/bin/env python3
"""Main module."""

from brain_games.games import prime
from brain_games.engine import run


def main():
    """Call functions from other module."""
    run(prime)


if __name__ == '__main__':
    main()
