

# *****************************************************

# Numpy 1 | AGENDA
# =====================
#   - Intro to DAV
#   - Use case (NPS)
#   - Python lists vls Numpy arrays
#   - Why to use Numpy
#   - Indexing
#   - NPS case study


# ***********************************************************


# 1.Intro to DAV
'''
1.Intro to DAV
===============
(Data analysis and visualization)
    - DAV 1
        - Python Libraries
            1.Numpy
            2.Pandas
            3.Matplotlib
            4.seebom
    - DAV 2
        - Probability and Statistics
    - DAV 3
        - Hypothesis Testing

Note : It will take around 3 months to cover the above the topics
'''



# Numpy

l = [1,2,3,"Nishant",True,1.3]
print(type(l))
# <class 'list'>


'''
Python list:
    - list are heterogeneous in nature
    - In a list you can have more than one data type in one list
    - It is slower
    - location is stored instead of data
    
Numpy Arrays:
    - Array are homogeneous in nature
    - It have same kind of data in an array
    - Numerical computation
    - It is faster
    - Continuous memory allocation will be there
    - Implementation of Numpy library is done using C

    
How to define Numpy?
    - We cannot directly use Numpy we need to import and use
    

In C we need to write 100 lines of code but in python 10 lines code why?
    - In backend python need to do some extra work in backend, so it will take some time so it is slower


'''
# pip install numpy

import numpy as np

# python list
a = [1,2,3,4,5]
print(type(a))

# numpy array
b = np.array([1,2,3,4,5])
print(type(b))
#<class 'numpy.ndarray'>


# Speed comparison
#==================
print([i**2 for i in a]) 
#[1, 4, 9, 16, 25]

print(b**2) 
# [ 1  4  9 16 25]
# This is possbile due to parallel processing


import timeit

def myfunc():
    l = range(10000)
    return [i**2 for i in l]
time_taken = timeit.timeit('myfunc()',setup='from __main__ import myfunc', number=1)
print(time_taken)


def myfunc1():
    np_l = np.array(range(10000))
    return [i**2 for i in np_l]

time_taken = timeit.timeit('myfunc1()', setup='from __main__ import myfunc1',number=1)
print(time_taken)



# Dimensions and Shape
#========================

arr = np.array(range(10))
print(arr)
# [0 1 2 3 4 5 6 7 8 9]
print(arr.ndim)
# 1
print(arr.shape)
(10,)

arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1.ndim)
# 2
print(arr1.shape)
# (3, 3)

arr2 = np.array([[1,2,3,11],[4,5,6,10],[7,8,9,12]])
print(arr2.ndim)
# 2
print(arr2.shape)
# (3,4)


arr3 = np.array([[1],[2],[3],[4]])
print(arr3.ndim)
# 2
print(arr3.shape)
# (4, 1)



#Quiz 1
a = np.array([1,2,3,4,5,6,7,8])
print(a.ndim,a.shape)
# 1 (8,)


a = np.array([[1,2,3,4,5,6,7,8]])
print(a.ndim,a.shape)
# 2 (1, 8)




#Arange
#===============

# In range it takes only integers
print(list(range(1,100)))


# Starting Point (inclusive)
# Ending Point (Exclusive)
# Jump 


# Im arange it also takes decimal values
ar = np.arange(1,5,2)
print(ar)
# [1 3]

print(np.arange(1,10,1.2))
# [1.  2.2 3.4 4.6 5.8 7.  8.2 9.4]

print(np.arange(1.5,11.2,1.2))
# [ 1.5  2.7  3.9  5.1  6.3  7.5  8.7  9.9 11.1]




# Type Conversion
# ================

# Array are homogeneous in nature
# Can take one type of data type 

a = np.array([1,2,3,4.0])
print(a)
# [1. 2. 3. 4.]
# Here integers and float are defined in array
# As the float has more precedence then the integer the integers are converted to float


s = np.array(["Rahul", 1, 2])
print(s)
# ['Rahul' '1' '2']

# All the values will be converted into the string

print(s.dtype)
# <U21
# 21 character for each value in array


s = np.array(["Rahul", 1, 2, 4.5])
print(s)
# ['Rahul' '1' '2' '4.5']
print(s.dtype)
# <U32
# 32 -> characters for each value in array


a = np.array([1,2,3,4.5],dtype=int)
print(a)
# [1 2 3 4]
# here we are converting the float to int

