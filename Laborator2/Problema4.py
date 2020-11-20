"""Write a function that receives as a parameters a list of musical notes (strings), a list of moves
 (integers) and a start position (integer). The function will return the song composed by going though
 the musical notes beginning with the start position and following the moves given as parameter."""

notes = ["do", "re", "mi", "fa", "sol"]
moves = [1, -3, 4, 2]
start = 2


def compose(notes, moves, start):
    result = []
    result.append(notes[start])
    actual = start
    for index in moves:
        actual = (actual + index) % len(notes)
        result.append(notes[actual])
    return result


print(compose(notes, moves, start))
