#!/usr/bin/env python3

import sys


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
        library_books = list(set(list(map(int, lines[i + 1].split()))))
        library_param[0] = len(library_books)
        libraries.append([library_param, library_books])
    return books_nbr, books, libraries_nbr, days, libraries


def algo_books(libraries):
    books = {}
    for library in libraries:
        for book in library[1][1]:
            if book not in books.keys():
                books[book] = []
            books[book].append(library[0])
    return


def score(books, library):
    s = 0
    for book in library[1][1]:
        s += books[book]
    return s * library[1][0][2]


def score2(books, days, library):
    days -= library[1][0][1]
    libbooks = sorted(library[1][1], key=lambda x: books[x])
    if len(libbooks) / library[1][0][2] > days:
        offset = max(0, len(libbooks) - days * library[1][0][2])
        libbooks = libbooks[offset:]
    s = 0
    for book in libbooks:
        s += books[book]
    return s


def algo(books, days, libraries):
    parsed = []
    libs_out = []
    # known = []
    libraries = [list(enum) for enum in enumerate(libraries)]
    # libraries = sorted(libraries, key=lambda x: score2(books, days, x) / x[1][0][1], reverse=True)
    # tmp = libraries[::]
    # while len(tmp) > 0:
    #     library = max(tmp, key=lambda x: score2(books, days, x) / x[1][0][1])
    #     tmp.remove(library)
    #     library[1][1] = list(set(library[1][1]).difference(set(known)))
    #     # library[1][1] = sorted(library[1][1], key=lambda x: books[x])
    #     known += library[1][1]
    #     library[1][0][0] = len(library[1][1])
    # libraries = sorted(libraries, key=lambda x: score2(books, days, x) / x[1][0][1], reverse=True)
    while len(libraries) > 0:
        library = max(libraries, key=lambda x: score2(books, days, x) / x[1][0][1])
        libraries.remove(library)
        if library[1][0][0] == 0:
            continue
        books_to_parse = sorted(list(set(library[1][1]).difference(set(parsed))), key=lambda x: books[x])
        dayst = days - library[1][0][1]
        if len(books_to_parse) / library[1][0][2] > dayst:
            offset = max(0, len(books_to_parse) - dayst * library[1][0][2])
            books_to_parse = books_to_parse[offset:]
        if len(books_to_parse) == 0:
            continue
        days = dayst
        libs_out.append(('{} {}'.format(library[0], len(books_to_parse)), ' '.join([str(book) for book in books_to_parse])))
        parsed += books_to_parse
    print(len(libs_out))
    for item in libs_out:
        print(item[0])
        print(item[1])


def main(argv):
    if len(argv) != 2:
        return 1
    with open(argv[1]) as file:
        input_data = file.readlines()
        _, books, _, days, libraries = parse_file(input_data)
        algo(books, days, libraries)
    return 0


if __name__ == '__main__':
    exit(main(sys.argv))
