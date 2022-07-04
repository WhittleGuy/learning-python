#!/bin/python

################################################################################
# Programmer: Whittle
# File: template.py
# Purpose: Template for python programs
# Date: February 26, 2022
################################################################################

def main():
    def common_letters(str1, str2):
        com = []
        for letter in str1:
            if letter in str2 and not letter in com:
                com.append(letter)
        return com

    print(common_letters('banana', 'cream'))


if __name__ == '__main__':
    main()
