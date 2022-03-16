# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 08:50:59 2022

@author: G531
"""
import time
import random
import matplotlib.pyplot as plt 

#%% FIND MAX WITH LINEAR DEPENDENCY ON TIME

# Generate a random array of integers of size n
n = 100
A = random.sample(range(100),n)



def findmax(A:list):
    m = 0
    for e in A:
        if e > m:
            m = e
    return m

s = []
x = []
for i in range(30):
    A = random.sample(range(5000),100*i)
    start = time.perf_counter()
    m = findmax(A)
    end = time.perf_counter()
    el_time =  end -start 
    s.append(el_time)
    x.append(100*i)

fig, ax = plt.subplots(1,1, figsize = (10,10), sharex=True, sharey=True)
ax.plot(x,s)

# We can see that with exeption of some outliers, the run time Big O will be as
# a function of n. cause the time we take to compare is a cte. 
# n*O(cte) = O(n)

#%%
def calctime(f, x):
    
    s = []
    x = []
    
    for i in range(30):
        A = random.sample(range(5000),100*i)
        # A.append(x)
        start = time.perf_counter()
        m = f(A,x)
        end = time.perf_counter()
        el_time =  end -start 
        s.append(el_time)
        x.append(100*i)
    fig, ax = plt.subplots(1,1, figsize = (10,10), sharex=True, sharey=True)
    ax.plot(x,s)
    return s,x
    
    

#%% Find an Element given an Array 

n = 100 
A = random.sample(range(100),n)
x = random.randint(0,100)


def findX(A:list,x:int):
    for i in range(len(A)):
        if A[i] == x:
            return i
        else:
            pass

a = findX(A,x)

x = random.randint(0,100)
s,x = calctime(findX, x)

# Again we can se that for the worst scenario, which will be that the number we
# lookng for it's at the end of the array the time will be n*O(cte) = O(cte)




#%%  Binary search with recursivity. Given a sorted array. 

n = 100 
A = random.sample(range(1000),n)
A.sort()
x = random.randint(0,100)

def BS(A,x):
    m = len(A)/2
    if A[m] == x:
        return m
    elif m < x:
        return BS(A[:m],x)
    else:
        return BS(A[m:], x)

s = BS(A,x)

# Prblem with the array, as it can be odd or even. Then when we calculate the 
# length of m and pass it as an argument for the recursivity, if the array is 
# odd, will give us a float and will crack.

#%% AS THE EXAMPLE: We pass to aditional arguments, first and last index


n = 99
A = random.sample(range(1000),n)
A.sort() 
# x = random.randint(0,1000)
x = A[60]
    
def binarysearch(A:list, i: int, j: int, x:int):

    if j < i:
        return False 
    # Get the middle f the array 
    m = int((i+j)/2) # Get only the integer part.

    if A[m] == x:  # just in the middle of the array
        print('The number has been found, it is: ', A[m])
        return m
    elif A[m] < x: # it shoud be in the left part as it's smaller.
        return binarysearch(A, m+1, j, x) # We pass m+1 as we want to check element 49 also 
    else: # it shoud be in the right part as it's bigger.
        return binarysearch(A, i, m-1, x) # We pass m-1 as we want to check element 49 also 


print(binarysearch(A, 0, len(A), x))
    
#%% Insertion Sort: Increasing order 


A = [33, 4, 25, 5, 20, 45]

def sorting(A, n):
    for i in range(n):
        j = i
        while j > 0 and A[j-1] > A[j]: # In the first loop it doesn't get in. 
        # Then we compare the element with the previous one. If it's bigger, we 
        # switch the elements, or e cast it behind
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1 # We rest one to get out of the buckle cause it will compare 
            # 2 elements that have been already sorted, so A[j-1] will be equal 
            # to A[j]

    return A

print(sorting(A, len(A)))



# Running time = n^2 --> foor loop + while loop 

#%% Insertion Sort: Decreasing order 


A = [33, 4, 25, 5, 20, 45]

def sorting(A, n):
    for i in range(n):
        j = i
        while j > 0 and A[j-1] < A[j]: # We just change the sign, so the 
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1 # We rest one to get out of the buckle cause it will compare 
            # 2 elements that have been already sorted

    return A

print(sorting(A, len(A)))


# Running time = n^2 --> foor loop + while loop 



#%%Merge Sort via recursivity 

# NOTICE NOTH ARRAYS ARE SORTED.

# A1 array 1
# n1 length of array 1
# A2 array 2
# n2 length of array 2

def merge2arr(A, A2, n1, n2):
    # Set Indexes 
    i = 0
    j = 0 
    k = 0
    
    # create an empty array 
    A3 = [None]*(n1+n2)
    
    # Create a while loop to iterate through the arrays
    while i < n1 and j < n2: # That would loop until both arrays have numbers.
    # At the moment one of the arrays it's finished it would stop
    
        if A[i] < A2[j]: # Means the element from array 1 it's smaller
        # We add it to the new array and we pass to the next element of the array 1
            A3[k] = A[i]
            k += 1
            i += 1
        else: # A[i] > A2[j]  Means the element of array 2 it's smaller 
        # We add it to the new array and we pass to the next element of the array 2
            A3[k] = A2[j]
            j += 1
            k += 1
    
    # Now we have the scenario where one of the arrays contained more smaller 
    # numbers so we have iterated throgh it faster:
    
    # Array 2 is finished: j = n2. We now the remaining elements of Array 1 are sorted 
    # We just iterate through the array 1 adding the elements into new array 
    while i < n1:
        A3[k] = A[i]
        i += 1
        k += 1
    
    # Array 1 is finished. Same approach as above
    while j < n2:
        A3[k] = A2[j]
        j += 1
        k += 1
    

    return A3


# Driver code :

A = [1, 3, 5, 7]
n1 = len(A)
A2 = [2, 4, 6, 8, 10]
n2 = len(A2)

A3 = merge2arr(A, A2, n1, n2)



#%% Approach with only one Array and with the specified middle 


def merge(arr, l, m, r):
    # Calculate the length of the arrays
    n1 = m - l + 1 # Middle minus the left index + 1 to as it's not inclusive
    n2 = r - m
    
    # Create empty arrays 
    L = [None] * n1
    R = [None] * n2
    
    # Create data into temporary array, we could do it like that, but at is 
    # only a python property we'll do it a for loop 
    # L1 = arr[:n1]
    # R1 = arr[n2+1:]
    for i in range(n1):  # Running time O(n
        L[i] = arr[l + i]
    for j in range(0, n2):  # Running time O(n)
        R[j] = arr[m + j+ 1]
    # Running time since here O(n + n)
    
    # Now we have to join the arrays in an ordered way 
    i = j = k = 0 
    while i < n1 and j < n2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
            k +=1
        else:
            arr[k] = R[j]
            j += 1
            k += 1
    
    # If R is empty 
    while i < n1:  # Running time O(n/2)
        arr[k] = L[i]
        i += 1
        k +=1
        
    # If L is empty 
    while j < n2:  # Running time O(n/2)
        arr[k] = R[j]
        j += 1
        k += 1
    
    # Running time since here O(n + n + n/2 + n/2) = O(3n) = O(n)

#%% MergeSort using merge algorithm 

arr = [1, 3, 5, 7, 6, 3, 8]
n = len(arr)


def mergeSort(arr, l, r):
    
    if l < r:
        # Find The middle
        m = l+(r-l)//2 
        
        # If there are arrays of more than one element call again 
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r) 
        #  Runing time recursivity -> O(nlog2n)
        # When l < r ENDs recursevity 
        merge(arr, l, m, r)  # Running time -> O(n)

    # Running time O(n + nlog2n) = O(n)
mergeSort(arr, 0, n-1)

#%%
    

def merge_sort(arr):
    
    # Check the length of the array 
    if len(arr) > 1:
            
        # First step, find the midle of the array:
        m = len(arr) // 2
        
        # Divide the array into 2 arrays, Left and right 
        L = arr[:m] # Last not iincluded 
        R = arr[m:]
        
        # Now we have to check if both arrays are 1 element list 
        # We do it calling again the merge sort funtion, as the first step is 
        # to check if the array length is bigger than 1.
        # Left 
        merge_sort(L)
        # Right 
        merge_sort(R) 
        # If L is ef length 1 we don't call recursivity there 
        # Same with R
        i = j = k = 0
        
        # The First Case will be when all the elements are splited
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k +=1 
        
        # Then we will face at some point 2 list where L is 2 elements and R 
        # is 1, or the other way arround. So at some point one list will be 
        # ended sooner
        # R is empty 
        while i < len(L):
            arr[k]=L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            
        
arr = [33, 4, 25, 5, 20, 45, 2, 23, 12, 1, 54, 34, 94]

merge_sort(arr)
 











