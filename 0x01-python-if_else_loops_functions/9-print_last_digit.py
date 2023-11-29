#!/usr/bin/python3
def print_last_digit(number):
    ld = 0
    if number < 0:
        number *= -1
        ld = 1
        last_digit = number % 10
        if ld == 1:
            number *= -1
        print("{:d}".format(last_digit), end="")
        return last_digit
