"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = list()
    def isEmpty(self):
        return len(self)==0
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if not self.isEmpty():
           return self.storage.pop(0)


'''
class Queue:
    def __init__(self):
        self.qhead = None
        self.qtail = None
        self.size = 0
    def isEmpty(self):
        return self.qhead is None
    def __len__(self):
        return self.size
    def enqueue(self,value):
        node = QueueNode(value)
        if self.isEmpty():
            self.qhead = node
        else:
            self.qtail.next = node
        self.qtail = node
        self.size += 1

    def dequeue(self):
        if not self.isEmpty():
            node =self.qhead
        if self.qhead is self.qtail:
            self.qtail = None
            self.qhead = self.qhead.next
            self.count -=1
            return node.value
class QueueNode():
    def __init__(self,value):
        self.value = value
        self.next = None

'''