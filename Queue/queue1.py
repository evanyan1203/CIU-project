# Implement using linked-list, with tail pointer:

class Node:
    def __init__(self, value,next = None):
        self.value = value
        self.next = None


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


#  Implement using a fixed-sized array:
# enqueue(value) - adds item at end of available storage
# dequeue() - returns value and removes least recently added element
# empty()
# full()


#  Cost:
# a bad implementation using a linked list where you enqueue at the head and dequeue at the tail would be O(n) because you'd need the next to last element, causing a full traversal of each dequeue
# enqueue: O(1) (amortized, linked list and array [probing])
# dequeue: O(1) (linked list and array)
# empty: O(1) (linked list and array)