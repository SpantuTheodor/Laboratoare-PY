"""Write a functions that determine the most common letter in a string. For example if the string
 is "an apple is not a tomato", then the most common character is "a" (4 times). Only letters
  (A-Z or a-z) are to be considered. Casing should not be considered "A" and "a" represent
  the same character."""

string = str(input())


def max_number_of_letters(string):
    dictionary = {}
    max = 0
    result = ""

    string.lower()

    for char in string:
        dictionary[char] = dictionary.get(char, 0) + 1

    for key in dictionary:
        if dictionary[key] > max:
            max = dictionary[key]
            result = key

    return result


print(max_number_of_letters(string))
