import random
import math

from brain_games.engine import run_game, ROUNDS_COUNT

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def build_round():
    n1 = random.randint(1, 50)
    n2 = random.randint(1, 50)
    question = f"{n1} {n2}"
    answer = str(math.gcd(n1, n2))

    return (question, answer)


def start_gcd():
    i = 0

    rounds = []

    while (i < ROUNDS_COUNT):
        round = build_round()
        rounds.append(round)
        i += 1

    run_game(DESCRIPTION, rounds)