# But you cannot convert the string into integer or floar it will raise error

a = np.array([1,2,3,4],dtype = float)
print(a)
# [1. 2. 3. 4.]
# converting int to float

# Order of precedence
# int -> float -> String



# Indexing
# ============


m1 = np.arange(10)
print(m1)
# [0 1 2 3 4 5 6 7 8 9]

print(m1[0])  # 0

# Negative index start from last element
print(m1[-1]) # 9


print(m1[[1,2,3,1,2,4]])
# [1 2 3 1 2 4]
# Can able to fetch multiple values using multiple index


# print(m1[1,2,3,1,2,4])
# Will not work
# We need to pass 2 brackets


m = np.array([100,200,400,300,500])

print(m) 
# [100 200 400 300 500]
print(m[1])
# 200
print(m[2])
# 400
print(m[[1,2,3,1,2,1]])
# [200 400 300 200 400 200]




# Slicing of array
# ====================


print(m1)
# [0 1 2 3 4 5 6 7 8 9]

# Get first 5 elements
print(m1[:5])
# [0 1 2 3 4]

print(m1[-5:-1])
# [5 6 7 8]

print(m1[-5:-1:-1])
# []


a = np.array([1,2,5,4,3,6,7])
print(a[4:])
# [3 6 7]

a[4:] = 12
print(a)
# [ 1  2  5  4 12 12 12]


# Quiz 2
a = np.array([0,1,2,3,4,5])
a[4:] = 10
print(a)
# [ 0  1  2  3 10 10]





# Reshaping
# ============
# It is creating a new array, it is not changing the original array

a = np.array(range(16))
print(a)
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]

print(a.ndim)
# 1
print(a.shape)
# (16,)

# Converting 1D array to 2D array
print(a.reshape(8,2))
# [[ 0  1]
#  [ 2  3]
#  [ 4  5]
#  [ 6  7]
#  [ 8  9]
#  [10 11]
#  [12 13]
#  [14 15]]

print(a.reshape(2,8))
#[[ 0  1  2  3  4  5  6  7]
#  [ 8  9 10 11 12 13 14 15]]

print(a.reshape(2,8).ndim)
# 2

print(a.reshape(8,-1))
# [[ 0  1]
#  [ 2  3]
#  [ 4  5]
#  [ 6  7]
#  [ 8  9]
#  [10 11]
#  [12 13]
#  [14 15]]

# The reshape will automatically make reshape based on the positive integer and ignores -1

# print(a.reshape(-1,-1))
# If both are -1 then it will raise error

# print(a.reshape(5,-1))
# Also the postive integer must be a factor of the length of array



# Transpose
# ============
# It will convert the row to column and viceversa (3,4) -> (4,3)
a1 = a.reshape(8,2)
print(a1.shape)
# (8, 2)
print(a1.T.shape)
# (2, 8)


print(a1)
# [[ 0  1]
#  [ 2  3]
#  [ 4  5]
#  [ 6  7]
#  [ 8  9]
#  [10 11]
#  [12 13]
#  [14 15]]

# Index for [0,1]
print(a1[0])
# [0 1]

print(a1[2][1])
# 5


# Quiz 3
#============
a = [1,2,3,4,5]
b = [8,7,6]
a[3:] = b[::-2]
print(a)
# [1, 2, 3, 6, 8]




#==========================================================

# Q1. Even and odd
'''
a. Write the code using np.arange() to get all even numbers between 21 and 70, (70 inclusive)

b. Write the code using np.arange() to get all odd numbers between 20 and 71. (71 inclusive)

Which options correctly answer questions a and b?

Choose the correct answer from below, please note that this question may have multiple correct answers

1.For question 'a', the answer is np.arange(22,71,2)


2.For question 'a', the answer is np.arange(21,70,2)


3.For question 'b', the answer is np.arange(20, 72, 2)


4.For question 'b', the answer is np.arange(21, 72, 2)
'''
# Ans: a,d

#==============================================================

# Q2. Cast a type
'''
Raghu has created a numpy array arr using the following code:

import numpy as np
arr = np.array([10, 20, 30, 40, 50])
He wants to change the data type from integer to float.Which of the following is the correct approach to do so?

Choose the correct answer from below:

float(arr)

arr.to_float()

arr.astype('float64')

type(arr, dtype='float64')
'''

