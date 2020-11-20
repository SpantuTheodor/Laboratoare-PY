"""Să se scrie o funcție care are același comportament ca funcția de la exercițiul anterior, cu diferența
 că primește un parametru în plus: o funcție callback, care primește un parametru, iar pentru fiecare
  eroare apărută în procesarea fișierelor, se va apela funcția respectivă cu instanța excepției ca parametru"""

import os

target = os.path.join("D:\\", "[Faculty]", "III1", '[PY]', 'Laborator33')
to_search = "Bine"


def callback(e):
    return e


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
        try:
            raise Exception("Invalid target file/folder")
        except Exception as e:
            return callback(e)


print(my_function(target, to_search))
