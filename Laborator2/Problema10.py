"""Write a function that receives a variable number of lists and returns a list of tuples
as follows: the first tuple contains the first items in the lists, the second element contains
 the items on the position 2 in the lists, etc. Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"]
  return: [(1.5, "a ") ,(5, 6, "b"), (3,7, "c")].

  Note: If input lists do not have the same number of items, missing items will be replaced with
None to be able to generate max ([len(x) for x in input_lists]) tuples."""

print("Numarul de liste: ")
index = int(input())
inp = []
max_len = 0
while index:
    print("Numarul de elemente din lista actuala: ")
    items = int(input())
    auxiliary = []
    if items > max_len:
        max_len = items
    while items:
        item = input()
        auxiliary.append(item)
        items -= 1
    inp.append(auxiliary)
    index -= 1

for index in range(len(inp)):
    if len(inp[index]) < max_len:
        diff = max_len - len(inp[index])
        for _ in range(diff):
            inp[index].append(None)

print(inp)


def group_by_index(list):
    result = []

    for column in range(len(list[1])):

        auxiliary = []
        for index in list:
            auxiliary.append(index[column])

        result.append(tuple(auxiliary))

    return result


print(group_by_index(inp))
