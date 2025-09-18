# *****************************************************

# Numpy 3 | AGENDA
# =====================
#   - Element wise operation
#       - Matrix multiplicaiton
#   - Shallow v/s Deep copy
#   - Splitting and Stacking

# ***********************************************************


# Element wise operation
'''
1.Element wise operation
=======================

'''

import numpy as np

a = np.arange(1,6)
print(a)
# [1 2 3 4 5]
print(a*5)
# [ 5 10 15 20 25]
print(a**2)
# [ 1  4  9 16 25]


b = np.arange(6,11)
print(b)
# [ 6  7  8  9 10]
print(b+2)
# [ 8  9 10 11 12]


# Multiply each element with index wise
print(a*b)
# [ 6 14 24 36 50]


c=np.arange(1,10)
print(c)
# [1 2 3 4 5 6 7 8 9]


# print(b*c)

# If the sizes of the array are different then it will raise error 
# when you are performing these operations the size of the array should be same


# 2D arrays element wise operations

d = np.arange(12).reshape(3,4)
e = np.arange(13,25).reshape(3,4)
print(d)

# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
print(e)
# [[13 14 15 16]
#  [17 18 19 20]
#  [21 22 23 24]]

print(d+e)
# [[13 15 17 19]
#  [21 23 25 27]
#  [29 31 33 35]]

print(d*e)
# [[  0  14  30  48]
#  [ 68  90 114 140]
#  [168 198 230 264]]

f = e.reshape(4,3)
print(f)

# [[13 14 15]
#  [16 17 18]
#  [19 20 21]
#  [22 23 24]]

# The shape should be same else it will raise the error
# print(d+f)

# The shape should be same else it will raise the error
# print(d+a)

g = np.arange(3)
print(g)
# [0 1 2]


# If the len of the 1D array is equal to the len of the col of 2D array
#  It the concept of broadcasting
print(f*g)
# [[ 0 14 30]
#  [ 0 17 36]
#  [ 0 20 42]
#  [ 0 23 48]]

h = np.arange(3).reshape(3,1)
print(h)
# [[0]
#  [1]
#  [2]]
print(d)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# It has the same no of rows so it is working
print(d*h)
# [[ 0  0  0  0]
#  [ 4  5  6  7]
#  [16 18 20 22]]

i = np.arange(8).reshape(2,4)
print(i)
# [[0 1 2 3]
#  [4 5 6 7]]

# ValueError: operands could not be broadcast together with shapes (3,4) (2,4)
# print(d+i)


print(sum(d))
# [12 15 18 21]
print(sum(e))
# [51 54 57 60]
print(sum(d+e))
# [63 69 75 81]

print(np.sum(d))
# 66
print(np.sum(e))
# 222
print(np.sum(d+e))
# 288





# Matrix Multplication
'''
Matrix Multplication
=====================
    - np.matmul()
    - np.dot()
    - a @ b ( python way of matrix multiplication -> python 3.5 onwards)

Consider 2 matrix with (r1,c1) and (r2,c2)
    - To perform matrix multiplication 
     the len of the col should be equal to no of the rows i.e c1==r2
    
    - The output of the matrix will be (r1,c2)


    
https://www.geogebra.org/m/ETHXK756

For Use case of matrix multiplication, you can check out the YT Channel (3Blue1Brown) on maths and its uses: https://youtu.be/XkY2DOUCWMU?si=_2A_J1nQWRdSepwk

'''

a = np.arange(1,13).reshape(3,4)
b = np.arange(2,14).reshape(4,3)

print(a)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
print(b)
# [[ 2  3  4]
#  [ 5  6  7]
#  [ 8  9 10]
#  [11 12 13]]

print(np.matmul(a,b))
# [[ 80  90 100]
#  [184 210 236]
#  [288 330 372]]


print(np.dot(a,b))
# [[ 80  90 100]
#  [184 210 236]
#  [288 330 372]]

print(a @ b)
# [[ 80  90 100]
#  [184 210 236]
#  [288 330 372]]

#Element wise multiple is not possible with np.matmul and a @ b, but possible using np.dot 
# print(np.matmul(a,5))
print(np.dot(a,5))
# [[ 5 10 15 20]
#  [25 30 35 40]
#  [45 50 55 60]]

print(np.matmul([2],[5]))
# 10
# print(np.matmul(2,5))
# It will raise error

print(np.dot(2,5))
# 10





