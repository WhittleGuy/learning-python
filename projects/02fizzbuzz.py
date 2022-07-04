#!bin/bash/python

################################################################################
# Programmer: Brandon Whittle
# File: fizzbuzz.py
# Purpose: Practice Python fundamentals
# Date: January 29, 2022
################################################################################


def main():
  nums = [i for i in range(0,101)]
  for num in nums:
    if num % 15 == 0: print('fizzbuzz')
    elif num % 5 == 0: print('buzz')
    elif num % 3 == 0: print('fizz')
    else: print(num)
  return

if __name__ == '__main__':
  main()