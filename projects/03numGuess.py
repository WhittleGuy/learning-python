#!bin/bash/python

################################################################################
# Programmer: Brandon Whittle
# File: numGuess.py
# Purpose: Practice Python fundamentals
# Date: January 29, 2022
################################################################################

import random

MAX = 100


def main():
    choice = -1
    NUMBER = random.randint(1, MAX)

    while not choice == NUMBER:
        choice = int(input(f"Pick a number between 1 and {MAX}: "))
        if choice < 1 or choice >= MAX:
            print('Invalid choice.')
        if choice < NUMBER:
            print(f"{choice} is less than the number")
        elif choice > NUMBER:
            print(f"{choice} is greater than the number")

    print(f"You got it! The number was {NUMBER}")


if __name__ == '__main__':
    main()
