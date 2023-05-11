#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    if argc == 1:
        print("{} arguments.".format(argc - 1))
    elif argc == 1:
        print("{} argument:".format(argc - 1))
    elif argv > 1:
        print("{} arguments:".format(argc - 1))
    for i in range(argc - 1):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
