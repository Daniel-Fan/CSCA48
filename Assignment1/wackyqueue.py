"""
# Copyright Yuchen Fan, 2018
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSCA48, Winter 2018
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""

from wackynode import WackyNode


# Do not add import statements or change the one above.
# Write your WackyQueue class code below.
class Queue_is_Empty_Error(Exception):
    '''the error represents that the queue is empty'''


class WackyQueue():
    '''this class defines a Wacky Queue ADT '''
    def __init__(self):
        '''(WackyQueue) -> NoneType
        create two empty WackyQueue
        '''
        # respresentation inviriant:
        # _Oddhead is a WackyNode
        # _Evenhead is a WackyNode
        # if the Queue is empty:
        #     _Oddhead == _Evenhead == None
        # otherwise:
        #     _Oddhead is the first odd Node in the queue
        #     _Evenhead is the first even Node in the queue
        self._Oddhead = None
        self._Evenhead = None

    def isempty(self):
        '''(WackyQueue) -> bool
        return True iif both odd and even list is empty
        '''
        return self._Oddhead is None and self._Evenhead is None

    def insert(self, obj, pri):
        '''(WackyQueue, object, int) -> NoneType
        Insert object obj with priority pri into the wacky queue
        '''
        # create a new Wacky Node
        Newnode = WackyNode(obj, pri)
        # case 1: it is the first inserted Node in the list, the list is empty
        if(self._Oddhead is None):
            self._Oddhead = Newnode
        else:
            # use help funtion to find the position whose
            # priority is less than pri
            cur, pre, double_pre, Oddcur, Evencur, is_end, is_odd =\
                self._find_pri_pos(pri)
            # use help function to insert the Newnode in the position
            self._insert_pos(Newnode, cur, pre, double_pre, Oddcur, Evencur,
                             is_end, is_odd)

    def extracthigh(self):
        '''(WackyQueue) -> object
        Remove and return the first item in the wacky queue
        REQ: the Wacky Queue is not empty
        '''
        # the queue is empty, raise the error
        if(self.isempty()):
            raise Queue_is_Empty_Error
        # the queue is not empty
        else:
            # get the item with the highest priority
            high_item = self._Oddhead.get_item()
            # set a temporary point points to the next node of oddlist
            # switch the oddhead and evenhead
            temp = self._Oddhead.get_next()
            self._Oddhead = self._Evenhead
            self._Evenhead = temp
        return high_item

    def getoddlist(self):
        '''(WackyQueue) -> WackyNode or NoneType
        Return a pointer to a linked list of WackyNode containing
        every other object in the wacky queue
        starting with the first object.
        '''
        return self._Oddhead

    def getevenlist(self):
        '''(WackyQueue) -> WackyNode or NoneType
        Return a pointer to a linked list of WackyNode containing
        every other object in the wacky queue
        starting with the second object.
        '''
        return self._Evenhead

    def changepriority(self, obj, pri):
        '''(WackyQueue, object, int) -> NoneType
        Change the priority of the first copy of object obj to pri.
        The wacky queue is unchanged if obj is not in it or already has
        priority pri.
        If the priority of obj is changed, then the insertion time of
        obj is taken to be the time of the changepriority operation.
        '''
        # find the first Node whose item is the object in this list
        # find whether there exist the same priority in the list
        # find the position whose pri is less than pri
        cur, pre, double_pre, is_same, cur_pri, pre_pri, double_pre_pri,\
            pri_Even, pri_Odd, pri_is_end, pri_is_odd\
            = self._first_obj_same_priority(obj, pri)
        # change the priority when obj is in it and do not have same pri
        if(is_same is False and cur is not None):
            # if the pri is less than the first object's pri and
            # large than or euql to the next node's pri
            # just change the priority for the first node
            if(cur == pre_pri or cur == cur_pri):
                cur.set_priority(pri)
            # it is the first oddlist node and the second last node in the list
            elif(cur.get_next() is None and self._Oddhead == cur and
                 pri_is_end is True):
                cur.set_priority(pri)
                self._Evenhead = cur
                self._Oddhead = cur_pri
            # the first node is the second last node in list
            # and will be in the last
            elif(cur.get_next() is None and pre.get_next() is not None and
                 pri < cur_pri.get_priority()):
                cur.set_priority(pri)
                double_pre.set_next(cur_pri)
                pre.set_next(cur)
            # the first node will switch the position with the node before it
            elif(pre == cur_pri and double_pre is not None and
                 double_pre_pri is not None):
                cur.set_priority(pri)
                temp = cur.get_next()
                cur.set_next(cur_pri.get_next())
                double_pre_pri.set_next(cur)
                double_pre.set_next(cur_pri)
                cur_pri.set_next(temp)
            # the pri is less than first object and large than
            # the next node of next node of this object's pri
            elif(cur == double_pre_pri):
                cur.set_priority(pri)
                cur.set_next(pre_pri.get_next())
                pre_pri.set_next(cur_pri)
                # case 1: the first object is the first node in the odd list
                if(pre is None and double_pre is None):
                    self._Evenhead = cur
                    self._Oddhead = pre_pri
                # case 2: the first object is the first node in even list
                elif(double_pre is None and pre is not None):
                    pre.set_next(cur)
                    self._Evenhead = pre_pri
                # case 3: the general case
                else:
                    pre.set_next(cur)
                    double_pre.set_next(pre_pri)
            else:
                # remove this object from the list
                # case 1: the first object is the first node in odd list
                if(double_pre is None and pre is None):
                    # point the Oddhead to the Evenhead
                    # point the Evenhead to second node in the odd list
                    self._Oddhead = self._Evenhead
                    self._Evenhead = cur.get_next()
                # case 2: the first object is the first node in even list
                elif(double_pre is None and pre is not None):
                    # point Evenhead to the next node of pre
                    # point the pre node to next node of cur
                    self._Evenhead = pre.get_next()
                    pre.set_next(cur.get_next())
                # case 3: the general case
                else:
                    # remove the Node with first obj in the list
                    # set the next node of cur node to be
                    # the next node of pre node
                    # set the next node pf pre node to be the next
                    # node of double pre node
                    double_pre.set_next(pre.get_next())
                    pre.set_next(cur.get_next())
                # insert the Node to the sepcific position
                # create a new Wacky Node
                Newnode = WackyNode(obj, pri)
                # case 1: the list is empty
                if(self._Oddhead is None):
                    self._Oddhead = Newnode
                else:
                    self._insert_pos(Newnode, cur_pri, pre_pri,
                                     double_pre_pri, pri_Odd, pri_Even,
                                     pri_is_end, pri_is_odd)

    def negateall(self):
        '''(WackyQueue) -> NoneType
        Negate the priority of every object in the wacky queue.
        '''
        # creat pre, cur and next nodes for odd and even list respectively
        pre_odd = pre_even = None
        cur_odd = self._Oddhead
        cur_even = self._Evenhead
        next_odd = self._Oddhead.get_next()
        next_even = self._Evenhead.get_next()
        # stop loop when the cur node is None
        while(next_odd is not None and next_even is not None):
            # negate the cur node's priority for both odd and even list
            cur_odd.set_priority(-cur_odd.get_priority())
            cur_even.set_priority(-cur_even.get_priority())
            # set the pre to be the next node of cur in the reverse order
            cur_odd.set_next(pre_odd)
            cur_even.set_next(pre_even)
            # set pre node to be cur node and cur node to be next node
            # next node to be the next node of next node
            pre_odd = cur_odd
            cur_odd = next_odd
            next_odd = next_odd.get_next()
            pre_even = cur_even
            cur_even = next_even
            next_even = next_even.get_next()
        # negate the priority for second last nodes in the list
        cur_odd.set_priority(-cur_odd.get_priority())
        cur_even.set_priority(-cur_even.get_priority())
        # conncet the rest of nodes
        cur_odd.set_next(pre_odd)
        cur_even.set_next(pre_even)
        # case 1: the odd list have one more element than even list
        if(next_odd is not None and next_even is None):
            # negate the priority of next node for odd list
            next_odd.set_priority(-next_odd.get_priority())
            next_odd.set_next(cur_odd)
            # set the head for odd and even lists
            # the odd and even lists do not change
            self._Oddhead = next_odd
            self._Evenhead = cur_even
        # case2: the odd and even list have the same amount of element
        else:
            # set the head for odd and even lists
            # the odd and even lists have been switched
            self._Oddhead = cur_even
            self._Evenhead = cur_odd

    def _find_pri_pos(self, pri):
        '''(WackyQueue, int) -> WackyNode, WackyNode, WackyNode, WackyNode,\
        WackyNode, bool, bool
        find the position of the Node whose priority  is less than pri
        '''
        # set two pointers point to the two list
        Oddcur = self._Oddhead.get_next()
        Evencur = self._Evenhead
        # compare priority with the nodes in two list in turn
        # from the first Node in the odd list
        # set a pointer point to the current node that is compared
        cur = self._Oddhead
        # set a previous pointer points to the node before cur node
        # set a previous poniter points to the node before pre node
        pre = double_pre = None
        # set a bool whether the cur node is in the odd list
        is_odd = True
        # set a bool whether the object is inserted at the end
        is_end = False
        # stop comparing when the pri is higher than the priority in the list
        while((Oddcur is not None or Evencur is not None) and
              cur.get_priority() >= pri):
            # set the previous and double_pre Node to
            # the current Node and pre Node
            double_pre = pre
            pre = cur
            # case 1: cur node is in odd list
            if(is_odd is True):
                cur = Evencur
                # Evencur points to next Node
                Evencur = Evencur.get_next()
            # case 2: cur node is in even list
            elif(is_odd is False):
                cur = Oddcur
                # Oddcur points to next node
                Oddcur = Oddcur.get_next()
            # change the value of is_odd
            is_odd = not is_odd
        # the object is inserted at the end
        if(Oddcur is None and Evencur is None and cur.get_priority() >= pri):
            is_end = True
        return cur, pre, double_pre, Oddcur, Evencur, is_end, is_odd

    def _first_obj_same_priority(self, obj, pri):
        '''(WackyQueue, object, int) -> WackyNode, WackyNode, WackyNode, bool,\
        WackyNode, WackyNode, WackyNode, WackyNode,\
        WackyNode, bool, bool
        find the first Node whose item is the object in the list
        whether their is the same pri in the list
        find the position whose pri is less than the pri
        '''
        # set two pointers point to the two list
        Oddcur = self._Oddhead.get_next()
        Evencur = self._Evenhead
        # compare object with the nodes in two list in turn
        # from the first node in odd list
        # set a pointer point to the current node that will be compared
        cur = self._Oddhead
        # set a previous pointer points to the node before the cur node
        # set a previous pointer points to the node before pre node
        pre = double_pre = None
        # set a bool whether the cur node is in the odd list
        is_odd = True
        # set Nodes for finding the first same object in the list
        first_obj = pre_first_obj = double_pre_first_obj = None
        # set the Nodes for finding the position whose pri is less than pri
        less_pri = pre_less_pri = double_pre_less_pri = None
        Even_pos_pri = Odd_pos_pri = None
        pri_is_end = False
        pri_is_odd = True
        # set a bool whether find the first same object in the list
        find_first = False
        # set a bool whether find the same priority for the same object
        is_same = False
        # set a bool whether find the first pri in list that is less than pri
        is_less_pri = False
        # stop loop when we find first obj and the same priority
        while((Oddcur is not None or Evencur is not None) and
              (is_same is False or find_first is False)):
            # find the obj first time, record the nodes
            if(find_first is False and cur.get_item() == obj):
                first_obj = cur
                pre_first_obj = pre
                double_pre_first_obj = double_pre
                find_first = True
            # find the obj and compare its priority
            if(cur.get_item() == obj and cur.get_priority() == pri):
                is_same = True
            # find the first pri which is less than pri
            if(is_less_pri is False and cur.get_priority() < pri):
                # record this position
                less_pri = cur
                pre_less_pri = pre
                double_pre_less_pri = double_pre
                is_less_pri = True
                Even_pos_pri = Evencur
                Odd_pos_pri = Oddcur
                pri_is_odd = is_odd
            # set the previous and double_pre points to
            # the current pointer and pre
            double_pre = pre
            pre = cur
            # cur points to odd list
            if(is_odd is True):
                cur = Evencur
                # Evencur points to next Node
                Evencur = Evencur.get_next()
            # cur points to even list
            elif(is_odd is False):
                cur = Oddcur
                # Oddcur points to next node
                Oddcur = Oddcur.get_next()
            # change the value of is_odd
            is_odd = not is_odd
        # check the last node
        if(find_first is False and cur.get_item() == obj):
            first_obj = cur
            pre_first_obj = pre
            double_pre_first_obj = double_pre
            find_first = True
        # find the obj and compare its priority
        if(cur.get_item() == obj and cur.get_priority() == pri):
            is_same = True
        # find whether there is a pri which is less than pri in the list
        if(is_less_pri is False):
            # record this position
            less_pri = cur
            pre_less_pri = pre
            double_pre_less_pri = double_pre
            is_less_pri = True
            Even_pos_pri = Evencur
            Odd_pos_pri = Oddcur
            pri_is_odd = is_odd
            if(cur.get_priority() > pri):
                pri_is_end = True
        # return the first Node whose item is object
        # and whether there exists the same priority
        # return the pos of the pri is less than the pri
        return first_obj, pre_first_obj, double_pre_first_obj, is_same,\
               less_pri, pre_less_pri, double_pre_less_pri, Even_pos_pri,\
               Odd_pos_pri, pri_is_end, pri_is_odd

    def _insert_pos(self, Newnode, cur, pre, double_pre, Oddcur, Evencur,
                    is_end, is_odd):
        '''(WackyQueue, WackyNode, WackyNode, WackyNode, WackyNode, WackyNode,
        WackyNode, bool, bool) -> NoneType
        insert the Newnode in the specific position'''
        # case 2: the position which the node will be inserted
        # is the head of odd list
        if(pre is None and double_pre is None and
           Newnode.get_priority() > self._Oddhead.get_priority()):
            # set the evenhead to be the next node of Newnode
            Newnode.set_next(self._Evenhead)
            # switch the odd and even list
            self._Evenhead = self._Oddhead
            self._Oddhead = Newnode
        # case 3: the position is the head of even list
        # and evenhead is None
        elif(pre is None and double_pre is None and is_end is True):
            self._Evenhead = Newnode
        # case 4: the position is the head of even list
        # and evenhead is not None
        elif(pre is not None and double_pre is None and cur is not None):
            # Newnode is the first node in the even list
            Newnode.set_next(self._Oddhead.get_next())
            # switch the even and odd list
            pre.set_next(cur)
            self._Evenhead = Newnode
        # case 5: the object is inserted at the end of list
        elif(is_end is True):
                pre.set_next(Newnode)
        # case 6: the object is inserted in the middle of list
        else:
            # set the cur to be the next node of pre
            pre.set_next(cur)
            # set the Newnode to be the next node of double_pre
            double_pre.set_next(Newnode)
            # the cur is in oddlist
            if(is_odd is True):
                # set the Evencur to be the next node of Newnode
                Newnode.set_next(Evencur)
            else:
                # set the Oddcur to be the next node of Newnode
                Newnode.set_next(Oddcur)
