"""Write a function that receives a variable number of positional arguments and a variable number
of keyword arguments and will return the number of positional arguments whose values can be found among
 keyword arguments values."""


def my_function(*args, **kwargs):
    result = 0
    for index in kwargs.items():
        if args.count(index[1]):
            result += 1
    return result


print(my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5))
