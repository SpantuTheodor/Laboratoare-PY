"""Să se scrie o funcție ce primește un parametru cu numele dir_path. Acest parametru reprezintă calea
 către un director aflat pe disc. Funcția va returna o listă cu toate căile absolute ale fișierelor
  aflate în rădăcina directorului dir_path."""
import os
import sys
from pathlib import Path

dir_path = "../../[SI]"


def my_function(dir_path):
    result = []
    base_path = Path(__file__).parent
    full_path = (base_path / dir_path).resolve()
    print(full_path)
    for index in os.listdir(full_path):
        aux_path = (full_path / index).resolve()
        result.append(aux_path)
    return result


print(my_function(dir_path))
