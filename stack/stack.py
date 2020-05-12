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
'''
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

'''


from link_list import Node,LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size
    
    def push(self,value):
        self.storage.add_to_end(value)
        self.size +=1

    def pop(self):
        if not self.storage.head:
            return None
        else:
            self.size -= 1
            return self.storage.remove_from_end()
