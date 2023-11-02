class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.size = 0
        self.head = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def push(self, item):
        if self.is_full():
            # Si el buffer está lleno, sobrescribir el elemento más antiguo.
            self.buffer[self.head] = item
            self.head = (self.head + 1) % self.capacity
        else:
            # Si el buffer no está lleno, simplemente agregar el elemento.
            self.buffer[self.size] = item
            self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        else:
            item = self.buffer[(self.head - self.size) % self.capacity]
            self.size -= 1
            return item

    def __str__(self):
        elements = [str(self.buffer[(self.head - i) % self.capacity]) for i in range(self.size)]
        return " ".join(elements)

# Ejemplo de uso
buffer = CircularBuffer(5)
buffer.push(1)
buffer.push(2)
buffer.push(3)
buffer.push(4)
buffer.push(5)

print("Buffer después de agregar elementos:", buffer)
print("Pop:", buffer.pop())
print("Buffer después de hacer pop:", buffer)

buffer.push(6)
print("Buffer después de agregar otro elemento:", buffer)
