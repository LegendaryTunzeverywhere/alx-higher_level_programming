#!/usr/bin/python3
def print_arg(argv):
    size = len(argv) - 1
    if size == 0:
        print("{:d} arguments.".format(size))
        return
    else:
        if size == 1:
            print("{:d} argument:".format(size))
        else:
            print("{:d} arguments:".format(size))
        a = 1
        while a <= size:
            print("{:d}: {:s}".format(a, argv[a]))
            a += 1

if __name__ == "__main__":
    import sys
    print_arg(sys.argv)
