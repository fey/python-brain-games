import random

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
