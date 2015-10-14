#!/usr/bin/env python
"""
A simple FizzBuzz script
"""

import argparse

def fizzbuzz(number):
    """
    Fizzbuzzes a single number

    @param number
    @type int
    @returns A string, or an int
    """
    result = ""

    # If evenly divisible by 3, Fizz
    if not number % 3:
        result += "Fizz"
    # If evenly divisible by 5, Buzz
    elif not number % 5:
        result += "Buzz"

    return result or number

def parse_args():
    """
    Argument Parsing

    @returns A Namespace object conforming to the argparse paradigm
    """
    parser = argparse.ArgumentParser(description='Simple FizzBuzz.')

    parser.add_argument('max_num', metavar='N', type=int, help='Number to stop the fizzbuzz at')

    return parser.parse_args()

if __name__ == "__main__":
    ARGS = parse_args()

    for i in xrange(ARGS.max_num + 1):
        print fizzbuzz(i)
