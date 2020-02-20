#!/usr/bin/env python3

import sys


def parse_file(lines):
    books_nbr, libraries_nbr, days = map(int, next(lines).split())
    books = map(int, next(lines).split())
    libraries = []
    for line in lines:
        library_param = map(int, line.split())
        library_books = map(int, next(lines).split())
        libraries.append({"param": library_param, "books": library_books})
    return books_nbr, libraries_nbr, days, libraries


def main(argv):
    if len(argv) != 2:
        return 1
    with open(argv[1]) as file:
        input_data = file.readlines()
        # TODO
    return 0


if __name__ == '__main__':
    exit(main(sys.argv))
