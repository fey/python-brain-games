import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(n):
    return n % 2 == 0


def build_round():
    question = random.randint(1, 100)
    answer = 'yes' if is_even(question) else 'no'

    return (question, answer)