# Shallow v/s Deep Copy
'''
Shallow v/s Deep Copy
======================
    - a shallow copy creates a new compound object (like a list or dictionary) but populates it with references to the child objects found in the original. 

    - A deep copy in Python creates a new, independent copy of an object, including all its nested objects. This means that any modifications made to the copied object or its nested elements will not affect the original object.


From AI:

In Python, copying objects can be done in two main ways: shallow copy and deep copy. The choice between them depends on whether you need a completely independent copy of an object, including its nested structures, or if sharing references to nested objects is acceptable.

Shallow Copy
============
A shallow copy creates a new compound object (like a list or dictionary) and then populates it with references to the child objects found in the original. It does not recursively copy the child objects themselves. 

Benefits:

    Efficiency: Shallow copies are generally faster to create and consume less memory than deep copies, as they only copy references, not the actual nested objects.

    Memory Savings: Multiple objects can share the same underlying data, which can be advantageous when working with large datasets or in memory-constrained environments.

Disadvantages:

    Unintended Modifications: Changes made to mutable nested objects in the copy will also affect the original object, and vice-versa, because both objects reference the same nested objects. This can lead to unexpected behavior and bugs if not handled carefully.

Deep Copy
=========
A deep copy creates a new compound object and then recursively copies all the child objects found in the original, creating entirely new instances for them. This ensures full independence between the original and the copied object.

Benefits:

    Data Isolation: Changes made to the copied object, including its nested structures, will not affect the original object. This provides complete data independence and prevents unintended side effects.

    Predictability: Ensures that the copied object is truly a separate entity, making code more predictable and easier to reason about, especially when dealing with complex data structures.

Disadvantages:

    Performance Overhead: Deep copies can be significantly slower and more memory-intensive than shallow copies, as they involve recursively copying all nested objects. This overhead can be substantial for large or deeply nested structures.

    Complexity with Custom Objects: For custom classes, you might need to define a __deepcopy__() method to control how deep copying behaves, especially when dealing with circular references.

When to Use Which:

    Shallow Copy: Use when dealing with immutable objects (like numbers, strings, tuples) within your compound object, or when you explicitly want changes in nested mutable objects to be reflected in both the original and the copy.

    Deep Copy: Use when working with mutable nested objects and you need complete independence between the original and the copied object, ensuring that modifications to one do not impact the other. This is crucial for maintaining data integrity in complex scenarios.
'''
# Example from AI

import copy

original_list = [[1, 2], 3]

# Shallow copy
shallow_copied_list = copy.copy(original_list)
shallow_copied_list[0].append(4)
print(f"Original after shallow copy modification: {original_list}") # Output: [[1, 2, 4], 3]

# Deep copy
deep_copied_list = copy.deepcopy(original_list)
deep_copied_list[0].append(5)
print(f"Original after deep copy modification: {original_list}") # Output: [[1, 2, 4], 3]





l1 = [1,2,3,4]
l2 = l1
print(id(l1),id(l2))
# 1848885005568 1848885005568
# l2 will be pointing to the l1 and copy won't be created

l2 = l1.copy()
print(id(l1),id(l2))
# 1848885005568 1848885005184
# A new list will be created 











# Splitting
'''
Splitting 
==========
Splitting:
    - If we have large array we are splitting them into  smaller array

    Usecase: by performing calculation on large data set



'''

a = np.arange(9)
print(np.split(a,3))
# [array([0, 1, 2]), array([3, 4, 5]), array([6, 7, 8])]


# print(np.split(a,4))

# Uneven split
print(np.split(a,(3,6,7)))
# [array([0, 1, 2]), array([3, 4, 5]), array([6]), array([7, 8])]

# 2D array
a = np.arange(16).reshape(4,4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]

print(np.split(a,2))
# [array([[0, 1, 2, 3], [4, 5, 6, 7]]), array([[ 8,  9, 10, 11], [12, 13, 14, 15]])]


print(np.split(a,2,axis=0))
# [array([[0, 1, 2, 3], [4, 5, 6, 7]]), array([[ 8,  9, 10, 11], [12, 13, 14, 15]])]

print(np.split(a,2,axis=1))
# [array([[ 0,  1],
#        [ 4,  5],
#        [ 8,  9],
#        [12, 13]]), 
# array([[ 2,  3],
#        [ 6,  7],
#        [10, 11],
#        [14, 15]])]

'''
Slicing:
    Will give you sub array
Spliting:
    Will split your original array into multiple smaller ones
'''


# How to access these arrays after spliting?



#====================================
# Stacking
'''
Stacking
=========
'''

