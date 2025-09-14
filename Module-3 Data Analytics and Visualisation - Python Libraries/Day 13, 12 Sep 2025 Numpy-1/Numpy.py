

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
