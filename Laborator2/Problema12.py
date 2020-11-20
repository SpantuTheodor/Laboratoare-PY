"""Write a function that will receive a list of words  as parameter and will return a
 list of lists of words, grouped by rhyme. Two words rhyme if both of them end with the same 2 letters."""

list = ['ana', 'banana', 'carte', 'arme', 'parte', 'tabana', 'carne', 'caine']


def group_by_rhyme(list):
    list.sort(key=lambda item: item[-2:])

    print(list)

    cond1 = list[0][-2:]
    auxiliary = []
    result = []

    for index in range(len(list)):

        cond2 = list[index][-2:]
        if cond1 == cond2:
            auxiliary.append(list[index])
        else:
            result.append(auxiliary)
            auxiliary = [list[index]]
        if index == len(list) - 1 and cond1 == cond2:
            result.append(auxiliary)
        cond1 = cond2

    return result


print(group_by_rhyme(list))
