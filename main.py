#!/usr/bin/env python3

import sys


def algo(books, days, librairies):
    parsed = []
    i = -1
    libs_out = []
    for library in librairies:
        i += 1
        books_to_parse = list(set(library[1]).difference(set(parsed)))
        days -= library[0][1]
        if len(books_to_parse) > days:
            books_to_parse = books_to_parse[days * library[0][0]:]
        if len(books_to_parse) == 0:
            continue
        libs_out.append(('{} {}'.format(i, len(books_to_parse)), ' '.join([str(book) for book in books_to_parse])))
        parsed += books_to_parse
    print(len(libs_out))
    for item in libs_out:
        print(item[0])
        print(item[1])


def parse_file(lines):
    books_nbr, libraries_nbr, days = list(map(int, lines[0].split()))
    books = list(map(int, lines[1].split()))
    libraries = []
    lines = lines[2:]
    l = len(lines)
    for i in range(0, l, 2):
        if lines[i].strip() == "":
            continue
        library_param = list(map(int, lines[i].split()))
        library_books = list(map(int, lines[i + 1].split()))
        libraries.append((library_param, library_books))
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
