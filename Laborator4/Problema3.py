"""Să se scrie o funcție ce primește ca parametru un string my_path.
Dacă parametrul reprezintă calea către un fișier, se vor returna ultimele 20 de caractere din conținutul fișierului.
 Dacă parametrul reprezintă calea către un director, se va returna o listă de tuple (extensie, count), sortată
  descrescător după count, unde extensie reprezintă extensie de fișier, iar count - numărul de fișiere cu acea
   extensie. Lista se obține din toate fișierele (recursiv) din directorul dat ca parametru. """

import os
import operator
my_path = os.path.join("D:\\", "[Faculty]", "III1")


def is_dir(my_path, result):
    for index in os.listdir(my_path):
        new_path = os.path.join(my_path, index)
        if os.path.isdir(new_path):
            result = is_dir(new_path, result)
        else:
            result.append(index)
    return result


def my_function(my_path):
    if os.path.isfile(my_path):
        f = open(my_path, "r")
        result = f.read()
        f.close()
        return result[-21:len(result)]
    elif os.path.isdir(my_path):
        result = []
        result = is_dir(my_path, result)
        actual_result = {}
        for index in result:
            if os.path.splitext(index)[1] not in actual_result:
                actual_result[os.path.splitext(index)[1]] = index.count(os.path.splitext(index)[1])
            else:
                actual_result[os.path.splitext(index)[1]] = actual_result[os.path.splitext(index)[1]] + index.count(
                    os.path.splitext(index)[1])
        sorted_result = sorted(actual_result.items(), key=operator.itemgetter(1), reverse=True)
        return sorted_result


print(my_function(my_path))