a = np.arange(5)
b = np.arange(5,10)
print(a)
# [0 1 2 3 4]
print(b)
# [5 6 7 8 9]

print(np.vstack((a,b)))
# [[0 1 2 3 4]
#  [5 6 7 8 9]]

print(np.hstack((a,b)))
# [0 1 2 3 4 5 6 7 8 9]


# Quiz 1
# What will be the output of following code?
a = np.array([[1], [2], [3]])
b = np.array([[4], [5], [6]])
np.hstack((a, b))
'''
A. [[1]
    [2]
    [3]
    [4]
    [5]
    [6]]

B. [[1 2]
    [3 4]
    [5 6]]

C. [[4 1]
    [5 2]
    [6 3]]

D. [[1 4]
    [2 5]
    [3 6]]

'''
# Ans : D



#===========================================================================
# Assignment Questions
#===========================================================================

# Q1. Matrix elements

# What will be the outcome of the following code snippet ?

x = np.ones((5,5))
x[1:-1,1:-1] = 0


'''
Choose the correct answer from below:
1.All the elements except those at the border are equated to zero.

2.All the elements at the border are equated to zero.

3.All the elements in the first and last columns are equated to zero.

4.All the elements in the first and last rows are equated to zero.
'''
# Ans : 1

#==========================================================================


# Q2. Specific elements
'''
Problem Statement:

Given two 2D arrays, row and column ranges,

Perform the following operations:

Find the matrix multiplication of the given two matrices and
Extract the elements from the output of above step using the given ranges
If matrix multiplication is not possible, return -1
Note: The end points (upper range) of both rows and columns are excluded.

Input Format:

There will be four lines of input as follows:  
First line will have mat1.  
Second line will have mat2.  
Third line will have two space-separated integers representing start and end point of rows.  
Fourth line will have two space-separated integers representing start and end point of columns.
Output Format:

A Numpy array
Sample Input:

[[6 6 4 7 9]  
 [0 2 2 9 3]  
 [6 0 2 5 2]  
 [2 4 3 5 5]]  
[[8 6 6 8 3]  
 [2 7 0 3 1]  
 [3 2 1 5 2]  
 [7 0 7 6 8]  
 [1 5 6 4 5]]  
1 3  
2 4
Sample Output:

[[83 82]  
 [85 96]]
Sample explanation:

The dimension of product is (5,5), and the elements for rows 1 to 4 and columns 2 to 4 are prd[1][2], prd[1][3], prd[2][2] and prd[2][3] i.e. 83, 82, 85 and 96.

'''

import numpy as np
def specific_elements(mat1,mat2,r1,r2,c1,c2):
    '''mat1,mat2 are the two 2d numpy array.
       r1,r2 are the start and end of rows indices
       c1,c2 are the start and end of columns indices
       Output = Return a numpy array according to indices'''
    
    # STEP1 CHECK whether matrix multiplication is possible
    
    if mat1.shape[1]!=mat2.shape[0]:
        return -1
    ## STEP 2 Perform matrix multiplication
    
    matmul_array = np.matmul(mat1,mat2)
    
    ## STEP 3 slice the array based on range value
    
    result = matmul_array[r1:r2,c1:c2]
    
    return result



#===========================================================================


# Q3. Sort the birds
'''

Problem Description:

Given a list of birds and their corresponding age, return the name of birds sorted according to age (ascending)
Input Format:

Two 1D array list i.e. bird array and age array
Output Format:

A 1D array
Sample Input:

birds = ['spoonbills',  'plovers',  'plovers',  'plovers',  'plovers',  'Cranes',  'plovers',  'plovers',  'Cranes',  'spoonbills']
age = [5.5, 6.0, 3.5, 1.5, 3.0, 4.0, 3.5, 2.0, 5.5, 6.0]
Sample Output:

['plovers', 'plovers', 'plovers', 'plovers', 'plovers', 'Cranes', 'spoonbills', 'Cranes', 'plovers', 'spoonbills']
Side Note: Recall the functionality of .sort() and .argsort()

'''

import numpy as np

def sort_birds(birds, age):
    '''
    INPUT: birds, age -> 1D numpy array
    
    OUTPUT: result -> sorted bird 1D array
    '''
    
    ## STEP 1 : Get the sorted index of age.
    
    sorted_age_index = age.argsort()
    
    ## STEP 2: Use the index from previous step to get sorted birds
    # print(sorted_age_index)
    result = birds[sorted_age_index]

    # print(result)
    return result


#===========================================================================

