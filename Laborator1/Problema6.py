"""Write a function that validates if a number is a palindrome."""
number = int(input())


def invert_number(number):
    aux = int(number)
    inverted = int(aux % 10)
    aux = aux // 10
    c = 0

    while aux > 0:
        c = aux % 10
        inverted = inverted * 10 + c
        aux = aux // 10

    return inverted


def palindrome(number):
    inverted = invert_number(number)
    if inverted == number:
        return True
    else:
        return False


print(palindrome(number))
