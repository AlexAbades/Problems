# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 21:31:12 2022

@author: G531
"""

# =============================================================================
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
# =============================================================================

#%% No physical array ceated, we just keep track of tail and head 

class queue():
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.elements = []
        self.head = -1
        self.tail = -1
    
    def enqueue(self, data):
        if len(self.elements) < self.capacity:
            
            if self.head == -1:
                self.head += 1
                self.tail += 1
                self.elements.append(data)
                                    
            else:
                self.tail += 1
                self.elements.append(data)
                if self.tail > self.capacity:
                    self.tail = 0
                
        else:
            print('Overflow')
            return False
            
    def dequeue(self):
        if self.isEmpty():
            print('Underflow')
            # self.tail = -1
            # self.head = -1
            return False
        else:
            if self.head == self.tail and self.elements:
                return self.elements.pop(0)
            else:
                self.head +=1
            if self.head >= self.capacity:
                self.head = 0
            return self.elements.pop(0)
            
    def isEmpty(self):
        if self.head == self.tail and not self.elements:
            return True 
        else: 
            return False 
            
    def display(self):
        print(self.elements)
        
        
#%% 


q1 = queue(10)

q1.enqueue(1)
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')
q1.dequeue()
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')
q1.enqueue(1)
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')
q1.enqueue(2)
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')
q1.enqueue(3)
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')
q1.enqueue(4)
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')
q1.enqueue(5)
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')
q1.enqueue(6)
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')
q1.enqueue(7)
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')
q1.enqueue(8)
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')
q1.enqueue(9)
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')
q1.enqueue(10)
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.display()
q1.enqueue(11)
q1.display()
q1.dequeue()
q1.display()
q1.dequeue()
q1.display()
q1.dequeue()
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')
q1.display()
q1.dequeue()
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')
q1.dequeue()
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')
q1.enqueue(3)
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')
q1.dequeue()
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')
q1.dequeue()
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')
q1.dequeue()
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')

q1.enqueue(1)
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')
q1.dequeue()
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')
q1.enqueue(1)
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')
q1.enqueue(2)
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')
q1.enqueue(3)
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')
q1.enqueue(4)
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')
q1.enqueue(5)
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')
q1.enqueue(6)
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')
q1.enqueue(7)
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')
q1.enqueue(8)
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')
q1.enqueue(9)
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')
q1.enqueue(10)
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')

q1.enqueue(11)
q1.display()
print(f'Head {q1.head}, Tail {q1.tail}')
