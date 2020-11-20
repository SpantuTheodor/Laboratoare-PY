"""Să se scrie o funcție ce returnează o listă cu extensiile unice a fișierelor din directorul dat ca
 argument la linia de comandă (nerecursiv). Lista trebuie să fie sortată crescător.
Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’, iar ‘fisier’ nu are extensie, deci nu va apărea în lista finală. """

import os

path_to_dir = str(input())


def printare(path_to_dir):
    result = set()
    for index in os.listdir(path_to_dir):
        result.add(os.path.splitext(index)[1])
    sorted(result, key=None, reverse=False)
    for x in result:
        print(x[1:])


printare(path_to_dir)
