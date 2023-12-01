#!/usr/bin/env python3

from brain_games.games.brain_progression import DESCRIPTION, build_round
from brain_games.engine import run_game


def start_calc():
    run_game(DESCRIPTION, build_round)


def main():
    start_calc()


if __name__ == '__main__':
    main()
