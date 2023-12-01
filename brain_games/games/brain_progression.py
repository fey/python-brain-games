import random

DESCRIPTION = 'What number is missing in the progression?'


def build_progression(start, step, length):

    progression = []
    for i in range(length):
        element = str(start + step * i)
        progression.append(element)

    return progression


def build_round():
    start = random.randint(1, 50)
    length = 10
    step = random.randint(1, 10)
    progression = build_progression(start, step, length)
    hiddenIndex = random.randint(0, length - 1)
    answer = str(progression[hiddenIndex])

    progression[hiddenIndex] = '..'
    question = str.join(" ", progression)

    return (question, answer)
