"""Compare two dictionaries without using the operator "==" and return a list of differences as
follows: (Attention, dictionaries must be recursively covered because they can contain other containers,
 such as dictionaries, lists, sets, etc.)"""


dictionary1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "codes": {
        "code1": 7,
        "code2": 53,
        "code3": "X AE A-12"
    },
    "condition": ["pretty good", "meh", "meh"],
    "size": (65, 43, 189, 5)
}

dictionary2 = {
    "brand": "Porsche",
    "model": "Mustang",
    "codes": {
        "code1": 7,
        "code2": 53,
        "code3": "X A A-12"
    },
    "condition": ["pretty good", "meh"],
    "size": (65, 4, 189, 5)
}


def compare_dictionaries(dictionary1, dictionary2):
    differences = []
    for index in dictionary1:
        if index not in dictionary2:
            differences.append(index)

        elif type(dictionary1[index]) == dict and type(dictionary2[index]) == dict:
            if compare_dictionaries(dictionary1[index], dictionary2[index]):
                differences.append(index)

        elif type(dictionary1[index]) == list and type(dictionary2[index]) == list:
            if dictionary1[index].sort != dictionary2[index].sort:
                differences.append(index)

        elif type(dictionary1[index]) == set and type(dictionary2[index]) == set:
            if dictionary1[index].intersection(dictionary2[index]) == dictionary2[index].intersection(
                    dictionary1[index]):
                differences.append(index)

        elif not type(dictionary2[index]) == type(dictionary1[index]):
            differences.append(index)

        elif dictionary1[index] != dictionary2[index]:
            differences.append(index)
    return differences


print(compare_dictionaries(dictionary1, dictionary2))
