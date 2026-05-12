#  Implement using a fixed-sized array:
class Queue:
    def __init__(self, capacity = 16):
        self.capacity = capacity
        self.size_value = 0
        self.data = [None] * capacity
# enqueue(value) - adds item at end of available storage
    def enqueue(self,value):
        if self.size_value == self.capacity:
            raise OverflowError("queue is full")

        self.data[self.size_value] = value
        self.size_value+=1
        
# dequeue() - returns value and removes least recently added element
    def dequeue(self):
        if self.size_value ==0:
            raise IndexError("queue is empty")
        
        value = self.data[0]
        
        for i in range(self.size_value-1):
            self.data[i] = self.data[i+1]
        
        self.size_value -= 1
        self.data[self.size_value] = None

        return value
    

# empty()
    def empty(self):
        return self.size_value ==0

# full()
    def full(self):
        return self.size_value ==self.capacity


