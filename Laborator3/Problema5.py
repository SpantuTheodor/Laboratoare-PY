"""The validate_dict function that receives as a parameter a set of tuples ( that represents validation rules
 for a dictionary that has strings as keys and values) and a dictionary. A rule is defined as follows: (key,
  "prefix", "middle", "suffix"). A value is considered valid if it starts with "prefix", "middle" is inside
   the value (not at the beginning or end) and ends with "suffix". The function will return True if the given
    dictionary matches all the rules, False otherwise."""

given_string = {("key1", "come", "inside", "out"), ("key2", "start", "middle", "winter")}
given_dictionary = {
    "key1": "come inside, it's too cold out",
    "key3": "this is not valid"}


def validate_dict(given_string, given_dictionary):

    mistakes = set()
    for index in given_string:
        if index[0] in given_dictionary:
            aux = given_dictionary[index[0]]
            if aux[0:len(index[1])] != index[1]:
                mistakes.add(index[0])
            aux = aux[len(index[1]):len(aux)]
            if aux[-len(index[3]):len(aux)] != index[3]:
                mistakes.add(index[0])
            aux = aux[0:-len(index[3])-1]
            if not index[2] in aux:
                mistakes.add(index[0])

    for index in given_dictionary:

        if index not in [item[0] for item in given_string]:
            mistakes.add(index)

    return mistakes


print(validate_dict(given_string, given_dictionary))