def rsum(List):
    '''(list) -> int
    return the sum of all elements in a given list
    REQ: the list will have at least one element
    '''
    # initialize the result
    result = 0
    # the list only has one element
    if(len(List) == 1):
        if isinstance(List[0], list):
            result = rsum(List[0])
        else:
            result = List[0]
    # the list has more than one element
    elif(len(List) > 1):
        if isinstance(List[0], list):
            result = rsum(List[0]) + rsum(List[1:])
        else:
            result = List[0] + rsum(List[1:])
    return result


def rmax(List):
    '''(list) -> int
    return the maximum number in a given list
    REQ: the list will have at least one element
    '''
    if(len(List) >= 1):
        if isinstance(List[0], int):
            result = List[0]
        else:
            result = rmax(List[0])
        if(len(List) > 1):
            new = rmax(List[1:])
            if(new > result):
                result = new
    else:
        result = float('-inf')
    return result


def second_smallest(L):
    if isinstance(L[0], list):
        if len(L) == 2:
            result = second_smallest(L[0] + L[1:])
        else:
            result = second_smallest(L[0] + L[1:])
    elif isinstance(L[1], list):
        if len(L) == 2:
            result = second_smallest(L[0:1] + L[1])
        else:
            result = second_smallest(L[0:1] + L[1] + L[2:])
    elif len(L) >= 3 and isinstance(L[2], list):
        if len(L) == 3:
            result = second_smallest(L[0:2] + L[2])
        else:
            result = second_smallest(L[0:2] + L[2] + L[3:])
    elif len(L) == 2:
        if L[0] > L[1]:
            result = L[0]
        else:
            result = L[1]
    elif L[0] >= L[1] and L[0] >= L[2]:
        result = second_smallest(L[1:])
    elif L[1] >= L[0] and L[1] >= L[2]:
        result = second_smallest(L[0:1] + L[2:])
    else:
        result = second_smallest(L[0:2] + L[3:])
    return result


def sum_max_min(L):
    if isinstance(L[0], list):
        if len(L) == 1:
            result = sum_max_min(L[0])
        else:
            result = sum_max_min(L[0] + L[1:])
    elif len(L) >= 2 and isinstance(L[1], list):
        if len(L) == 2:
            result = sum_max_min(L[0:1] + L[1])
        else:
            result = sum_max_min(L[0:1] + L[1] + L[2:])
    elif len(L) >= 3 and isinstance(L[2], list):
        if len(L) == 3:
            result = sum_max_min(L[0:2] + L[2])
        else:
            result = sum_max_min(L[0:2] + L[2] + L[3:])
    elif len(L) == 1:
        result = L[0] * 2
    elif len(L) == 2:
        result = L[0] + L[1]
    elif (L[0] - L[1]) * (L[0] - L[2]) <= 0:
        result = sum_max_min(L[1:])
    elif (L[1] - L[0]) * (L[1] - L[2]) <= 0:
        result = sum_max_min(L[0:1] + L[2:])
    else:
        result = sum_max_min(L[0:2] + L[3:])
    return result
