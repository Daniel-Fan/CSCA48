def greeting(name):
    '''(str) -> str
    take a string as a parameter that represents a person's name,
    and returns a greeting in the form Hello <name> how are you today?
    where <name> is replaced by the given name.
    REQ: name should be contain first and given name
    >>> greeting('Alice Chen')
    'Hello Alice how are you today?'
    >>> greeting('Daniel Fan')
    'Hello Daniel how are you today?'
    '''
    # split the string to list of strings
    name = name.split()
    # get the sentence
    result = "Hello " + name[0] + " how are you today?"
    # return the sentence
    return result


def mutate_list(new_list):
    '''(list) -> None
    takes a list as a parameter, and modifies that list in some ways
    REQ: list will have at least 1 element in it,
    REQ: and all strings in list will have at least 2 characters in them.
    >>> mutate_list([1, 2, 3])
    '''
    # loop every element in the new_list
    for index in range(1, len(new_list)):
        # element that is an integer is multipled by 2
        if(type(new_list[index]) == int):
            new_list[index] = new_list[index] * 2
        # element that is a boolean is inverted
        elif(type(new_list[index]) == bool):
            new_list[index] = not new_list[index]
        # element that is a string has its first and last characters removed
        elif(type(new_list[index]) == str):
            new_list[index] = new_list[index][1:-1]
    # The 0th element of the list is set to the string Hello
    new_list[0] = 'Hello'


def merge_dicts(dict1, dict2):
    '''(dict, dict) -> dict
    takes two dictionaries as input
    The function returns a new dictionary with all key:value pairs
    from both dictionaries
    REQ: key need to be str
    REQ: value need to be the list of int
    >>> d1 = {'a': [1, 2, 3], 'b': [4], 'c': [5, 6, 7]}
    >>> d2 = {'a': [2], 'b': [8, 9, 0], 'd': [10, 11, 12]}
    >>> merge_dicts(d1, d2)
    {'a': [1, 2, 3, 2], 'b': [4, 8, 9, 0], 'c': [5, 6, 7], 'd': [10, 11, 12]}
    >>> d1 = {'a': [1, 2, 3], 'b': [4], 'c': [5, 6, 7]}
    >>> d2 = {'a': [2], 'b': [8, 9, 0], 'd': [10, 11, 12]}
    >>> merge_dicts(d2, d1)
    {'a': [2, 1, 2, 3], 'b': [8, 9, 0, 4], 'd': [10, 11, 12], 'c': [5, 6, 7]}
    '''
    # loop every key in dict2
    for key in dict2:
        # the dict1 and dict2 are share the same key
        if(key in dict1):
            # loop every element in this value of
            for element in dict2[key]:
                dict1[key].append(element)
        # the key in dict2 is not dict1
        else:
            dict1[key] = dict2[key]
    # return the dict1
    return dict1
