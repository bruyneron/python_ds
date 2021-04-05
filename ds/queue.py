'''
1) List
enqueue()   |   q.append()
dequeue()   |   q.pop(0)     1st element is 0
size()      |   len(q)
is_empty()  |   len(q)==0


2) SLL/DLL 
  (Have to use DLL. Reason: With SLL deletion takes O(n), Queue is supposed to take O(1) for deletion) <--- This is dumb
   why?? 
   SLL with head and tail. 
   Insertion @ tail (No deletion @ tail) -> O(1)
   Deletion @ head (No insertion @ head) -> O(1)

   1 -> 2 -> 3 ->
   |         |
   head      Tail

------------------------------------------------------------------------------------

FIFO - QUEUE

Insertion       |   O(1)
Deletion        |   O(1)
Access/Search   |   O(n)

'''

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        # if (self.head is self.tail) doesn't work for identifying empty queue
        # Reason: If queue has only one element, then head and tail pint to the same element
        return self.head is None and self.tail is None

    def enqueue(self, data):
        '''
        2 cases:
        1) Empty queue
        2) Non empty queue
        '''
        if self.is_empty():
            self.head = self.tail = Node(data, None)
            return

        self.tail.next = Node(data, None) 
        self.tail = self.tail.next
    
    def dequeue(self):
        '''
        3 cases:
        1) Empty queue
        2) Non-empty queue with more than 1 elements
        3) Non-empty queue with exactly 1 element
        '''
        if self.is_empty():
            raise Exception('Queue is empty. Can\'t dequeue')

        dequeued_element = self.head.data # Don't return node itself. If node is returned returned node can be used to traverse the Queue
        self.head = self.head.next

        # In case of a Queue 'q'  with one element
        #     1 --> None
        #     /\
        #  head tail
        #
        # After: q.dequeue()
        #
        #     1 --> None
        #     |      |
        #   tail    head
        # 
        # Tail would still be pointing to an element. Hence queue won't be empty. So tail should be reset
        # For queue to be empty condition is:  (self.head is None) and (self.tail is None)
        #
        if self.head is None:
            self.tail = None

        return dequeued_element
    
    def size(self):
        if self.is_empty():
            return 0
        
        itr = self.head
        length = 0
        while itr:
            length += 1
            itr = itr.next

        return length
    
    def reverse(self):
        if self.is_empty():
            return 
        
        # Reverse links (Reversing linked list)
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next
        
        # Reverse head and tail markers
        temp = self.head
        self.head = self.tail
        self.tail = temp

    
    def print(self):
        if self.is_empty(): 
            print('Queue is empty')
            return
        
        itr = self.head
        qstr = ''
        while itr:
            qstr += str(itr.data) + '-->'
            itr = itr.next
        
        print(qstr)



if __name__ == '__main__':
    q = Queue()
    q.print()
    print(q.head, q.tail)
    q.enqueue(1)
    q.print()
    print(q.head.data, q.tail.data)
    q.enqueue(2)
    q.print()
    print(q.head.data, q.tail.data)
    q.enqueue(3)
    q.print()
    print('Size', q.size())
    print(q.head.data, q.tail.data)
    print(q.dequeue())
    q.print()
    print(q.head.data, q.tail.data)
    print(q.dequeue())
    q.print()
    print(q.head.data, q.tail.data)
    print(q.dequeue())
    q.print()
    print(q.head, q.tail)
    print('Size', q.size())
    #q.dequeue()
    print('For fun\n==========')
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.print()
    print(f'head = {q.head.data}, tail = {q.tail.data}')
    q.reverse()
    q.print()
    print(f'head = {q.head.data}, tail = {q.tail.data}')
    q.enqueue(0)
    q.print()
    q.dequeue()
    q.print()   
