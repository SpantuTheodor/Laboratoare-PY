"""Write a function that receives a string as a parameter and returns a dictionary in which the keys
 are the characters in the character string and the values are the number of occurrences of that character
  in the given text."""

string = "Ana has apples."


def string_to_dictionary(string):
    dictionary = {}
    for index in string:
        dictionary[index] = string.count(index)
    return dictionary


print(string_to_dictionary(string))