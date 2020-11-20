"""Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores."""
old_string = str(input())
new_string = ""

for char in old_string:
    if char.isupper():
        new_string = new_string + "_"
        new_string = new_string + char.lower()
    else:
        new_string = new_string + char
if new_string[0] == "_":
    print(new_string[1:])
else:
    print(new_string)
