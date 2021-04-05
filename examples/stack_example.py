import sys
import os
sys.path.append(os.path.dirname(os.path.dirname( os.path.abspath(__file__))))
from ds.stack import Stack

if __name__ == "__main__":
    string = 'This will be reversed'
    stack = Stack()

    for s in string:
        stack.push(s)

    stack.print(sep='', top_marker='')
