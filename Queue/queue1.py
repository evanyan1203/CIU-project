# Implement using linked-list, with tail pointer:

class Node:
    def __init__(self, value,next = None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
# empty()

    def empty(self):
        return self.head == None
    
 # enqueue(value) - adds value at a position at the tail           
    def enqueue(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node
            

# dequeue() - returns value and removes least recently added element (front)
    def dequeue(self):
        if self.head is None:
            raise IndexError("queue is empty")
        value = self.head.value
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return value

