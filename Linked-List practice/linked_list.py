class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

#     *** Implement (I did with tail pointer & without):


class LinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
    def front(self ):
        if self.head is None:
            raise IndexError("List is empty")
        return self.head.value
    
    def pop_front(self):
        if self.head is None:
            raise IndexError("List is empty")
        value = self.head.value
        self.head = self.head.next
        return value
    

#  size() - returns the number of data elements in the list
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
#  empty() - bool returns true if empty
    def empty(self):
        return self.head is None
    
#  value_at(index) - returns the value of the nth item (starting at 0 for first)
    def value_at(self,index):
        current = self.head
        for i in range(index):
            if current is None:
                raise IndexError("Index out of bounds")
            current = current.next
        if current is None:
            raise IndexError("Index out of bounds")
        return current.value
    
#  push_front(value) - adds an item to the front of the list
    def push_front(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

#  pop_front() - remove the front item and return its value
#  push_back(value) - adds an item at the end
#  pop_back() - removes end item and returns its value
#  front() - get the value of the front item
#  back() - get the value of the end item
#  insert(index, value) - insert value at index, so the current item at that index is pointed to by the new item at the index
#  erase(index) - removes node at given index
#  value_n_from_end(n) - returns the value of the node at the nth position from the end of the list
#  reverse() - reverses the list
#  remove_value(value) - removes the first item in the list with this value 