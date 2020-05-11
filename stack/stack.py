"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = list()
    
    def __len__(self):
        return len(self.storage)
    
    def is_empty(self):
        return len(self)==0
   
    def peek(self):
        if not self.is_empty():
            return self.storage[-1]

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if not self.is_empty():
            return self.storage.pop()

# Implementation of the Stack ADT using a singly linked list.
class Stack :
# Creates an empty stack.
    def __init__( self ): 
        self.top = None 
        self.size = 0
# Returns True if the stack is empty or False otherwise.
    def isEmpty( self ): 
        return self.top is None
# Returns the number of items in the stack.
    def __len__( self ): 
        return self.size
# Returns the top item on the stack without removing it.
    def peek( self ):
        if not self.isEmpty():
            return self.top.item
# Removes and returns the top item on the stack.
    def pop( self ):
        if not self.isEmpty():
            node = self.top
            self.top = self.top.next
            self.size -= 1
            return node.item
# Pushes an item onto the top of the stack.
    def push( self, value ) :
        self.top = StackNode( value, self._top ) 
        self.size += 1
# The private storage class for creating stack nodes.
class StackNode :
    def __init__( self, item, link ) :
        self.item = item 
        self.next = link
