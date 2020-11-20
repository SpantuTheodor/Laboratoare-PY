"""Să se scrie o funcție care primește ca argumente două șiruri de caractere, target și to_search și
returneaza o listă de fișiere care conțin to_search. Fișierele se vor căuta astfel: dacă target este
 un fișier, se caută doar in fișierul respectiv iar dacă este un director se va căuta recursiv in toate
  fișierele din acel director. Dacă target nu este nici fișier, nici director, se va arunca o excepție
   de tipul ValueError cu un mesaj corespunzator."""

import os

target = os.path.join("D:\\", "[Faculty]", "III1", '[PY]', 'Laborator3')
to_search = "Bine"


def is_dir(target, to_search):
    for index in os.listdir(target):
        new_path = os.path.join(target, index)
        if os.path.isdir(new_path):
            return is_dir(new_path, to_search)
        else:
            f = open(new_path, "r")
            result = f.read()
            f.close()
            if result.find(to_search) >= 0:
                return True
    return False


def my_function(target, to_search):

    if os.path.isfile(target):
        f = open(target, "r")
        result = f.read()
        f.close()
        if result.find(to_search):
            return True
        else:
            return False

    elif os.path.isdir(target):
        return is_dir(target, to_search)

    else:
        raise Exception("Invalid target file/folder")


print(my_function(target, to_search))
