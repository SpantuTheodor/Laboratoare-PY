"""Write a function that will order a list of string tuples based on the 3rd character of the 2nd
 element in the tuple. Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]"""

list = [('abc', 'bcd'), ('abc', 'zza'), ('brd', 'bcr'), ('cwa', 'zzz')]


def sort_third_from_second_touple(list):
    list.sort(key=lambda item: item[1][2])
    return list


print(sort_third_from_second_touple(list))
