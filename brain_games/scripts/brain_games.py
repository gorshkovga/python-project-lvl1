#!/usr/bin/env python3
"""Main module."""

from brain_games.cli import welcome_user


def main():
    """Call functions from other modules."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
