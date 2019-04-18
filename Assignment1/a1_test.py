from wackyqueue import *


queue = WackyQueue()
queue.insert('A', 1)
queue.insert(1, 2)
queue.insert(3, 7)
queue.insert('E', 5)
queue.insert('Z', 0)
queue.insert('Y', -10)
queue.insert('C', 3)
queue.insert('H', 20)
queue.insert('U', -5)
queue.insert('X', -20)
queue.changepriority(3, 5)
print(queue.getoddlist().get_priority())
print(queue.getevenlist().get_item())
print(queue.getoddlist().get_next().get_priority())
print(queue.getevenlist().get_next().get_priority())
print(queue.getoddlist().get_next().get_next().get_priority())
print(queue.getevenlist().get_next().get_next().get_priority())
print(queue.getoddlist().get_next().get_next().get_next().get_priority())
print(queue.getevenlist().get_next().get_next().get_next().get_priority())
print(queue.getoddlist().get_next().get_next().get_next().get_next().get_priority())
print(queue.getevenlist().get_next().get_next().get_next().get_next().get_priority())