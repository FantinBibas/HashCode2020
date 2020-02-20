#!/usr/bin/env python3

import sys


def algo(books, days, librairies):
    parsed = []
    i = 0
    for library in librairies:
        books = set(library['books']).difference(set(parsed))
        print('{} {}'.format(i, len(books)))
        print(' '.join(books))
        parsed += books
        i += 1


def parse_file(lines):
    books_nbr, libraries_nbr, days = map(int, lines[0].split())
    books = map(int, lines[1].split())
    libraries = []
    lines = lines[2:]
    l = len(lines)
    for i in range(0, l, 2):
        library_param = map(int, lines[i].split())
        library_books = map(int, lines[i + 1].split())
        libraries.append({"param": library_param, "books": library_books})
    return books_nbr, books, libraries_nbr, days, libraries


def main(argv):
    if len(argv) != 2:
        return 1
    with open(argv[1]) as file:
        input_data = file.readlines()
        books, _, _, days, libraries = parse_file(input_data)
        algo(books, days, libraries)
    return 0


if __name__ == '__main__':
    exit(main(sys.argv))
