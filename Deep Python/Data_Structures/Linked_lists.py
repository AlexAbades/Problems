# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 09:11:22 2022

@author: G531
"""
# =============================================================================
# 
# Normal list: Use a contiguous memory blocks to store reference to their data
# 
# Linked List: Store elements as part of their own elements. 
# Is a collection of nodes. The first node is called the head and it’s used as 
# the starting point for any iteration through the list. The last node must 
# have its next reference pointing to None to determine the end of the list.
# 
# OPERATIONS:
    # Node Search
    # Node Insert
    # Node Delete
# =============================================================================


class Node():
    
    def __init__(self, key):
        self.key = key
        self.next = None


class LinkedList():
    
    def __init__(self):
        self.head = None
        
        
# Initialize a Linked List  
L1 = LinkedList()

# Set the head of the Linked List to a node
L1.head = Node(1)
# Now the linked List has a node at the begining 

# Initialize a second Node 
a = Node(2)

# Link the second node to the Linked List 
L1.head.next = a

# Now we have a first node (head) with value 1, and a it's pointing to node "a"
# that has a value of 2 and points to None
print(f'Value of first Node {L1.head.key}, \n\tPointing to a: {L1.head.next == a}'
      f'\n\t\tThat has a value of: {a.key}')

# We add a third Node 
b = Node(3)

# Link the third Node with the Linked List
a.next = b 
print(f'Value of second Node {a.key}, \n\tPointing to Node b: {a.next == b}'
      f'\n\t\tThat has a value of: {b.key}')

c = Node(4)
b.next = c
print(f'Value of third Node {b.key}, \n\tPointing to Node c: {b.next == c}'
      f'\n\t\tThat has a value of: {c.key}')


#%% 

class Node():
    
    def __init__(self, key):
        self.key = key
        self.next = None


class LinkedList():
    
    def __init__(self):
        self.head = None
    

    def linearsearch(self, k):
        # Linear search of a value "k".
        # Return the pointer to this element. (node)
        # Running time: O(n)
    
        x = self.head
        while x!=None and x.key != k:
            x = x.next
        return x
    
    def insertnode(self, node):
        # Insert a node in the head of the list (at the begining), it shifts
        # everything to the right. 
        # Runing time: O(1)
        node.next = self.head
        self.head = node
        
    def insertval(self, val):
        # Insert a value at the begining of the linked list.
        # Running time: O(n)
        node = Node(val)
        node.next = self.head
        self.head = node
    
        
    def deletefirst(self):
        # Deletes a node given it's pointer. 
        # Running time: O(1)
        self.head = self.head.next
        
        
    def deletenode(self, node):
        # Deletes a given node from the linked list 
        # Running time: O(n)
        n = self.head
        while n.next != node:
            n = n.next
        n.next = node.next
        
        
    def deleteval(self, val):
        # Deletes a value in the list. If it's not in the list returns flase.
        # Running time: O(n)
        n = self.head
        
        while n.next.key != val:
            n = n.next
            if n:
                print(f'Value {val} not in Linked List')
                return False
        n.next = n.next.next
        
        # another aproach, time O(n^2)  
        # x = self.linearsearch(val)
        # self.deletenode(x)
        
        
    def display(self):
        # Displays the key values of each node
        # Linear time O(n)
        n = self.head
        el = []
        while n.next:
            el.append(n.key)
            n = n.next
        el.append(n.key)
        print(el)

    def appendval(self, k):
        node = Node(k)
        x = self.head
        while x.next:
            x = x.next
        print(x.key, x.next)
        x.next = node

 

## Test        
L1 = LinkedList()


L1.head = Node(1)
a = Node(2)
L1.head.next = a
b = Node(3)
a.next = b 
c = Node(4)
b.next = c

e = L1.linearsearch(4)
print(f'The node is: {e} and has a value of {e.key}')
d = Node(0)
L1.display()
L1.insertnode(d)
L1.display()
L1.deletefirst() 
L1.display()

L1.deletefirst() 
L1.display()
L1.insertval(8)
L1.display()
L1.deletenode(a)
L1.display()

L1.insertval(4)
L1.insertval(2)
L1.insertval(7)
L1.display()
L1.deleteval(8)
L1.display()
L1.insertval(5)
L1.insertval(6)
L1.display()
L1.appendval(10)
L1.display()               

    
#%% IMPLIMENT DOUBLE LINKED LIST WITH 



  
class Node():
    
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None 


class LinkedList():
    
    def __init__(self):
        self.head = None
        self.prev = None # It is necessary? 
    

    def linearsearch(self, k):
        # Linear search of a value "k".
        # Return the pointer to this element. (node)
        # Running time: O(n)
    
        x = self.head
        while x!=None and x.key != k:
            x = x.next
        return x
    
    def insertnode(self, node):
        # Insert a node in the head of the list (at the begining), it shifts
        # everything to the right. 
        # Runing time: O(1)
        
        node.next = self.head
        if self.head != None:
            self.head.prev = node
        self.head = node 
        node.prev = None

    def deletefirst(self):
        # Deletes a node given it's pointer. 
        # Running time: O(1)
        
        self.head = self.head.next   
        self.head.prev = None 
    
    def deletenode(self, node):
        # Deletes a given node from the linked list. 
        # node must be a pointer to the node we want to delete 
        # Running time: O(1)
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        
    
    def insertval(self, val):
        # Insert a value at the begining of the linked list.
        # Running time: O(1). 
        # check if it's the first one or not 
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            self.head.prev = node
            node.next = self.head 
            
            
            
        
        # self.head.prev = node
        # node.next = self.head
        # self.head = node
    
        
    def deleteval(self, val):
        # Deletes a value in the list. If it's not in the list returns flase.
        # Running time: O(n)
        n = self.linearsearch(val)
        self.deletenode(n)
        

    def appendval(self, k):
        node = Node(k)
        x = self.head
        while x.next:
            x = x.next
        print(x.key, x.next)
        x.next = node
        node.prev = x
        
        
    def display(self):
        # Displays the key values of each node
        # Linear time O(n)
        n = self.head
        el = []
        while n.next:
            el.append(n.key)
            n = n.next
        el.append(n.key)
        print(el)
   
# TESTS

L = LinkedList()
L.insertval(10)
L.display()
a = Node(0)
b = Node(1)
c = Node(2)
d = Node(3)
e = Node(4)
f = Node(5)
g = Node(6)
L.insertnode(a)
L.insertnode(b)
L.insertnode(c)
L.insertnode(d)
L.insertnode(e)
L.insertnode(f)
L.display()
#%%
    
L.deletenode(d)
L.display()   
L.deletenode(a)    
L.display()
L.deletenode(f)        
L.display()
L.insertval(10)
L.display()
L.deleteval(2)
L.display()
L.appendval(11)
L.display()
p = L.linearsearch(11)









