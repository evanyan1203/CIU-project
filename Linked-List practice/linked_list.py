class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

#     *** Implement (I did with tail pointer & without):


class LinkedList:
    def __init__(self):
        self.head = None


    

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
        
        if index<0 or index>= self.size():
            raise IndexError("index out of bound")
        
        current = self.head

        for i in range(index):
            current = current.next

        return current.value
    
#  push_front(value) - adds an item to the front of the list
    def push_front(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        
    
#  push_back(value) - adds an item at the end
    def push_back(self,value):

        new_node = Node(value)
              
        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

#  pop_front() - remove the front item and return its value
    def pop_front(self):
        if self.head is None:
            raise IndexError("List is empty")
        value = self.head.value
        self.head = self.head.next
        return value
        
#  pop_back() - removes end item and returns its value
    def pop_back(self):

        if self.head is None:
            raise IndexError("list is empty")

        if self.head.next is None:
            value = self.head.value
            self.head = None
            return value
        
        current = self.head

        while current.next.next:
            current = current.next
        
        last_node = current.next
        
        current.next = None

        return last_node.value
  

    
#  front() - get the value of the front item

    def front(self):
        if self.head == None:
            raise IndexError("List is empty")
        return self.head.value
    

#  back() - get the value of the end item
    def back(self):
        if self.head is None:
            raise IndexError("List is empty")
        current = self.head
        while current.next:
            current = current.next
        return current.value
        
#  insert(index, value) - insert value at index, so the current item at that index is pointed to by the new item at the index

    def insert(self,index,value):
        if index<0 or index > self.size():
            raise IndexError("Index out of bound")
        
        new_node = Node(value)
        current = self.head

        if index == 0 :
            new_node.next = self.head
            self.head = new_node 
            return 
        
        for i in range(index-1):
            current = current.next
            
        new_node.next = current.next
        current.next = new_node


#  erase(index) - removes node at given index
    def erase(self,index):
        if index<0 or index>= self.size():
            raise IndexError("Index out of bound")
        
        if index == 0:
            self.head = self.head.next
            return
        
        current = self.head

        for i in range(index-1):
            current = current.next
        
        index_node = current.next
        current.next = index.node.next
        index_node.value = None



        
        


#  value_n_from_end(n) - returns the value of the node at the nth position from the end of the list
#  reverse() - reverses the list
#  remove_value(value) - removes the first item in the list with this value 