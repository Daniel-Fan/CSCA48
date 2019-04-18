#test cases for WackyQueue
from wackyqueue import *

def display(a):
    li = ''
    while a != None:
        li += str(a) + '->'
    return li[: -4]

def get_all(q):
    print('Display of my_q as one queue: \n')
    print(str(my_q))

    print('Even list: \n')
    a = my_q.getoddlist()
    print(display(a))

    print('Odd list: \n')
    b = my_q.getoddlist()
    print(display(b))



my_q = WackyQueue()

input('my_q is empty')
input(my_q.isempty())

input('empty extracthigh')
try:
    my_q.extracthigh()
except(EmptyQueueError):
    print('EmptyQueueError')
# input('empty changepri')
# input(my_q.changepriority(4, 2))
# my_q.negateall()

# get_all(my_q)


input('insert empty my_q')
my_q.insert('9', 3)
get_all(my_q)
# input('one element changepri')
# # input(my_q.changepriority(0, 10))
# get_all(my_q)
# input(my_q.changepriority('9', 10))
# get_all(my_q)
# input('negateall')
# my_q.negateall()
# get_all(my_q)
input('extract the only one')
input(my_q.extracthigh())



input('insert a few into my_q')
my_q.insert('A', 3)
my_q.insert('B', 7)
my_q.insert('C', 34)
my_q.insert('D', -8)
my_q.insert('E', 0)
my_q.insert('F', 0)
my_q.insert('G', 0)
my_q.insert('H', -88)
my_q.insert('H', 99)

get_all(my_q)

print('Extract High')
print(my_q.extracthigh())

get_all(my_q)


# print('a few changepri')
# print('change B to 6')
# get_all(my_q)
# print('change E to 1')
# get_all(my_q)
# print('change bweuiofhlkcj to 6')
# get_all(my_q)
# print('change H to 14')
# get_all(my_q)

# input('negateall')
# my_q.negateall()
# get_all(my_q)