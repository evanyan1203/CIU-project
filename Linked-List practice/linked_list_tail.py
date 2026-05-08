
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
    def pop_back(self):
        
        if self.head is None:
            raise IndexError("list is empty")
        
        value = self.tail.value

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return value
    
        current= self.head

        while current.next is not self.tail:
            current = current.next

        self.tail = current
        self.tail.next = None

        return value
#  front() - get the value of the front item
    def front(self):
        if self.head is None:
            raise IndexError("list is empty")
        return self.head.value
    
#  back() - get the value of the end item
    def back(self):
        if self.head is None:
            raise IndexError("list is empty")
        return self.tail.value
    
#  insert(index, value) - insert value at index, so the current item at that index is pointed to by the new item at the index
    def insert(self,index,value):
        if index<0 or index>=self.size():
            raise IndexError("index out of bound")

        if index == 0 :
            self.push_front(value)
            return
        
        if index == self.size():
            self.push_back(value)

        new_node = Node(value)
        current = self.head

        for i in range(index-1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node

       
#  erase(index) - removes node at given index

#  value_n_from_end(n) - returns the value of the node at the nth position from the end of the list
#  reverse() - reverses the list
#  remove_value(value) - removes the first item in the list with this value