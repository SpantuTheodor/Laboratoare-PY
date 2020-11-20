"""Write a script that receives two strings and prints the number of occurrences of the first string in the second."""
string = str(input())
substring = str(input())

index = 0
contor = 0

while string.find(substring, index, len(string)) != -1:
    contor = contor + 1
    index = string.find(substring, index, len(string))
    index = index + 1

print(contor)
