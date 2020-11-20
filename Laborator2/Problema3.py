"""Write a function that receives as parameters two lists a and b and returns:
 (a intersected with b, a reunited with b, a - b, b - a)"""

array1 = [86, 42, 6, 46, 8, 4]
array2 = [6, 5, 8, 16, 4]


def operations(array1, array2) -> tuple:
    set1 = set(array1)
    set2 = set(array2)
    result = ()
    result += tuple(set1.intersection(set2))
    result += tuple(set1.union(set2))
    result += tuple(set1 - set2)
    result += tuple(set2 - set1)

    return result


print(operations(array1, array2))
