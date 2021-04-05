

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None

    def purge(self):
        self.head = None

    def get_head(self):
        return self.head

    def get_length(self):
        length = 0
        
        itr = self.head
        while itr:
            length += 1
            itr = itr.next

        return length  

    def insert_at_beginning(self, data):
        '''
        2 cases:
        LL is empty                  None  |  29 --> None
        LL is not empty            1 2 3   |  29 --> 1 2 3
        '''
        node = Node(data, self.head) 
        self.head = node

    def insert_at_end(self, data):
        '''
        2 cases:
        LL is empty
        LL is not empty
        '''
        if self.head is None:
            self.head = Node(data, None) # self.insert_at_beginning(data) 
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        node = Node(data, None)
        itr.next = node  

    def insert_at(self, index, data):
        if index>self.get_length() or index<0: 
            # I can insert anywhere b/n 0 and length (Emphasis on length)
            # Inclusive of length value eventhough indexing starts with 0
            # ll = 1-->2--> | length = 2 | insert_at(2, 100) | insertion at the end
            raise Exception('Invalid index')

        if index==0:
            # Addresses 2 issues:
            # If one tries to insert at index 0, then 
            # for empty LL --> `while itr` ---> exits | No insertion
            # for non-empty LL --> count never == index-1 | No insertion
            self.insert_at_beginning(data)
            return

        itr = self.head 
        count = 0
        while itr:             # Don't check itr.next, need another if check to cover edge case. Use count var to stop at prev element
            if count==index-1:
                itr.next = Node(data, itr.next)
                return

            itr = itr.next
            count += 1 

    def insert_values(self, data_list):
        # if self.head is None:
        #     for data in data_list:
        #         self.insert_at_end(data)
        #     return

        # itr = self.head
        # while itr.next:
        #     itr = itr.next
        
        # for data in data_list:
        #     itr.next = Node(data, itr.next)
        for data in data_list:
            self.insert_at_end(data)               

    def purge_and_insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)               

    
    def delete_at(self, index):
        if index<0 or index>=self.get_length(): 
            # If LL is empty and 
            # if we try to remove 0th index, 
            # Invalid index error is thrown here
            # Empty LL is also kicked out
            raise Exception('Invalid index')
        
        # Only Non empty LL will come here
        if index==0:
            self.head = self.head.next 
            # Automatic garbage collector will free up the space that has gone out of scope
            return
      
        itr = self.head
        count = 0
        while itr:
            if count==index-1:
                itr.next = itr.next.next
                return

            itr = itr.next
            count += 1
        
    def reverse(self):
        if self.head is None:
            print('Linked list is empty')
            return
        
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            # Change links
            curr.next = prev

            # prepare data for next iteration
            prev = curr
            curr = next

        self.head = prev # DON'T FORGET TO MOVE HEAD
    
    def detect_loop(self):
        '''
        If there's no loop return None
        Else returns the meeting point based in Floyd's algorithm
        (Tortoise @1x and hare @2x algo)

        '''
        if self.head is None:
            return None
        
        slow = fast = self.head

        # SOLUTION 1: Beginner
        # if slow = fast = self.head, then following while loop will immediately break
        # To help while loop detect loop (the second time slow meets fast [1st time they meet is at the start i.e 0th position]),
        # do the 1st iteration
        '''
        if slow.next is not None:
            slow = slow.next
        else:
            return None     # No loop, ends with None
        
        if fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
        else:
            return None     # No loop, ends with None

        # Detect loop
        while (fast.next is not None) and \
              (fast.next.next is not None) and \
              (slow is not fast):
            #print(slow.data, fast.data, end=' => ') 
            slow = slow.next
            #print(fast.next.data, end=' => ')
            fast = fast.next.next
            #print(slow.data, fast.data)

        if fast.next is None or fast.next.next is None:
            return None
        
        if slow is fast:
            return slow
        
        # return None # Redundant
        '''

        # SOLUTION 2: Above solution with less lines code
        # Since slow = fast = self.head and because of that while loop breaks (Refer prev while loop)
        # 1) Check slow.next is fast.next.next. Then I don't have to do the 1st iteration. If slow.next = fast.next.next then break
        # 2) Check fast.next and fast.next.next exist. If one of them doesn't then there is no loop (ends with None). Break, as well from here
        # Note: I don't have to check if slow.next exists, because leading fast would've verified that
        while fast.next is not None and \
            fast.next.next is not None and \
                slow.next is not fast.next.next:
                slow = slow.next
                fast = fast.next.next
    
        if fast.next is None or fast.next.next is None:
            return None
            
        if slow.next is fast.next.next:
            return slow.next

        # return None # Redundant

    def get_loop_length(self):
        meeting_point = self.detect_loop()
        if not meeting_point:
            return 0
        
        loop_traverser = meeting_point
        count = 1
        
        while loop_traverser.next is not meeting_point:
            loop_traverser = loop_traverser.next
            count += 1
        
        return count
    
    def get_loop_start(self):
        meeting_point = self.detect_loop()
        if meeting_point is None:
            return None
        
        starter = self.head
        looper = meeting_point

        while starter is not looper:
            starter = starter.next
            looper = looper.next
        
        return starter 

    def remove_loop(self):
        traverser = loop_start = self.get_loop_start()
        if loop_start is None:
            return None
        
        while traverser.next is not loop_start:
            traverser = traverser.next
        
        traverser.next = None
        
    def print(self):
        '''
        2 cases:
        LL is empty
        LL is not empty
        '''
        if self.head is None:
            print('Linked list is empty')
            return

        itr = self.head
        llstr = ''

        while itr:
            #print(itr)
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

if __name__ == '__main__':
    ll = LinkedList()
    # print('length =', ll.get_length())
    ll.insert_at(0, 0)
    ll.print()
    ll.insert_at_end(100)
    ll.print()

    ll.insert_at_beginning(1)
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(3)
    ll.print()
    ll.insert_at(5, 5)
    ll.print()
    ll.insert_at(3, 'middle')
    ll.print()
    # ll.insert_at(100, 'error')
    print('length =', ll.get_length())

    ll.delete_at(6)
    ll.print()
    ll.delete_at(3)
    ll.print()
    ll.insert_values([])
    ll.print()
    ll.insert_values([1,2,3])
    ll.print()
    ll.purge_and_insert_values([234, 12, 'as'])
    ll.print()
    ll.reverse()
    ll.print()

    ll = LinkedList()
    # Set 1 
    ll.insert_values([1,2,3,4,5,6,7])
    ll.print()
    ll.head.next.next.next.next.next.next.next = ll.head.next.next.next.next # 1-->2-->3-->4-->5-->6-->7-->(5 of the same LL)
    print('Meeting point = ', ll.detect_loop().data)
    print('Length of the loop = ', ll.get_loop_length())
    print('Start of the loop = ', ll.get_loop_start().data)
    ll.remove_loop()
    ll.print() # No infinite loop now

    ll.purge()

    # Set 2
    ll.head = Node(1)
    ll.print()
    ll.head.next = ll.head # 1->itself
    print('Meeting point = ', ll.detect_loop().data)
    print('Length of the loop = ', ll.get_loop_length())
    print('Start of the loop = ', ll.get_loop_start().data)
    ll.remove_loop()
    ll.print() # No infinite loop now

