class Vector:
    def __init__(self, capacity=16):
        self.capacity_value = capacity
        self.size_value = 0
        self.data = [None] * capacity


    def size(self):
        return self.size_value

    def capacity(self):
        return self.capacity_value

    def is_empty(self):
        return self.size_value == 0
    
    def at(self, index):
        if index < 0 or index >= self.size_value:
            raise IndexError("index out of bounds")
        
        return self.data[index]
    
    def push(self, item):
        self.data[self.size_value] = item
        self.size_value += 1
        if self.size_value == self.capacity_value:
            self._resize(self.capacity_value * 2)


    def _resize(self, new_capacity): # private
        new_data = [None] * new_capacity

        #move old data
        for i in range(self.size_value):
            new_data[i] = self.data[i]


        self.data = new_data
        self.capacity_value = new_capacity

    def insert(self, index ,item ):
        # check index legal or not
        if index < 0 or index > self.size_value:
            raise IndexError
        #check resize
        if self.size_value == self.capacity_value:
            self._resize(self.capacity_value * 2)

        for i in range(self.size_value, index, -1):
            self.data[i] = self.data[i-1]

        self.data[index] = item    
        self.size_value+=1

    #prepend(item) - can use insert above at index 0

    def prepend(self, item):
        self.insert(0,item)
        

    #pop() - remove from end, return value

    def pop(self):
        #check if its empty
        if self.is_empty():
            raise IndexError("pop from empty vector")

        value = self.data[self.size_value - 1]

        self.data[self.size_value-1] = None

        self.size_value -= 1

        if self.size_value <= self.capacity_value//4:
            self._resize(self.capacity_value//2)

        return value

    #delete(index) - delete item at index, shifting all trailing elements left

    def delete(self,index):

        #check
        if index <0 or index >=self.size_value:
            raise IndexError("Index out of bounds")
        
        for i in range(index, self.size_value-1):
            self.data[i] = self.data[i+1]
        self.pop()

    #remove(item) - looks for value and removes index holding it (even if in multiple places)

    def remove(self,item):
        i = 0
        while i < self.size_value:

            if self.data[i] == item:
                self.delete(i)
            else:
                 i+=1   

    #find(item) - looks for value and returns first index with that value, -1 if not found

    def find(self,item):
        for i in range(self.size_value):

            if self.data[i] == item:
                return i  
                
        return -1
        
    
    #when you reach capacity, resize to double the size


    #when popping an item, if the size is 1/4 of capacity, resize to half        