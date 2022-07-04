#!/bin/python

################################################################################
# Programmer: Whittle
# File: str_shift.py
# Purpose: Take a string and shift the letters by one pos
# Date: February 27, 2022
################################################################################

def main():
    # Given username
    username = 'AbeSimp'

    # Want temp pass to be username with letters shifted to right
    password = ''
    # Loop through letters by index
    for i in range(len(username)):
        # Concatenate prev letter into string
        password += username[i-1]

    # print or return shifted string
    print(password)


if __name__ == '__main__':
    main()
