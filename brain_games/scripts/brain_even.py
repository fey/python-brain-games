import random

from .engine import run_game, ROUNDS_COUNT

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

def is_even(n):
    return n % 2 == 0


def build_round():
    question = random.randint(1, 100)
    answer = 'yes' if is_even(question) else 'no'

    return (question, answer)


def start_even():
    i = 0

    rounds = []

    while (i < ROUNDS_COUNT):
        round = build_round()
        rounds.append(round)
        i += 1

    run_game(DESCRIPTION, rounds)


def main():
    start_even()


if __name__ == '__main__':
    main()