# Q4. Add padding
'''
Given a NumPy array of shape (n,m). Add padding of a layer of 0’s on all 4 boundaries of the matrix.

Input Format:

First line will be consisting of two space-separated integers representing n and m.  
There will be n lines of input consisting of m space-separated integers representing the elements of rows of the array.
Output Format:

A 2d numpy array.
Sample Input:

3 2  
1 2  
3 4  
5 6
Sample Output:

[[0 0 0 0]
 [0 1 2 0]
 [0 3 4 0]
 [0 5 6 0]
 [0 0 0 0]]
'''

import numpy as np
def add_padding(mat):
    '''mat-> NumPy array
       output-> NumPy array is expected to be returned'''

    # YOUR CODE GOES HERE
    # Working coding comment for 2nd version
    # n = mat.shape[0]
    # m = mat.shape[1]
    # n1 = n+2
    # m1 = m+2
    # empty = np.zeros((n1*m1),dtype=int).reshape(n1,m1)
    # empty[1:-1,1:-1]=mat
    # res = empty

    res = np.pad(mat,1)
    
    return res


#===========================================================================
# Q5. Column split

'''
Given an MxN 2D array (M >= 4),

Split the array column wise such that,

1st sub array contains the first 2 columns
2nd sub array contains the 3rd column
3rd sub array contains the rest of the columns
Input Format:

A 2D array
Output Format:

List of arrays
Sample Input:

[[0, 1, 2, 3],
 [4, 5, 6, 7],
 [8, 9, 10, 11],
 [12, 13, 14, 15],
 [16, 17, 18, 19],
 [20, 21, 22, 23]]
Sample Output:

[
array([[ 0,  1],
       [ 4,  5],
       [ 8,  9],
       [12, 13],
       [16, 17],
       [20, 21]]), 
array([[ 2],
       [ 6],
       [10],
       [14],
       [18],
       [22]]), 
array([[ 3],
       [ 7],
       [11],
       [15],
       [19],
       [23]])]
Output explanation:

Here, the first sub-array contains the first two columns of the input array.
Second sub-array contains the third column of the input array.
Third sub-array contains the rest of the columns, i.e the fourth column of the input array.
'''

import numpy as np

def split(arr):
    '''
    INPUT: arr -> 2D array
    
    OUTPUT: subarrays -> list of 2D arrays
    '''
    
    subarrays = np.split(arr,[2,3],axis=1)
    ### CODE starts here 
    
    
    
    return subarrays


#===========================================================================
# Q6. Split second
'''

Problem statement:

Given an 1D array and an integer k that specifies the number of equal parts to split the array into,

Perform the following operations:

Split the array into k number of equal parts.
Return the list of split arrays.
Assumption: The array can be split into k equal parts

Note: Recall how to split an array into equal parts.

Input Format:

Line separated numpy array and split count 
Output Format:

List of numpy arrays
Sample Input:

arr = [0,1,2,4,5,6,7,8]
k = 3
Sample Output:

[array([0, 1, 2]), array([3, 4, 5]), array([6, 7, 8])]
'''

import numpy as np

def split(arr, k):
    '''
    INPUT: arr, k
    
    OUTPUT: split_arr -> list of arrays
    '''
    
    split_arr = np.split(arr,k)
    
    ## CODE starts here
    
    
    
    return split_arr


#==========================================================================

# Q7. Wise split

'''

What will be the output of following code?

import numpy as np
arr = np.arange(16).reshape(4,4)  
print(np.split(arr,4))
A.

Error
B.

[array([[ 0, 4, 8, 12]]),
 array([[ 1, 5, 9, 13]]),
 array([[ 2, 6, 10, 14]]),
 array([[ 3, 7, 11, 15]])]
C.

[array([[0, 1, 2, 3]]),
 array([[4, 5, 6, 7]]),
 array([[ 8, 9, 10, 11]]),
 array([[12, 13, 14, 15]])]
D.

[array([[1, 2, 3, 4]]),
 array([[5, 6, 7, 8]]),
 array([[ 9, 10, 11, 12]]),
 array([[13, 14, 15, 16]])]
'''

# Ans : C


#===========================================================================
# Q8. Filter Copy

'''
Which of the following will return a deep copy of array?

arr = np.array([1,2,3,0,-2,4])

A. arr1 = arr*1


B. arr1 = arr[:]


C. arr1 = arr[arr > 0]


D. arr1 = arr.reshape(2,3)
'''
# Ans : A,C


#===========================================================================
# Additional Problems
#===========================================================================





