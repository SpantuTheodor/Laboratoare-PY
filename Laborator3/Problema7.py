"""Write a function that receives a variable number of sets and returns a dictionary with the following
 operations from all sets two by two: reunion, intersection, a-b, b-a. The key will have the following form:
  "a op b", where a and b are two sets, and op is the applied operator: |, &, -. """

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
set_c = {7, 8, 9, 10}


def set_operations_to_dict(**kwargs):
    dictionary = {}
    keys = []
    values = []
    for key in kwargs.keys():
        keys.append(key)
    for value in kwargs.values():
        values.append(value)
    print(keys, values)

    for index in range(len(keys)-1):
        for index2 in range(index + 1, len(keys)):
            dictionary[keys[index] + '&' + keys[index2]] = values[index].intersection(values[index2])
            dictionary[keys[index] + '|' + keys[index2]] = values[index].union(values[index2])
            dictionary[keys[index] + "/" + keys[index2]] = values[index] - values[index2]
            dictionary[keys[index2] + "/" + keys[index]] = values[index+1] - values[index]

    return dictionary


print(set_operations_to_dict(A=set_a, B=set_b, C=set_c))