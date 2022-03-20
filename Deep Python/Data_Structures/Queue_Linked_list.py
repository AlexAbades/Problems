# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 17:05:27 2022

@author: G531
"""


# =============================================================================
# To implement a stack using singly linked list concept , all the singly linked 
# list operations are performed based on Stack operations 
# 
# FIFO -> First In First Out
# Conceptual: Que on a cinema, first that arruves first to get the tiquet 
# and first to get out the que
# 
# Enqueue:  Add an element to the end of the queue
# Dequeue:  Remove an element from the front of the queue
# IsEmpty:  Check if the queue is empty
# IsFull:   Check if the queue is full
# Peek:     Get the value of the front of the queue without removing it
# 
# Time:
#     Enqueue, Dequeue, isEmpty --> O(1)
# Space:
#     O(N)
# In order to implment the Linked List queue, we have to implment it with 
# inverse order, so when we dequeue the elemnt we won't have to searh linearly
# 
# =============================================================================


class Node():
    
    def __init__(self, value):
        self.key = value 
        self.next = None
        self.prev = None 



class LinkedList_Queue():
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, value):
        
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
            self.head.prev = None 
        
    def dequeue(self):
        if not self.tail:
            print('Underflow')
            return False
        if not self.head.next:
            self.tail = None
            self.head = None
            return
        self.tail = self.tail.prev 
        self.tail.next = None
        
        
    def isEmpty(self):
        if not self.head:
            return True
        else:
            return False
            
        
        
    def display(self):
        # Displays the key values of each node
        # Linear time O(n)
        n = self.head
        el = []
        if not n:
            return print(el)
        while n.next:
            el.append(n.key)
            n = n.next
        el.append(n.key)
        print(el)
        


L = LinkedList_Queue()
L.enqueue(0)
L.display()
L.enqueue(1)
L.display()
L.dequeue()
L.display()
L.enqueue(2)
L.enqueue(3)
L.enqueue(4)
L.enqueue(5)
L.display()
print(f'Head: {L.head.key} pointing to {L.head.next.key} \n'
      f'Tail: {L.tail.key} pointing to {L.tail.next} and {L.tail.prev.key}')
L.dequeue()
L.display()
print(f'Head: {L.head.key} pointing to {L.head.next.key} \n'
      f'Tail: {L.tail.key} pointing to {L.tail.next} and {L.tail.prev.key}')
L.dequeue()
L.display()
print(f'Head: {L.head.key} pointing to {L.head.next.key} \n'
      f'Tail: {L.tail.key} pointing to {L.tail.next} and {L.tail.prev.key}')
L.dequeue()
L.display()
print(f'Head: {L.head.key} pointing to {L.head.next.key} \n'
      f'Tail: {L.tail.key} pointing to {L.tail.next} and {L.tail.prev.key}')
L.dequeue()
L.display()
print(f'Head: {L.head.key} pointing to {L.head.next} \n'
      f'Teail: {L.tail.key} pointing {L.tail.prev} and {L.tail.next}')
L.dequeue()
L.display()
print(f'Head: {L.head} pointing to {L.tail}')

L.enqueue(0)
L.enqueue(1)
L.enqueue(2)
L.enqueue(3)
L.enqueue(4)
L.enqueue(5)
L.display()
L.dequeue()
L.display()










#%% 










class LinkedList_Queue():
    
    def __init__(self):
        # Stores the front node 
        self.head = None 
        # Stored the last node 
        self.tail = None 
    
    def isEmpty(self):
        if not self.head == self.head == None:
            return True
        else: 
            return False 
    
    def enqueue(self, val):
        # Insert a value at the begining of the linked list.
        # Running time: O(1). 
        # check if it's the first one or not 
        node = Node(val)
        
        if self.head == self.tail == None:
            self.head = self.tail = node
        else:
            self.head.prev = node
            node.prev = node
    
        

    def display(self):
        # Displays the key values of each node
        # Linear time O(n)
        n = self.head
        el = []
        while n.prev:
            el.append(n.key)
            n = n.prev
        el.append(n.key)
        print(el)
        
        
# TESTS    
L = LinkedList_Queue()
L.enqueue(0)
L.display()
L.enqueue(1)
L.display()
# L.enqueue(2)
# L.display()
# L.enqueue(3)
# L.display()


#%% 

class Node():
    
    def __init__(self, value):
        self.key = value 
        self.next = None
        self.prev = None 

class Queue:
     
    def __init__(self):
        self.front = self.tail = None
 
    def isEmpty(self):
        return self.front == None
     
    # Method to add an item to the queue
    def enqueue(self, item):
        temp = Node(item)
         
        if self.tail == None:
            self.front = self.tail = temp
            return
        self.tail.next = temp
        self.tail = temp
 
    # Method to remove an item from queue
    def dequeue(self):
         
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next
 
        if(self.front == None):
            self.tail = None



L = Queue()
L.enqueue(0)
L.display()
L.enqueue(1)
L.display()
# L.enqueue(2)
# L.display()
# L.enqueue(3)
# L.display()