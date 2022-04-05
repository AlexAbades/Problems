# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 16:09:34 2022

@author: G531
"""

# =============================================================================
# A dynamic array is similar to an array, but with the difference that its size 
# can be dynamically modified at runtime. 
# In a normal array we have to specify the  apacity of the array. See Stacks or 
# Queues
# The elements of an array occupy a contiguous block of memory, and once created,
# its size cannot be changed.
# How it works?
# Once the original array is filled, it creates a new array and copies the
# elements of the old array to the new one. Then deletes the old array 
# =============================================================================

#%%  Nomral Array 

class Array():
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.idx = 0
        self.array = [None]*self.capacity
        
    def append(self, value):
        if self.idx < self.capacity:
            self.array[self.idx] = value 
            self.idx += 1
        else:
            print('Overflow')
            return False
    def pop(self):
        if self.idx:
            self.idx -=1
            self.array[self.idx] = None
            
            return
        else: 
            print('Underflow')
            return False 
    
    def isEmpty(self):
        if self.idx:
            return False
        else:
            return True
    
    def display(self):
        return print(self.array)



L = Array(10)
L.display()
L.append(5)
L.display()
L.append(5)
L.append(5)
L.append(5)
L.append(5)
L.append(5)
L.append(5)
L.append(5)
L.append(5)
L.append(5)
L.display()

L1 = Array(11)








#%% Dynamic Array 


class DynamicArray():
    
    
    def __init__(self):
        
        self.arraycapacity = 0
        self.arrayidx = 0
        self.elements = Array(self.arraycapacity)
    
    def append(self, value):
        if self.arraycapacity == self.arrayidx:
            self.arraycapacity += 1
            self.arrayidx += 1
            new = Array(self.arraycapacity)
            new.array[:self.arraycapacity-1] = self.elements.array[:]
            new.array[self.arraycapacity-1] = value
            self.elements = new
        else:
            self.elements.array[self.arrayidx] = value
            self.arrayidx += 1
        
    def pop(self):
        if self.arrayidx:
            self.elements.array[self.arrayidx-1] = None
            self.arrayidx -= 1
        else:
            print('Underflow')
            return False
        
        
        
        
    def display(self):
        return print(self.elements.array)
    
    
    
    
L = DynamicArray()
L.display()
L.append(10)
L.display()
L.append(11)    
L.display()
L.append(15)
L.display()    
L.append(16)
L.display()    
L.pop()
L.display()
L.append(9)
L.display()
L.append(32)
L.display()
L.append(56)
L.display()
L.pop()
L.pop()
L.display()
L.append(10)
L.display()
L.pop()
L.pop()
L.pop()
L.pop()
L.display()
L.pop()
L.display()

L.pop()
#%% Dynamic array 2

class DynamicArray2():
    
    def __init__(self):
        
        self.arraycapacity = 0
        self.arrayidx = 0
        self.elements = Array(self.arraycapacity)
    
    def append(self, value):
        if self.arraycapacity == self.arrayidx:
            if not self.arraycapacity:
                print('hhehehe')
                self.arraycapacity += 1
                self.arrayidx += 1
                new = Array(self.arraycapacity)
                new.array[:self.arraycapacity-1] = self.elements.array[:]
                new.array[self.arraycapacity-1] = value
                self.elements = new
            else:
                self.arraycapacity *= 2
                self.arrayidx += 1
                print(self.arraycapacity)
                new = Array(self.arraycapacity)
                new.array[:self.arrayidx-1] = self.elements.array[:]
                new.array[self.arrayidx-1] = value
                self.elements = new
        else:
            print('hahashs')
            self.elements.array[self.arrayidx] = value
            self.arrayidx += 1
        
    def pop(self):
        if self.arrayidx:
            self.elements.array[self.arrayidx-1] = None
            self.arrayidx -= 1
        else:
            print('Underflow')
            return False
        
        
        
        
    def display(self):
        return print(self.elements.array)
    
    
    
    
    

    
L = DynamicArray2()
L.display()
L.append(5)
L.display()    
L.append(8)
L.display()  
L.append(9)
L.display()      
L.append(10)
L.display()      
L.append(11)
L.display()   
L.append(12)
L.display()   
L.append(13)
L.display()   
L.append(14)
L.display()   
L.pop()
L.display()
L.pop()
L.display()
L.pop()
L.display()
L.pop()
L.display()
L.append(5)
L.display()
      
    
    
