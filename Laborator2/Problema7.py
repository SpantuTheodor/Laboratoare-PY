"""Write a function that receives as parameter a list of numbers (integers) and will return a
tuple with 2 elements. The first element of the tuple will be the number of palindrome numbers found in
 the list and the second element will be the greatest palindrome number."""

list = [121, 100, 22, 154, 51, 4, 1221, 23, 23, 54, 44, 3003]


def count_palindrom_max_palindrom(list):
    max = list[0]
    array = []

    for index in range(len(list)):
        aux = str(list[index])
        if aux == aux[::-1]:
            array.append(aux)
            if max < len(aux):
                max = len(aux)
        result = (len(array), max)
    return result


print(count_palindrom_max_palindrom(list))
