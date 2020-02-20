#!/usr/bin/env python3

import sys


def main(argv):
    if len(argv) != 2:
        return 1
    with open(argv[1]) as file:
        input_data = file.readlines()
        # TODO
    return 0


if __name__ == '__main__':
    exit(main(sys.argv))
