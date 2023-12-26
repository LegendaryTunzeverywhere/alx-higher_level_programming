#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    index = printed_intgrs = 0
    while True:
        try:
            if index < x:
                print("{:d}".format(my_list[index]), end='')
                index += 1
                printed_intgrs += 1
            else:
                print()
                return printed_intgrs
        except (ValueError, TypeError):
            index += 1
