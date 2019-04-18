from week4_DLL import DNode, DoubleLinkedList


def reverse_merge(asc_list, dec_list):
    '''(DoubleLinkedList, DoubleLinkedList) -> DoubleLinkedList
    merge one ascending DLL and one decending DLL to one ascending DLL
    REQ: Should be DLLs
    '''
    # creat a new DLL for the result
    merge_list = DoubleLinkedList()
    # when two DLL are either not empty, continue the loop
    while(not asc_list.is_empty() and not dec_list.is_empty()):
        # get the first node from ascending list
        # get the last node from decending list
        asc_element = asc_list.get_first().get_element()
        dec_element = dec_list.get_last().get_element()
        # put the node which has the less value to the merge_list
        # and delete the node from the previous DLL
        if(asc_element < dec_element):
            merge_list.add_last(asc_element)
            asc_list.remove_first()
        elif(asc_element > dec_element):
            merge_list.add_last(dec_element)
            dec_list.remove_last()
        # there exists the same name
        else:
            merge_list.add_last(asc_element)
            asc_list.remove_first()
            dec_list.remove_last()
    # find whether there is a DLL that is not empty
    if(not asc_list.is_empty()):
        # add every first node in asc_list to the merge_list by loop
        while(not asc_list.is_empty()):
            merge_list.add_last(asc_list.get_first().get_element())
            asc_list.remove_first()
    elif(not dec_list.is_empty()):
        # add every last node in dec_list to the merge_list by loop
        while(not dec_list.is_empty()):
            merge_list.add_last(dec_list.get_last().get_element())
            dec_list.remove_last()
    # return the result
    return merge_list


def allocate_room(name_list, room, capacity, index_of_node):
    '''(DoubleLinkedList, str, int, int) -> str
    return a string that shows the two first letters of the
    surnames of the first and last person that should attend the given room
    REQ: index_of_node should not be greater than size of DLL
    '''
    # get the node at index_of_node
    # initial a current node
    curr_node = name_list.get_first()
    for i in range(0, index_of_node):
        curr_node = curr_node.get_next()
    # get the two first letters of first person's name
    first_name = curr_node.get_element()
    first_name = first_name[:2]
    # get the last people who should be in the room
    # by loop according to the capacity
    # initialize a index
    index = 0
    while(index < capacity and curr_node.get_element() is not None):
        # last_person should be next node's element
        last_person = curr_node
        curr_node = curr_node.get_next()
        index += 1
    # get the last people who should be in the room
    last_name = last_person.get_element()
    last_name = last_name[:2]
    # convert to uppercase
    first_name = first_name.upper()
    last_name = last_name.upper()
    # get the result string
    result = room + ' ' + first_name + '-' + last_name
    return result
