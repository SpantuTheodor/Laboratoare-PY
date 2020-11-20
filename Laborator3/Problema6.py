"""Write a function that receives as a parameter a list and returns a tuple (a, b), representing the
 number of unique elements in the list, and b representing the number of duplicate elements in the list
  (use sets to achieve this objective)."""

string = "Ana has apples. and don't forget, Ana has apples."


def uniques_and_duplicates(string):
    aux_string = set(string)
    return len(aux_string), len(string) - len(aux_string)


print(uniques_and_duplicates(string))

