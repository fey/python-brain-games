import random

from brain_games.engine import run_game, ROUNDS_COUNT

DESCRIPTION = 'What is the result of the expression?'


def calc(n1, n2, operator):
    match operator:
        case '+':
            return n1 + n2
        case '-':
            return n1 - n2
        case '*':
            return n1 * n2
        case _:
            raise ValueError(f"Invalid operator: {operator}")


def build_round():
    n1 = random.randint(10, 15)
    n2 = random.randint(5, 10)
    operators = ["+", "-", "*"]
    operator = random.choice(operators)
    question = f"{n1} {operator} {n2}"
    answer = str(calc(n1, n2, operator))

    return (question, answer)


def start_calc():
    i = 0

    rounds = []

    while (i < ROUNDS_COUNT):
        round = build_round()
        rounds.append(round)
        i += 1

    run_game(DESCRIPTION, rounds)
