import random
import math

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def build_round():
    n1 = random.randint(1, 50)
    n2 = random.randint(1, 50)
    question = f"{n1} {n2}"
    answer = str(math.gcd(n1, n2))

    return (question, answer)
