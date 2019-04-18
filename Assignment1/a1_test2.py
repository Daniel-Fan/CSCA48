#test cases for WackyQueue
from wackyqueue import *

queue = WackyQueue()

input('insert a few into queue')
queue.insert('A', 3)
queue.insert('B', 7)
queue.insert('C', 34)
queue.insert('D', -8)
queue.insert('E', 0)
queue.insert('F', 0)
queue.insert('G', 0)
queue.insert('H', -88)
queue.insert('H', 99)

print(queue.getoddlist().get_priority())
print(queue.getevenlist().get_priority())
print(queue.getoddlist().get_next().get_priority())
print(queue.getevenlist().get_next().get_priority())
print(queue.getoddlist().get_next().get_next().get_priority())
print(queue.getevenlist().get_next().get_next().get_priority())
print(queue.getoddlist().get_next().get_next().get_next().get_priority())
print(queue.getevenlist().get_next().get_next().get_next().get_priority())
print(queue.getoddlist().get_next().get_next().get_next().get_next().get_priority())
