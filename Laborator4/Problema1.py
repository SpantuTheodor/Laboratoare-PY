"""Să se scrie o funcție ce primeste un singur parametru, director, ce reprezintă calea către un director.
Funcția returnează o listă cu extensiile unice sortate crescator (in ordine alfabetica) a fișierelor din
 directorul dat ca parametru."""

import os


def printare():
    result = set()
    for index in os.listdir("../../[SI]"):
        result.add(os.path.splitext(index)[1])
    for x in result:
        print(x[1:])


printare()