import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print(arr.astype('float64'))


# Ans : arr.astype('float64')

#===========================================


# Q3. Slice away
'''
What woud be the output of the following code :

import numpy as np
a = np.arange(10)
print(a[2:5])

Choose the correct answer from below:

[2, 4, 6]

[0, 1, 2]

[5, 6, 7]

[2, 3, 4]

'''
# Ans : [2, 3, 4]

#====================================================


# Q4

# Which option is correct about the output of the following code snippet?

import numpy as np
x = np.array([-5, 9 , 20 , 25, -3, 5, 16, 10,-8])
x[(x >= -5) & (x <= 15)] *= -1
print(x) 


'''
Choose the correct answer from below:

1.Given code will change the sign of all the numbers in x.

2.Given code will change the sign of all the numbers in range [-5, 15] in x.

3.Given code will change the sign of all the numbers greater than -5 in x.

4.Given code will change the sign of all the numbers smaller than 15 in x.
'''
# Ans : Given code will change the sign of all the numbers in range [-5, 15] in x.
# [  5  -9  20  25   3  -5  16 -10  -8]

#===================================================

# Q5. Shape of you
'''
Problem statement:

Given an array, return the shape and dimension of the array.
Input Format:

A numpy array
Output Format:

A Tuple (shape, dim)
Sample Input:

[0 1 2 3 4 5]
Sample Output:

((6,), 1)


'''
import numpy as np

def get_array_properties(arr):
    '''
    INPUT: arr -> A nD array
    
    OUTPUT: result -> tuple consisting of shape and dimension
    '''
    
    ## STEP 1. Get the shape of array
    a=np.array(arr)
    shape = a.shape
    
    ## STEP 2. Get the dimension of array
    
    dim = a.ndim
    
    
    return shape,dim
    

#===============================================

# Q6. Index of Pokédex

'''
Problem Statement:

Given a 1D array, return the first and last elements from the array.
Input Format:

A 1D numpy array
Output Format:

A tuple (first_element, last_element)
Sample Input:

[0, 1, 2, 3, 4, 5]
Sample Output:

(0, 5)

'''

import numpy as np

def get_elements(arr):
    '''
    INPUT: arr -> 1D numpy array
    
    OUTPUT elements -> tuple of first and last element.
    '''
    a= np.array(arr)
    first_element = a[0]
    
    last_element = a[-1]
    
    return (first_element, last_element)

#==================================================



# Q7. Create the sequence
'''

Create a sequence of a given length from a given start point, where the difference between 2 consecutive elements of the expected sequence is also given as step.

Input Format:

One line of input will have 3 space-separated integers consisting of start, length of sequence and step between two continuous elements of the sequence.

Output Format:

A numpy array of integers
Sample Input:

5 10 3
Sample Output:

[5 8 11 14 17 20 23 26 29 32]
Sample explanation:

Start of the sequence = 5, length of the sequence = 10 and step = 3.

First point would be the start point only, second point = start + 1*step = 5 + 1*3 =8, ....... 10th point = start + (10-1)*step = 5 + 9*3 = 32


Note: You can use either .arange() or .linspace() to solve this question.

'''

import numpy as np
def seq(start, length, step):
    ''' start, length and step are in form of integers all representing the attributes as their names suggest
        output -> A numpy array is expected to be returned'''

    # YOUR CODE GOES HERE
    
    sequence = np.array(np.arange(start,start+length*step,step))
    
    return sequence



# Q8. The dawn of the planet of numpy
'''
Problem Statement:

Given the start, end, and the stepsize return a numpy array sequence in given range with the specified stepsize.
Input Format:

One line of input will have 3 space-separated integers consisting of start, end of sequence and step.
Output Format:

A numpy array with elements rounded off to 2 decimal places.
Sample Input:

5 7 0.5
Sample Output:

[5 5.5 6 6.5]
Note: To round off the numpy array, use np.round()

P.s: Recall that we can have float step size in numpy array

'''
import numpy as np

def create_seq(start, end, step):
    '''
    INPUT: start, end, step 
    
    OUTPUT: arr -> 1D numpy array
    
    '''
    
    arr = np.arange(start,end,step)
    arr = np.round(arr,2)
    
    return arr


#=============================================


# Q9. Indexed array

