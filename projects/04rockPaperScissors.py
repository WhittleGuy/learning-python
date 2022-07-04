#!bin/bash/python

################################################################################
# Programmer: Brandon Whittle
# File: rockPaperScissors.py
# Purpose: Practice Python fundamentals
# Date: January 29, 2022
################################################################################

# Imports
import random

# Definitions


def parseChoice(choice):
    """Parse the user choice into an easy to handle number"""
    if choice == '1' or choice.lower() == 'rock':
        return 1
    elif choice == '2' or choice.lower() == 'paper':
        return 2
    elif choice == '3' or choice.lower() == 'scissors':
        return 3
    elif choice == '4' or choice.lower() == 'quit':
        return 4
    else:
        return -1


def wordifyChoice(choice):
    """Take a numbered choice and return the associated string"""
    if choice == 1:
        return 'rock'
    elif choice == 2:
        return 'paper'
    elif choice == 3:
        return 'scissors'


def main():
    """Main loop (read: game)"""
    # Prompt user for choice
    choice = 0
    print('Please select a choice:')
    print('1. Rock')
    print('2. Paper')
    print('3. Scissors')
    print('4. Quit')

    # Get user input and validate
    while choice < 1 or choice > 4:
        choice = parseChoice(input('Your choice: '))
        # Check choice validity
        if choice < 1 or choice > 4:
            print('Invalid choice. Pick again')
      # Quit condition
    if choice == 4:
        return

    # Get computer choice
    compChoice = random.choice([1, 2, 3])

    if choice == compChoice:
        print('[Stalemate] You both chose ' + wordifyChoice(choice))
    elif choice - compChoice == -1 or choice - compChoice == 2:
        print('[Loss] Your choice: ' + wordifyChoice(choice) +
              ' Computer Choice: ' + wordifyChoice(compChoice))
    else:
        print('[Win] Your choice: ' + wordifyChoice(choice) +
              ' Computer Choice: ' + wordifyChoice(compChoice))
    return


if __name__ == '__main__':
    main()
