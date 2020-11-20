"""Să se scrie o funcție care primește ca parametru un șir de caractere care reprezintă calea către un fișer
 si returnează un dicționar cu următoarele cămpuri: full_path = calea absoluta catre fisier, file_size =
 dimensiunea fisierului in octeti, file_extension = extensia fisierului (daca are) sau "", can_read,
  can_write = True/False daca se poate citi din/scrie in fisier."""
import os
import sys
from pathlib import Path

path = "../../[SI]/clientA.py"


def my_function(path):
    dictionary = {}
    base_path = Path(__file__).parent
    full_path = (base_path / path).resolve()
    dictionary.update(full_path=full_path)
    dictionary.update(file_size=os.stat(full_path)[6])
    dictionary.update(file_extension=os.path.splitext(full_path)[1])
    dictionary.update(can_read=os.access(full_path, os.R_OK))
    dictionary.update(can_write=os.access(full_path, os.W_OK))
    return dictionary


print(my_function(path))
