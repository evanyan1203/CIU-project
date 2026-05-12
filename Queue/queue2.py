#  Implement using a fixed-sized array:
class Queue:
    def __init__(self, capacity = 16):
        self.capacity = capacity
        self.size_value = 0
        self.data = [None] * capacity

        self.front = 0
        self.rear = 0

# enqueue(value) - adds item at end of available storage
    def enqueue(self,value):
        if self.size_value == self.capacity:
            raise OverflowError("queue is full")


        # self.data[self.size_value] = value
        

        self.data[self.rear] = value

        self.rear = (self.rear + 1)%self.capacity
        
        self.size_value+=1
        
# dequeue() - returns value and removes least recently added element
    def dequeue(self):
        if self.size_value ==0:
            raise IndexError("queue is empty")
        
        # value = self.data[0]
        
        # for i in range(self.size_value-1):
        #     self.data[i] = self.data[i+1]
        
        # self.size_value -= 1
        # self.data[self.size_value] = None

        # return value

        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size_value -= 1

        return value
    

# empty()
    def empty(self):
        return self.size_value ==0

# full()
    def full(self):
        return self.size_value ==self.capacity


