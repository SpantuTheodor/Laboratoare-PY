"""Write a function that extract a number from a text (for example if the text is
"An apple is 123 USD", this function will return 123, or if the text is "abc123abc"
 the function will extract 123). The function will extract only the first number that is found."""
string = str(input())


def trim_first_number(string):
    condition = 0
    array = ""

    for char in string:
        if char.isnumeric():
            condition = 1
            array += char
        elif ((char.isnumeric() == 0) and (condition == 1)):
            return array
            break


print(trim_first_number(string))
