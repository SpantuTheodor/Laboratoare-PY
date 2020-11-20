"""Find The greatest common divisor of multiple numbers read from the console."""
n = int(input())
array = []

while n > 0:
    x = int(input())
    array.append(x)
    n -= 1


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


result = array[0]

for i in array:
    result = gcd(result, i)

print(result)
