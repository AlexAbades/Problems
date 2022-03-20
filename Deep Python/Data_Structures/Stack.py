# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 20:56:18 2022

@author: G531
"""

# =============================================================================
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
#     Push, Pop, isEmpty --> O(n)
# Space:
#     O(N)
# =============================================================================

#%% Virtual capacity, we do not create the array of length N
class Stack:
    
    def __init__(self, capacity):
        self.elements = []
        self.top = -1
        self.capacity = capacity 


    def push(self, data):
        if self.top < (self.capacity-1):
            self.elements.append(data)
            self.top += 1
        else:
            print('Overflow')
    
    def pop(self):
        if self.top != -1:
            self.top -= 1
            return self.elements.pop()
        else:
            print('Underflow')
              
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    def display(self):
        print(self.elements)


s = Stack(10)
s.push(10)
s.push(3)
print(s.top)
s.pop()
print(s.top)
s.display()

s.push(4)
s.display()
s.push(10)
s.push(3)
s.push(10)
s.push(3)
s.push(10)
s.push(3)
s.push(10)
s.push(3)
s.display()
s.push(3)
s.display()
print(s.top)
s.pop()
s.pop()
s.pop()
s.pop()
s.display()
print(s.top)

#%% WAY 2 We create an array of length elements, length N

class Stack1:
    
    def __init__(self, capacity):
        self.elements = [None] * capacity
        self.top = -1
        self.capacity = capacity 

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    def push(self, data):
        if self.top < (self.capacity-1):
            self.top += 1
            self.elements[self.top] = data
            
        else:
            return 'Overflow'
    
    def pop(self):
        if self.isEmpty():
            return 'Underflow'
        else:            
            value = self.elements[self.top]
            self.top -= 1
            self.elements[self.top+1] = None 
            return value
              

    def display(self):
        print(self.elements)


c = Stack1(10)
c.display()
c.push(1)
c.push(2)
c.push(3)
c.push(4)
c.push(5)
c.push(6)
c.display()
print('Element popped: ', c.pop())
c.display()
print('Top: ', c.top)

print('Element popped: ', c.pop())
c.display()
print('Top: ', c.top)

