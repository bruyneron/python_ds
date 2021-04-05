import import_setup
from ds.stack import Stack

class Queue:
    def __init__(self):
        self.push_queue = Stack()
        self.pop_queue = Stack()

    def is_empty(self):
        return self.pop_queue.is_empty() and self.push_queue.is_empty()

    def enqueue(self, data):
        self.push_queue.push(data)
    
    def dequeue(self):
        if self.is_empty():
            raise Exception('Can\'t dequeue. Queue is empty')
        
        if self.pop_queue.is_empty():
            while(not self.push_queue.is_empty()):
                self.push_queue.push(self.push_queue.pop())

        return self.pop_queue.pop()
    
    def size(self):       
        return self.push_queue.size() + self.pop_queue.size()


if __name__ == '__main__':
    pass