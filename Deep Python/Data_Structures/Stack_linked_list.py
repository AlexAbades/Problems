# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 15:23:00 2022

@author: G531
"""

# =============================================================================
# To implement a stack using singly linked list concept , all the singly linked 
# list operations are performed based on Stack operations LIFO(last in first out)
# 
# LIFO -> Last in First out
# Conceptual meaning: Pile of plates one on top of other.
# 
# Push:    Add an element to the top of a stack
# Pop:     Remove an element from the top of a stack
# IsEmpty: Check if the stack is empty
# IsFull:  Check if the stack is full
# Peek:    Get the value of the top element without removing it.
# 
#   Time: 
#     Push, Pop, isEmpty --> O(1)
# Space:
#     O(N)
# =============================================================================

#%% 


class Node():
    
    def __init__(self, value):
        # Creates a node for a linked list 
        self.key = value
        self.next = None
        self.prev = None 


class LinkedList_Stack():
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push(self, value):
        
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
            self.head.prev = None 
            
    def pop(self):
        if not self.head:
            print('Underflow')
            return False
        if not self.head.next:
            self.head = None
            return
        self.head = self.head.next 
        self.head.prev = None
        
        
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
        
        
        
        
L = LinkedList_Stack()
L.push(1)
L.display()
L.pop()
L.display()
L.push(0)

L.push(1)
L.display()
print(f'Value of first Node {L.head.key}, \n\tPointing to a: {L.head.next.key}'
      f'\n\t\tand the previous: {L.head.next.prev.key}')
L.push(2)
L.display()
print(f'Value of first Node {L.head.key}, \n\tPointing to a: {L.head.next.key}'
      f'\n\t\tand the previous: {L.head.next.prev.key}')
L.push(3)
L.display()
print(f'Value of first Node {L.head.key}, \n\tPointing to a: {L.head.next.key}'
      f'\n\t\tand the previous: {L.head.next.next.prev.key}')
L.push(4)
L.push(5)
L.display()
L.pop()
L.display()
