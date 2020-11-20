"""Write a function to return a list of the first n numbers in the Fibonacci string."""


def fibonacciString(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    index1 = 1
    index2 = 1
    result = [index1, index2]
    for _ in range(n - 2):
        index3 = index1 + index2
        index1 = index2
        index2 = index3
        result.append(index2)

    return result


print(fibonacciString(5))
