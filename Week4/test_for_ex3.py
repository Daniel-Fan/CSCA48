from ex3 import *


DLL_name1 = DoubleLinkedList()
names1 = sorted(["Archer", "Bailey", "Baker", "Brewer", "Porter", "Potter", "Sawyer", "Slater", 
                 "Smith", "Stringer", "Taylor","Butcher", "Carter", "Chandler", "Clark", "Collier"])
for name in names1:
    DLL_name1.add_first(name) # Descending
DLL_name2 = DoubleLinkedList()
names2 = sorted(["Head", "Hunt", "Hunter", "Judge", "Knight", "Miller", 
                 "Mason", "Page", "Palmer", "Parker", "Thatcher", "Turner", "Walker", "Weaver"], reverse=True)
for name in names2:
    DLL_name2.add_first(name) # Ascending
result = reverse_merge(DLL_name2, DLL_name1)
curr_node = result.get_first()
while(curr_node.get_next() != None):
    element = curr_node.get_element()
    print(element)
    curr_node = curr_node.get_next()
print(allocate_room(result, 'SW319', 5, 2))