"""Write a script that calculates how many vowels are in a string."""
array = str(input())
vowels = 0

for char in array:
    if char in "aeiouAEIOU":
        vowels = vowels + 1

print(vowels)
