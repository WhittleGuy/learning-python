#!bin/bash/python

from functools import lru_cache


@lru_cache(maxsize=1000000)
def fibonacci(n):
    if (type(n) != int or n < 1 or n > 10000):
        print('Invalid number')
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-2) + fibonacci(n-1)


def main():
    n = int(input('Enter a number: '))
    for num in range(1, n):
        fibonacci(num)
    print(fibonacci(n))


if __name__ == '__main__':
    main()
