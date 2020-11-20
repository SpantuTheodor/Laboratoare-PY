"""Write a function that receives a number x, default value equal to 1, a list of strings,
 and a boolean flag set to True. For each string, generate a list containing the characters that
  have the ASCII code divisible by x if the flag is set to True, otherwise it should contain
  characters that have the ASCII code not divisible by x."""


def ascii_divisible_with_x(list, flag=True, x=1):
    result = []
    for index in range(len(list)):
        wresult = []
        for letter in list[index]:
            if flag == True:
                if ord(letter) % x == 0:
                    wresult.append(letter)
            if flag == False:
                if ord(letter) % x != 0:
                    wresult.append(letter)

        result.append(wresult)
    return result


print(ascii_divisible_with_x(["atatatafdas", "bagameas", "harapasdkb"], False, 2))
