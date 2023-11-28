import prompt

ROUNDS_COUNT = 3

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
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
