"""Să se scrie o funcție ce primește ca argumente două căi: director si fișier.
Implementati functia astfel încât în fișierul de la calea fișier să fie scrisă pe câte o linie, calea
absolută a fiecărui fișier din interiorul directorului de la calea folder, ce incepe cu litera A. """

import os


def abs_path_write_in_file():
    path = os.path.join("D:\\", "[Faculty]", "III1", "[PY]", "Laborator4")
    f = open("auxiliar.txt", "w")
    for index in os.listdir(path):
        index_path = os.path.join(path, index)
        f.write(index_path)
        f.write("\n")
    f.close()


abs_path_write_in_file()
