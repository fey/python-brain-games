import prompt

ROUNDS_COUNT = 3


def run_game(description, build_round):
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("Welcome to the Brain Games!")
    print(description)

    for _ in range(ROUNDS_COUNT):
        (question, answer) = build_round()

        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ')

        if (user_answer == answer):
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
