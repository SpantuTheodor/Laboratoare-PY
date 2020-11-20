"""Write a function that receives as parameters two lists a and b and returns a list of sets
containing: (a intersected with b, a reunited with b, a - b, b - a)"""

a = ['a', 'b', 'c', 'd', 'e']
b = ['c', 'd', 'e', 'f']


def set_operations(a , b):
    aux_a = set(a)
    aux_b = set(b)
    aux = [aux_a.intersection(aux_b), aux_a.union(aux_b), aux_a-aux_b, aux_b-aux_a]
    return aux


print(set_operations(a, b))