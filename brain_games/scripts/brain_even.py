import prompt
import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

def is_even(n):
    return n % 2 == 0


def build_round():
    question = random.randint(1, 100)
    answer = 'yes' if is_even(question) else 'no'

    return (question, answer)


def start_even():
    (question, answer) = build_round()
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("Welcome to the Brain Games!")
    print(DESCRIPTION)
    print(f"Question: {question}")
    user_answer = prompt.string('Your answer: ')

    if (user_answer == answer):
        print('Correct!')
    else:
        print(f"'yes' is wrong answer ;(. Correct answer was 'no'.")
        print(f"Let's try again, {name}!")
        return

    print(f"Congratulations, {name}!")


def main():
    start_even()


if __name__ == '__main__':
    main()
