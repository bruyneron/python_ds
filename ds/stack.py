'''
Using Python Lists (Dynamic arrays) as Stack

    is_empty() - len(list) == 0
    push()     - list.append(2)
    pop()      - list.pop()
    peek()     - list[-1]
    size()     - len(list)
'''

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def push(self, data):
        self.head = Node(data, self.head)
    
    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')

        popped_item = self.head.data 
        # popped_item = self.head (Don't return node. If node is returned,
        # returned node can be used to traverse the entire stack)
        self.head = self.head.next
        return popped_item
    
    def peek(self):
        if self.is_empty():
            raise Exception('Stack is empty') 
            # Don't return, raise exception.
            # If None is returned then that indicates that stack top's `data` is None
        
        return self.head.data
    
    def size(self):
        size = 0

        if self.is_empty():
            return size
        
        itr = self.head
        while itr:
            size += 1
            itr = itr.next
        
        return size

    
    def print(self, sep='-->', top_marker='(top)'):
        if self.is_empty():
            print('Stack is empty')
            return
        
        itr = self.head
        stack_str = top_marker
        while itr:
            stack_str +=  str(itr.data) + sep
            itr = itr.next
        print(stack_str)

if __name__ == '__main__':
    stack = Stack()
    stack.print()
    print('Size =', stack.size())
    print(stack.is_empty())
    stack.push(1)
    stack.push(2)
    stack.print()
    print(stack.pop())
    stack.print()
    print(stack.pop())
    stack.print()
    #stack.pop()
    stack.push(112)
    stack.push(23)
    print('Stack peek =', stack.peek())
    stack.print()
    print('Size =', stack.size())

