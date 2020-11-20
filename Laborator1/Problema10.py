"""Write a function that counts how many words exists in a text. A text is considered to be form out
 of words that are separated by only ONE space. For example: "I have Python exam" has 4 words."""
string = str(input())


def number_of_words(string):
    string = string.lower()
    string = string.title()
    contor = 0

    for char in string:
        if char <= "Z" and char >= "A":
            contor += 1

    return contor


print(number_of_words(string))