# Q1. Dot Dot Dash
'''
Which of the following code will NOT throw an error?

A.

arr1 = np.array([1,2,3])
arr2 = np.array([9,8,7])
np.dot(arr1, arr2)

B.

arr1 = np.array([[1,2], [3,4]])
arr2 = np.array([[1], [2]])
np.dot(arr1, arr2)

C.

arr1 = np.array([1,2,3])
k = 3
np.dot(arr1, k)

D.

arr1 = np.array([[1,2], [3,4]])
arr2 = np.array([1,1])
np.dot(arr1, arr2)
'''
# Ans :A, B, C, D



#===========================================================================

# Q2. Swappers

# What would the following code do?

import numpy as np
A = np.arange(9).reshape(3,3)
print(A[:, ::-1])

'''
Choose the correct answer from below:
Reverse the rows of a 2D array A

Reverse the columns of a 2D array A

Reverse both rows and columns of a 2D Array A

None of the above
'''
# Ans : 2


#===========================================================================

# Q3. Oldest bird

'''

Given a array of bird names and another array with corresponding ages of the birds, find the name of the oldest bird in the list.

Input Format:

Input has two lines.
First line is the array of bird names (String).
Second line is the array of ages of the birds (Int).
Output Format:

string
Sample Input:

['sparrow', 'peacock', 'parrot', 'owl', 'peacock', 'macaw', 'macaw', 'parrot', 'macaw', 'peacock']  
[6, 1, 6, 5, 7, 6, 0, 9, 0, 7]
Sample Output:

parrot
Explanation:

parrot has age 9 which is the max of all the ages in the array; therefore parrot is returned.
Note:

Recall how to get index of maximum element
'''


import numpy as np
def oldest_bird(birds, age):
    ''' birds[i] consist of the names of the type of ith bird
        age[i] consist of the age of ith bird'''
        
    ## STEP 1: Get the index of maximum age element
    
    # It is also working but commenting for 2nd version
    # max_age_index = np.argsort(age)[-1]

    max_age_index = np.argmax(age)
    
    
    ## STEP 2: Get the bird with maxium age using the above index
    
    old_bird = birds[max_age_index]
    
    
    return old_bird


#===========================================================================

# Q4. Inter dimension

'''
Given a 3D array of shape (2, 3, 3)


array([[[ 0, 1, 2],
        [ 3, 4, 5], 
        [ 6, 7, 8]], 

        [[ 9, 10, 11], 
         [12, 13, 14], 
         [15, 16, 17]]])

What will be the output of arr[1, :, :] ?

A.

array([[ 3, 4, 5], 
       [12, 13, 14]])

B.

array([[ 9, 10, 11], 
       [12, 13, 14], 
       [15, 16, 17]])

C.

array([[ 1, 4, 7], 
       [10, 13, 16]])

D.

array([[0, 1, 2], 
       [3, 4, 5], 
       [6, 7, 8]])
'''
# Ans : 2


#==========================================================================
# Q5. Hstack

# Given the following array:

import numpy as np
arr = np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
# Which options are correct?

# Note: np is the alias for NumPy in the options.

'''

Choose the correct answer from below, please note that this question may have multiple correct answers
2 Attempts left

np.hstack((arr, arr[:, 0])).shape = (3, 4)


np.hstack((arr, arr[:, [0]])).shape= (3, 4)


np.hstack((arr, arr[:, [0]])).shape= (4, 3)


np.hstack((arr,arr[:, 0])) => Throws Error
'''

# Ans : 2,4

#==========================================================================
# Q6. Split and cycle


'''
You are given the following:

A 2D Numpy array (data) representing a grayscale image, where pixel values range from 0 (black) to 255 (white).
A desired number of horizontal splits (num_splits).
Tasks:

Split the image to divide the image array (data) evenly into num_splits horizontal sections.
Rearrange sections: Create a new array by concatenating the image sections in the following order:
The last section moves to the first position.
All other sections shift downwards by one position.
Return the modified array
Input format:

data: np.array
num_splits: int
Output format:

np.array
Input Sample

data = np.array([[10, 20, 30],
                 [40, 50, 60],
                 [70, 80, 90],
                 [100, 110, 120]])

num_splits = 2
Output Sample

[[ 70  80  90]
 [100 110 120]
 [ 10  20  30]
 [ 40  50  60]]
'''


def rearrange_image(data, num_splits):
    # write your code here

    res = np.split(data,num_splits,axis=0)
    # print(res)
    res = res[-1:]+res[:-1]
    # print(res)
    res = np.vstack(res)
    return res