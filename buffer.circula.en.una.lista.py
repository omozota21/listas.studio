class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer =  None * capacity
        self.size = 0
        self.head = 0

    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.capacity
    
    
Buffer = CircularBuffer
Buffer = 1
Buffer = 2
Buffer = 3
Buffer = 4

print( Buffer)