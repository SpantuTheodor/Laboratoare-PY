import math

"""2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it."""


def onlyPrimes(array: list) -> list:
    result = [array[x] for x in range(len(array)) if
              len([y for y in range(2, int(math.sqrt(array[x]) + 1)) if array[x] % y == 0]) == 0]
    return result


print(onlyPrimes([2, 6, 7, 424, 74, 3, 1, 0, 234, 97]))
