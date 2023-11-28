#!/usr/bin/env python3

import prompt


def greet():
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("Welcome to the Brain Games!")


def main():
    greet()


if __name__ == '__main__':
    main()
