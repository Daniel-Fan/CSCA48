from container import *


def banana_verify(source, goal, container, list_move):
    '''(str, str, Container, list) -> bool
    test whether the moves in the moves list,
    preformed using the specified container turn the source word into the goal
    word, in which case, your function will return True.
    Otherwise it should return False.
    REQ: contain should be stack, queue or bucket
    REQ: the element in list of move should be "P", 'M', "G', 'M'
    '''
    # set initial value for loop
    list_of_i = 0
    # set initial value for source word
    source_of_i = 0
    # set the result that get from operation be empty
    result = ''
    # set the answer be False at first
    answer = False
    # set a value for whether the method raises a exception
    is_exception = False
    # get the step in list of move by loop
    while(list_of_i < len(list_move)):
        # get the action from the list
        action = list_move[list_of_i]
        # the action is move
        if(action == 'M'):
            try:
                # add the letter to result
                result = result + source[source_of_i]
                # increase the index in source
                source_of_i += 1
            except:
                is_exception = True
                pass
        # the action is put
        elif(action == 'P'):
            try:
                # put the item in container
                container.put(source[source_of_i])
                # increase the index in source
                source_of_i += 1
            except ContainerFullException:
                # the container is full and raise a exception
                is_exception = True
                pass
        elif(action == 'G'):
            try:
                # get the item in container and add to result
                result = result + container.get()
            except ContainerEmptyException:
                # the contianer is empty and raises an exception
                is_exception = True
                pass
        # increase the index in list
        list_of_i += 1
    # the len of result need to be the same length to the source
    if(len(goal) == len(source)):
        same_length = True
    # result is the same as goal word, container need to be empty
    # there is no exception raised and have the same letter with the source
    if(result == goal and container.is_empty() and not is_exception and
       same_length):
        answer = True
    # return the result
    return answer
