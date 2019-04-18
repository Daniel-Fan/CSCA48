def rsum(List):
    '''(list) -> int
    return the su of all elements in a given list
    REQ: the list will have at least one element
    '''
    # initialize the result
    result = 0
    # the list only has one element
    if(len(List) == 1):
        result = List[0]
    # the list has more than one element
    else:
        result = List[0] + rsum(List[1:])
    return result


def rmax(List):
    '''(list) -> int
    return the maximum number in a given list
    REQ: the list will have at least one element
    '''
    result = List[0]
    if(len(List) > 1):
        result = List[0]
        new = rmax(List[1:])
        if(new > result):
            result = new
    return result


def second_smallest_helper(List):
    '''(list) -> tuple
    return two smallest numbers in a given list
    '''
    # the list has only two elements
    if(len(List) == 2):
        result = ((List[0], List[1]) if List[0] < List[1]
                  else(List[1], List[0]))
    # the list has more than two elements
    else:
        # List[0] is bigger than one of element in tuple
        small_result = second_smallest_helper(List[1:])
        if(List[0] < small_result[1] and
           List[0] >= small_result[0]):
            result = (small_result[0], List[0])
        elif(List[0] <= small_result[0]):
            result = (List[0], small_result[0])
        else:
            result = small_result
    return result


def second_smallest(List):
    '''(list) -> int
    return the second smallest number in a given list
    REQ: the list will have at least two elements
    '''
    return second_smallest_helper(List)[1]


def sum_max_min_helper(List):
    '''(list) -> tuple
    return the tuple of the maximum and minimum elements in a given list
    '''
    # only one elements in list
    if(len(List) == 1):
        result = (List[0], List[0])
    # two elements in the list
    elif(len(List) == 2):
        result = ((List[0], List[1]) if List[0] > List[1]
                  else (List[1], List[0]))
    # there are more than two elements in the list
    else:
        small_result = sum_max_min_helper(List[1:])
        # the List[0] is the biggest element
        if(List[0] > small_result[0]):
            result = (List[0], small_result[1])
        # the List[0] is the smallest element
        elif(List[0] < small_result[1]):
            result = (small_result[0], List[0])
        else:
            result = small_result
    return result


def sum_max_min(List):
    '''(list0 -> int
    return the sum of the maximum and minimum elements in the given list
    '''
    result = sum_max_min_helper(List)
    return result[0] + result[1]
