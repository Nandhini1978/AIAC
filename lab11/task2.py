class ListQueue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)  
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)  
    def is_empty(self):
        return len(self.items) == 0
from collections import deque
class DequeQueue:
    def __init__(self):
        self.items = deque()
    def enqueue(self, item):
        self.items.append(item)  
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.popleft()  
    def is_empty(self):
        return len(self.items) == 0
if __name__ == "__main__":
    list_queue = ListQueue()
    print("Is ListQueue empty?", list_queue.is_empty())  
    list_queue.enqueue(10)
    list_queue.enqueue(20)
    list_queue.enqueue(30)
    print("Dequeue from ListQueue:", list_queue.dequeue())  
    print("Is ListQueue empty?", list_queue.is_empty())  
    list_queue.dequeue()
    list_queue.dequeue()
    print("Is ListQueue empty after dequeuing all?", list_queue.is_empty())  
    deque_queue = DequeQueue()
    print("Is DequeQueue empty?", deque_queue.is_empty())  
    deque_queue.enqueue(10)
    deque_queue.enqueue(20)
    deque_queue.enqueue(30)
    print("Dequeue from DequeQueue:", deque_queue.dequeue()) 
    print("Is DequeQueue empty?", deque_queue.is_empty())  
    deque_queue.dequeue()
    deque_queue.dequeue()
    print("Is DequeQueue empty after dequeuing all?", deque_queue.is_empty())  

