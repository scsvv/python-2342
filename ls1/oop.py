class Queue: 
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.size == 0
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else: 
            raise IndexError("Cannot dequeue from empty queue")
    
    def size(self):
        return len(self.items)


q1 = Queue()
q1.enqueue(12)
q1.enqueue(13)
print(q1.dequeue())
print(q1.dequeue())