"""Write a function that receives as paramer a matrix which represents the heights of the spectators
 in a stadium and will return a list of tuples (line, column) each one representing a seat of a spectator
  which can't see the game. A spectator can't see the game if there is at least one taller spectator
   standing in front of him. All the seats are occupied. All the seats are at the same level.
   Row and column indexing starts from 0, beginning with the closest row from the field."""

list = [[1, 2, 3, 2, 1, 1],
        [2, 4, 4, 3, 7, 2],
        [5, 5, 2, 5, 6, 4],
        [6, 6, 7, 6, 7, 5]]


def people_that_cant_see(list):
    result = []

    for column in range(len(list[1])):

        auxiliary = []
        for index in list:
            auxiliary.append(index[column])
        print(auxiliary)
        for row in range(len(auxiliary) - 1, 0, - 1):
            if max(auxiliary) == auxiliary[row] and auxiliary.count(auxiliary[row]) == 1:
                auxiliary.pop()
            else:
                result.append((row, column))
                auxiliary.pop()
    return result


print(people_that_cant_see(list))