'''
Given the following code, what will be the output?

import numpy as np
a = np.array([[34, 28,55], [8, 56, 3], [77, 87, 19]])
print(a.transpose()[-2,-2])

Choose the correct answer from below:

55

28

56

3
'''
# Ans : 56
import numpy as np
a = np.array([[34, 28,55], [8, 56, 3], [77, 87, 19]])
print(a.transpose()[-2,-2])

#=================================================

# Additional Problems
#=======================================

# Q1. Index operation

'''
What would be the output for the following code :

import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[-2])


Choose the correct answer from below:

3

5

4

6

'''

# Ans: 6

#===========================================

# Q2. Comparison Returns!

'''
What will be the output of the following code?


a = np.array([100, 200, 300, 400])

b = np.array([300, 200, 100, 400])

print(a == b)


Choose the correct answer from below:

True

False

[True, False, True, False]

[False, True, False, True]
'''

a = np.array([100, 200, 300, 400])

b = np.array([300, 200, 100, 400])

print(a == b)
# [False  True False  True]

#========================================


# Q3. Numpy Indexing

'''
Given a numpy array,

arr : array([10, 12, 15, 17, 2, 5, 4, 6])

Which of the following is NOT the correct way to access the values at even indices (0,2,4...)?


Choose the correct answer from below:

arr[0,2,4,6]

arr[[0,2,4,6]]

arr[::2]
'''
# Ans : arr[0,2,4,6]

#==============================================



# Q4. Multiple Assignment
'''
What will be the output of the following code?

arr = np.array([1,2,3,4,5,6,7,8])
arr[::2] = range(10,50,10)
print(arr)


Choose the correct answer from below:

[ 1 10 3 20 5 30 7 40]

[ 1 2 3 4 10 20 30 40]

[10 2 20 4 30 6 40 8]
'''
# Ans : [10 2 20 4 30 6 40 8]

#=========================================

# Q5. Distinction

'''
You are given a numpy array containing marks of students in a class. The student gets distinction or first-division on the basis of the below criteria.

marks >= 80 : Distinction

60 <= marks < 80 : First Division

Find the ratio of number of students who got distinction to the number of students who got first division.

Sample Input-

array([20, 35, 68, 82, 83, 70, 90])
Sample Output-

1.5
Sample Explanation-

Distinction marks are 82, 83 and 90. So, 3 distinctions. First division marks are 68, 70. So 2 first divisions. Ratio = 3/2 = 1.5.

'''
import numpy as np
def ratio(marks_arr):
    # Complete the missing code
    marks_arr = np.array(marks_arr)
    distinction = marks_arr[marks_arr >= 80] # Use masking to get the values
    first_div = marks_arr[(marks_arr>=60) & (marks_arr < 80)] # Use masking to get the values
    
    distinction_count = len(distinction)
    first_div_count = len(first_div)
    
    ratio = distinction_count/first_div_count
    
    return round(ratio,2)


#============================================


# Q6. ORDER ORDER ORDER

'''
Problem Statement:

Given a 2D numpy array, return array with its values in the column reversed.
Input Format:

A 2D numpy array
Output Format:

A 2D numpy array
Sample Input:

[[0, 1, 2], 
 [3, 4, 5], 
 [6, 7, 8]]
Sample Output:

[[2, 1, 0], 
 [5, 4, 3], 
 [8, 7, 6]]
P.S : Think about how we reverse list in python.

'''

import numpy as np

def reverse_column(arr):
    '''
    INPUT: arr -> 2D array 
    
    OUTPUT rev_arr -> 2D array
    '''
    arr = np.array(arr)
    rev_arr = arr[:,::-1]
    
    return rev_arr

#====================================================

# Q7. Rotate the array
'''
Given an array in form of a matrix of size (n, n), rotate the matrix clockwise by 90º.

Input Format:

A 2d numpy array
Output Format:

A 2d numpy array
Sample Input:

[[1 2 3] 
 [4 5 6]
 [7 8 9]]
Sample Output:

[[7 4 1]
 [8 5 2]
 [9 6 3]]

Note: Try Transpose / reversing.
'''

import numpy as np
def rotate_img(mat):
    '''mat -> A 2d numpy array
       output -> A 2d numpy array is expected to be returned'''

    # YOUR CODE GOES HERE
    mat = np.array(mat)
    mat = mat.T
    return np.fliplr(mat)
