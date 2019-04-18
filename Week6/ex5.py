from week6_heap import Heap


def merge_heap(heap1, heap2):
    '''(Heap, Heap) -> Heap
    takes two heaps as its input parameters and returns a heap that contains
    all the elements in two heaps
    REQ: two heaps should not be empty
    '''
    # insert the keys in heap2 to heap1 one by one
    while(not heap2.is_empty()):
        heap1.insert(heap2.remove_last_node())
    return heap1


def first_and_last(heap):
    '''(Heap) -> (obj, obj)
    takes a heap as an input parameter and returns a tuple containing the
    surname of the first and last student in alphabetical order
    '''
    first = heap.min()
    last = heap.remove_last_node()
    # insert the node back to the heap
    heap.insert(last)
    return (first, last)
