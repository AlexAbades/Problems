# -*- coding: utf-8 -*-
"""
Created on Thu May 12 10:26:04 2022

@author: AlexAbades 

Maintain a dynamic family of sets supporting the following operations:
    Init(n): Set elements to be their own representative
    Union(i,j): If Find(i) != Find(j), update their own representative
    Find(i): Return the representative
        
"""

class UnionFind():
    
    def __init__(self, n):
        self.n = n
        self.sset = [{i} for i in range(n)]
        self.rep = [{i} for i in range(n)]
        
    def find(self, i):
        
        return self.rep[i]
        
    def union(self, i,j):
        
        iId = self.find(i)
        jId = self.find(j)
        
        if iId != jId:
            for k in range(self.n):
                if self.rep[k] == iId:
                    
                    self.rep[k] = jId
                    
            
        
        
        
        
        
    def disp(self):
        print('The set is: \n', self.sset)
        print('The respresentative array is:\n', self.rep)
       


a = UnionFind(10)
print(a.find(3))
a.union(2, 4)
a.disp()


#%% 

class QuickFind():
    """
    Mantains a tree structure in the unions, makes the union on the parent tree
    """
    
    
    
    def __init__(self, n):
        """
        Time Complexity O(n)
        Space complexity O(n)
        """
        self.n = n 
        self.p = [i for i in range(n)]
    
    def find(self,i):
        """
        The only one that has the same index is the root.
        Time Complexity O(d)
            Where d is the depth of the tree
        """
        while i != self.p[i]:
            i = self.p[i]
        return i
    
    def union(self, i,j):
        """
        Time complexity O(d)
            d-> Depth of the tree 
        Problem: The depth can be n, as it can happen that the 
        """
        
        root_i = self.find(i)
        root_j = self.find(j)
        
        if root_i != root_j:
            self.p[root_i] = root_j
        
    
    def disp(self):
        print(self.p)


a = QuickFind(10)
a.disp()
print(a.find(2))
a.union(3,2)
a.disp()


#%% 

class QuickFind():
    """
    Mantains a tree structure in the unions, makes the union on the parent tree
    """
    
    
    
    def __init__(self, n):
        """
        Time Complexity O(n)
        Space complexity O(n)
        """
        self.n = n 
        self.p = [i for i in range(n)]
        self.size = [i for i in range(n)]
    
    def find(self,i):
        """
        The only one that has the same index is the root.
        Time Complexity O(d)
            Where d is the depth of the tree
        """
        while i != self.p[i]:
            i = self.p[i]
        return i
    
    def union(self, i,j):
        """
        Time complexity O(d)
            d-> Depth of the tree 
        Problem: The depth can be n, as it can happen that the 
        """
        
        root_i = self.find(i)
        root_j = self.find(j)
        
        # Check that the root it's not the same in both trees, se we can join them
        if root_i != root_j:
            # Check The dimensions of the tree 
            if self.size[root_i] < self.size[root_j]:
                # If th brach i is smaller than the branh j, we join i to j
                self.p[root_i] = root_j
                self. size[root_j] += self.size[root_i]
            else:
                self.p[root_j] = self.p[root_i]
                self.size[root_i] += self.size[root_j]
        
    
    def disp(self):
        print(self.p)