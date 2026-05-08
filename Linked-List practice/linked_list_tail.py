
#  Implement (I did with tail pointer & without):

class Node:
    def __init__(self,value = 0, next = None):
        self.value = value
        self.next = next

class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    
#  size() - returns the number of data elements in the list

    def size(self):
        current = self.head
        count = 0
        while current :
            current = current.next 
            count +=1
        return count
    
#  empty() - bool returns true if empty
    
    def empty(self):
        return self.head is None
    
#  value_at(index) - returns the value of the nth item (starting at 0 for first)

    def value_at(self,index):
        current = self.head
        for i in range(index):
            current = current.next

        return current.value
    
#  push_front(value) - adds an item to the front of the list

    def push_front(self,value):

        new_node = Node(value, next = self.head)

        self.head = new_node

        if self.tail is None:
            self.tail = new_node

#  pop_front() - remove the front item and return its value
    def pop_front(self):


        if self.head is None:
            raise IndexError("list is empty")

        value = self.head.value
        
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        return value
    

#  push_back(value) - adds an item at the end
    def push_back(self,value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        
        self.tail.next = new_node
        self.tail = new_node
       
#  pop_back() - removes end item and returns its value
#  front() - get the value of the front item
#  back() - get the value of the end item
#  insert(index, value) - insert value at index, so the current item at that index is pointed to by the new item at the index
#  erase(index) - removes node at given index
#  value_n_from_end(n) - returns the value of the node at the nth position from the end of the list
#  reverse() - reverses the list
#  remove_value(value) - removes the first item in the list with this value