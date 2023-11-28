import random
from brain_games.engine import run_game, ROUNDS_COUNT


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False

    return True


def build_round():

    number = random.randint(1, 100)
    question = str(number)

    answer = 'yes' if is_prime(number) else 'no'

    return (question, answer)


def start_prime():
    i = 0

    rounds = []

    while (i < ROUNDS_COUNT):
        round = build_round()
        rounds.append(round)
        i += 1

    run_game(DESCRIPTION, rounds)
