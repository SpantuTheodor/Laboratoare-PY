"""Write a function that receives as a parameter a variable number of lists and a whole
 number x. Return a list containing the items that appear exactly x times in the incoming lists. """

n = int(input())
list = [1, 1, 2, 1, 5, 4, 1, 2, 2, 5, 4, 3]


def only_n_times(list, n):
    result = []
    for index in list:
        if list.count(index) == n:
            if result.count(index) == 0:
                result.append(index)
    return result


print(only_n_times(list, n))
