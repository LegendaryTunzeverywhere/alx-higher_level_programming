#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    total = number % (-10)
else:
    total = number % 10

    if total > 5:
        print("Last digit of {} is {} and is greater than 5"
                .format(number, total))
    elif total == 0:
        print("Last digit of {} is {} and is 0"
                .format(number, total))
    else:
        print("Last digit of {} is {} and is less than 6 and not 0"
                .format(number, total))
