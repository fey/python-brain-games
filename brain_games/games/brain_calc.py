import random

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
