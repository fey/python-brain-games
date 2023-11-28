import prompt

ROUNDS_COUNT = 3


# NOTE: to fix max-line-length rule of flake8
def get_try_again_message(answer, user_answer):
    return f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'."


def run_game(description, rounds):
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("Welcome to the Brain Games!")
    print(description)

    for (question, answer) in rounds:
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ')

        if (user_answer == answer):
            print('Correct!')
        else:
            print(get_try_again_message())
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
