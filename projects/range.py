#!/bin/python

################################################################################
# Programmer: Whittle
# File: range.py
# Purpose: Allie needs to understand range(len(var))
# Date: February 27, 2022
################################################################################

def main():
    # Your code here

    # Prints 0 -> end - 1
    for i in range(5):
        print(i)

    print('------')

    str = 'string'
    # Prints the length of the *iterable* variable
    print(len(str))

    print('------')

    # "len(variable)" -> number of items in variable
    # "range(end)" -> 0 to end -1
    # "range(len(var))" -> 0 to number of items in var - 1
    for i in range(len(str)):
        print(i)

    print('------')

    # Prints the item at the given index of the variable
    for i in range(len(str)):
        print(str[i])

    print('------')

    for index, l in enumerate(str):
        print(f'{index}: {l}')


if __name__ == '__main__':
    main()
