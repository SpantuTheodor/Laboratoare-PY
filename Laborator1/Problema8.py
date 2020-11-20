"""Write a function that counts how many bits with value 1 a number has. For example for number 24,
 the binary format is 00011000, meaning 2 bits with value "1"""
number = int(input())


def to_bin(number):
    bin_number = bin(number)[2:]
    print(bin_number)
    return bin_number


def count_ones(number):
    bin_number = to_bin(number)
    counter = bin_number.count('1')
    return counter


print(count_ones(number))
