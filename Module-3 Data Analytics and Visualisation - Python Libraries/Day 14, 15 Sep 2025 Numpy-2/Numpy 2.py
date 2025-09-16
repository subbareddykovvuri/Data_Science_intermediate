

# *****************************************************

# Numpy 2 | AGENDA
# =====================
#   - 2D matrices
#   - Indexing in 2D matrices
#   - Slicing in 2D matrices
#   - fancy indexing
#   - Aggregate functions
#   - Any v/s All

# ***********************************************************


# 2D matrices
'''
1.2D Matrices
=============


'''


import numpy as np

a = np.arange(1,17)
print(a)
# [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16]
print(a.ndim)
# 1
print(a.shape)
# (16,)
a=a.reshape(4,4)
print(a)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]]
print(a.ndim)
# 2
print(a.shape)
# (4, 4)
print(a.reshape(2,-1))
# [[ 1  2  3  4  5  6  7  8]     
#  [ 9 10 11 12 13 14 15 16]]

# -1 will be automatically replaced with the factor 

print(a[0])
# [1 2 3 4]
print(a.size)
# 16

a1 = np.arange(12).reshape(3,4)
print(a1.shape)
# (3, 4)

print(a1)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
print(a1.T)
# [[ 0  4  8]
#  [ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]]
print(a1.transpose())
# [[ 0  4  8]
#  [ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]]


# .T is the short form of transpose


# Indexing in 2D arrays
'''
2.Indexing in 2D arrays
==================================
'''


a = np.arange(0,12).reshape(3,4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a[0])
# [0 1 2 3]
print(a[0][3])
# 3
print(a[1])
# [4 5 6 7]
print(a[2])
# [ 8  9 10 11]
print(a[-1][-1])
# 11
print(a[2][3])
# 11
print(a[1][3])
# 7
# alternative way
print(a[1, 3])
# 7


print(a[[1,2]])
# [[ 4  5  6  7]
#  [ 8  9 10 11]]

print(a[[0,1]])
# [[0 1 2 3]
#  [4 5 6 7]]



# Accessing multiple indexes at a time
arr = np.arange(10)
print(arr)
# [0 1 2 3 4 5 6 7 8 9]
print(arr[[1,3,4,5]])
# [1 3 4 5]

print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a[[0,1],[0]])
# [0 4]


# The below code will return : (1, 1), (1, 2), (2, 3)
print(a[[1,1,2],[1,2,3]])
# [ 5  6 11]

# print(a[[1,1,2,4],[1,2,3]])
# IndexError: shape mismatch: 


# Slicing in 2D arrays
'''
3.Slicing in 2D arrays
======================

'''


print(arr)
# [0 1 2 3 4 5 6 7 8 9]

print(arr[:])
# [0 1 2 3 4 5 6 7 8 9]

print(arr[:3])
# [0 1 2]


print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a[:2])
# [[0 1 2 3]
#  [4 5 6 7]]


# Get last two rows?
print(a[1:3])
# [[ 4  5  6  7]
#  [ 8  9 10 11]]

print(a[:-2])
# a[0:-2] 
# [[0 1 2 3]]


print(a[1:3000])
# [[ 4  5  6  7]
#  [ 8  9 10 11]]
# As the 3000 is greater than the 2 it won't raise error and print till the last and stops

print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

a1 = np.arange(0,16).reshape(4,-1)
print(a1)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]


# Fetch the first 2 columns
print(a1[:,:2])
# [[ 0  1]
#  [ 4  5]
#  [ 8  9]
#  [12 13]]

# Fetch the first 2 columns
print(a1[0:4,0:2])
# [[ 0  1]
#  [ 4  5]
#  [ 8  9]
#  [12 13]]


print(a1[1:2,0:1])
# [[4]]

print(a1[1:4,1:3])
# [[ 5  6]
#  [ 9 10]
#  [13 14]]

# Fetching the 1st column and 3rd column
print(a1[:,[1,3]])
# [[ 1  3]
#  [ 5  7]
#  [ 9 11]
#  [13 15]]

# Same using jump
print(a1[:,1::2])
# [[ 1  3]
#  [ 5  7]
#  [ 9 11]
#  [13 15]]

print(a1[ :: , 1::2])
# [[ 1  3]
#  [ 5  7]
#  [ 9 11]
#  [13 15]]

print(a1[ ::2 , 1::2])
# [[ 1  3]
#  [ 9 11]]

print(a1[[0,1,2,3],[0,2,3,2]])
# [ 0  6 11 14]


# Masking of values in an array
#================================
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a<6)
# [[ True  True  True  True]
#  [ True  True False False]
#  [False False False False]]

l = []
for i in a:
    l1 = []
    for j in i:
        if j<6:
            l1.append(True)
        else:
            l1.append(False)
    l.append(l1)
print(l)
# [[True, True, True, True], [True, True, False, False], [False, False, False, False]]


print(a[a<6])
# [0 1 2 3 4 5]




# 5.Aggregate Functions
'''
# 5.Aggregate Functions
========================
'''


print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a.sum())
# 66
print(a.min())
# 0 

print(a.mean())
# 5.5

print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a.sum(axis=0))
# [12 15 18 21]




# Logical Operators any or all
'''
6.Logical Operators
======================
    - any
        - will give true even if one of the value satisfies the condition
    - all
        - will gives true only if all values gets satisfied with the condition
    - where
        -
'''

# Item prices on myntra shopping list
prices = np.array([50,45,25,20,35])

# budget
budget = 30

# Check if there's at least one item that you can affod
can_afford = np.any(prices <= budget)

if can_afford:
    print("Hurrah! I can buy atleast one item :)")
else:
    print("Sorry, better luck next time.")

# Hurrah! I can buy atleast one item :)

print(prices<=budget)
# [False False  True  True False]






# Item prices on myntra shopping list
prices = np.array([50,45,25,20,35])

# budget
budget = 30

# Check if there's at least one item that you can affod
can_afford = np.all(prices <= budget)

if can_afford:
    print("Hurrah! I can buy any product that I want :)")
else:
    print("Sorry, better luck next time.")

# Sorry, better luck next time.



# np.where
# ===========


# product prices:
prices = np.array([45, 55, 60, 75, 40, 90])

# Apply a 10% discount to prices above $50

discounted_prices = np.where(prices>50, prices * .9, prices)

print("Original prices :", prices)
print("Discounted prices : ",discounted_prices)

# Original prices : [45 55 60 75 40 90]
# Discounted prices :  [45.  49.5 54.  67.5 40.  81. ]



# Sorting
'''
Sorting
============

'''

ar = np.array([4,7,3,6,8,1,0,2,5,9])
print(ar)
# [4 7 3 6 8 1 0 2 5 9]

b = np.sort(ar)
print(b)
# [0 1 2 3 4 5 6 7 8 9]





# Vectorization
'''
Vectorization
=============
    - Vectorization is Numpy refers to performing operations on entire arrays or array elements simultaneously, which is significantly faster and more efficient than using explict loops.
'''


a = np.arange(10)

print(a)
# [0 1 2 3 4 5 6 7 8 9]

def random_operation(x):
    if x%2 == 0:
        x += 2
    else:
        x -= 2
    return x


print(random_operation(1))
# -1
operation = np.vectorize(random_operation)
print(type(operation))
# <class 'numpy.vectorize'>

print(operation(a))
# [ 2 -1  4  1  6  3  8  5 10  7]


def square(x):
    return x**2

print(a)
# [0 1 2 3 4 5 6 7 8 9]

sq = np.vectorize(square)
print(sq(a))
# [ 0  1  4  9 16 25 36 49 64 81]



#=====================================================
# Assignment
#======================================================

# Q1. What about code?

'''
import numpy as np
arr = 2 * np.arange(0,2,0.5)
if arr <= 0.6:
    print("condition satisfies")
else:
    print("condition doesn't satisfy")


    
In the above code, 'condition' implies the situation that arr has at least one value smaller than or equal to 0.6. Which option is true with respect to the code and condition?

Choose the correct answer from below:

1.The Code will give the required output.

2.The Code will throw ValueError, and np.any() should be used to get the required output.

3.The Code will throw ValueError and np.all() should be used to get the required output.

4.None of the given option is correct
'''

# Ans: 2

# ============================================================================

# Q2. What will be printed?
'''
Mark the options which are true about the outputs for code snippets a and b.
'''
# Code Snippet a:

import numpy as np
x = np.array([[200,200,200],[300,300,300],[400,400,400]])
v = np.array([200,300,400])
print(v[:,None])
print(x/v[:,None])
print((x / v[:,None])[1][1]) 


# Code Snippet b:
import numpy as np
p = np.array([[0], [10], [20]])
q = np.array([10, 11, 12]) 
print((p + q)[1][1])

'''
Choose the correct answer from below, please note that this question may have multiple correct answers

1.For 'a', the answer is 1.0


2.For 'a', the answer is 2.0


3.For 'b', the answer is 21


4.The code in 'b' will throw ValueError.
'''

# Ans : 1,3

#===========================================================================

# Q3. Batchmate's code
'''
Your batchmate writes the following code :
'''
import numpy as np
a = np.array([[16, 5], [81, 6], [33, 1]])
print(a)
print(np.transpose(a))
# [[16 81 33]
#  [ 5  6  1]]
x=np.transpose(a).reshape(2,3)
print(x)
# [[16 81 33]
#  [ 5  6  1]]
print(x.flatten())
'''
Which of the following is the correct output for the above code?

Note:

flatten() function is used to transform a multi-dimensional array into a one-dimensional array.
In other words, it "flattens" a multi-dimensional array structure into a simple linear sequence.


Choose the correct answer from below:
1.[16 81 33 5 6 1]

2.[16 33 81 5 1 6]

3.[16 5 81 6 33 1]

4.[[16 5 81 6 33 1]]
'''
# Ans : 1


#===========================================================================

# Q4. The Mask



'''
Problem Statement:

Given an array of marks, return the array only containing elements with marks > 40
Input Format:

A 1D numpy array
Output Format:

A 1D numpy array
Sample Input:

[85, 18, 2, 57, 65, 44]
Sample Output:

[85, 57, 65, 44]
'''

import numpy as np

def filter_marks(marks):
    '''
    INPUT: marks -> 1D array
    
    OUTPUT: filtered_marks -> 1D array
    '''
    
    ### Step 1 Get the mask for marks > 40
    
    mask = marks>40
    
    ### STEP 2 use the mask to filter the array
    
    filtered_array = marks[mask]
    
    return filtered_array

#===========================================================================


# Q5. Comparing in numpy

# a. What is the last element of the output?
import numpy as np
print(np.sort(np.array(['Ram','Astha','Raghavendra'])))

# b. What is the output of the code snippet given below?

arr1 = np.array(['Ram','Astha','Brahat'])
arr2 = np.array(['Shyam','Kalyan','Naveen'])
arr1 > arr2

'''
Choose the options which are answers to questions a and b.


Choose the correct answer from below, please note that this question may have multiple correct answers

1.For block 'a', answer is 'Ram'.


2.For block 'a', answer is 'Raghavendra'.


3.For block 'b', answer is array([False, False, False]).


4.For block 'b', answer is False.

'''

# Ans : 1,3


#===========================================================================


# Q6. mapping in numpy

# Given the NumPy array arr, which of the following line of code will return the expected output?

import numpy as np
arr= np.array([[2,3,4,5],[1,7,3,5],[2,8,6,9],[11,23,12,19]])

'''
Expected output:

array ([[4,6,8,10],
 [2,14,6,10],
 [4,16,12,18],
 [22,46,24,38]])
'''

# a.

arr1 = np.array([[2,2,2,2]])
def func(x, y):
    return x * y
vec = np.vectorize(func)
vec(arr,arr1)

# b.

arr1 = np.array([[2],[2],[2],[2]])
def func(x, y):
    return x * y
vec = np.vectorize(func)
vec(arr, arr1)


# c.

arr1 = 2
def func(x, y):
    return x * y
vec = np.vectorize(func)
vec(arr, arr1)


'''
Choose the correct answer from below, please note that this question may have multiple correct answers

1.b


2.c


3.a


4.None of the options are correct
'''
# Ans : 1,2,3


#===========================================================================
# Additional Problems
#===========================================================================


# Q1. One for All

'''
Problem Statement:

Given a numpy array and target value k,

Return True if all elements of array satisfy all below given conditions

Multiple of 2
Greater than k
Input Format:

The input has two lines
First line is the array
Second line is the integer value k
Output Format:

Boolean value i.e. True or False
Sample Input:

[0, 1, 2, 3, 4, 5, 6, 7, 8]
3
Sample Output:

False
Sample Input:

[8, 12, 16, 20]
4
Sample Output:

True
Note: Recall logical functions in numpy
'''

import numpy as np

def check_conditions(arr, k):
    '''
    INPUT: arr, k
    
    OUTPUT: result -> bool
    '''
    
    result = None
    
    ## STEP 1 : Create mask for the given condition
    
    mask = arr%2
    mask = mask==0
    # print(mask)
    ## STEP 2: Use logical function on mask
    
    result = all(arr>k & mask)
    
    
    
    return result




#==========================================================================
# Q2. Extract sub array

'''
Problem Statement:

Given a 2d array, write a program to return a subarray such that the subarray consists of the elements from:

1. the second to the fourth row of the original array,

2. the elements in these rows should be from the last three columns of the corresponding rows of the original array,

3. the rows should be in reversed order.

Sample Input:

[[ 0,  1,  2,  3],  
 [ 4,  5,  6,  7],   
 [ 8,  9, 10, 11],   
 [12, 13, 14, 15],   
 [16, 17, 18, 19]]
Sample Output:

array([[13, 14, 15],  
       [ 9, 10, 11], 
       [ 5,  6,  7]])
Input Format:

A 2D list
Output Format:

A 2D numpy array
Note:

This question can be solved using negative indexing and slicing

'''

import numpy as np


def extract_subarray(arr):
    '''
    INPUT: arr -> 2D array
    
    OUPUT: result -> 2D array
    '''
    
    ### STEP1: Get the rows (2nd  to 4th row)
    
    row_array = arr[1:4]
    
    # print(row_array)
    #### STEP 2: Get the last 3 cols from the row array
    
    cols_array = row_array[:,-3:]
    # print(cols_array)
    #### STEP3: Reverse the rows in cols array
    
    result = cols_array[::-1]
    

    return result


#===========================================================================


# Q3. Transpose Reshaped
# What would the following code print?
import numpy as np
a = np.array([[6, 28], [8, 56], [7, 19]])
x = np.transpose(a).reshape(1,6)
print(x)

'''
Choose the correct answer from below:
[ 6 8 7 28 56 19]

[[ 6 8 7 28 56 19]]

[ 6 28 8 56 7 19]

[[ 6 28 8 56 7 19]]

'''
# Ans : 2

#===========================================================================


# Q4. Reshape me

# What is the below code printing?

import numpy as np
a = np.arange(10,22).reshape((3, 4))
print(a)

'''
Choose the correct answer from below:
1.A 1D numpy array filled with values from 10 to 21

2.A 3X4 matrix filled with values from 10 to 22

3.A 3X4 matrix filled with values from 10 to 21

4.A 1D numpy array filled with values from 10 to 22
'''

# Ans : 3

#===========================================================================

# Q5. Vectorized code

'''
Given 3 arrays,

arr1 = np.array([1,2,3,6,3,2]) 
arr2 = np.array([4,2,1,3,3,2]) 
arr3 = np.zeros(len(arr1)) 
Which of the following are vectorized code(s) for array operations?

A.

for i in range(len(arr1)): 
    arr3[i] = arr1[i] * arr2[i] 
B.

arr3 = arr1*arr2 
C.

for i in range(len(arr1)): 
    if(arr1[i] < 0 ): 
        arr1[i] = -1 
    else: 
        arr1[i] = 1
D.

np.where(arr1 > 0, 1, -1)


Choose the correct answer from below, please note that this question may have multiple correct answers

A


B


C


D

'''
# Ans : 2,4



#==========================================================================

# Q6. Calculate Age

'''
Problem Description:

Given a list of birds and their corresponding age, calculate the mean age of the Crane bird (rounded off to 2 decimal points)
Input Format:

Two 1D array list i.e. bird array and age array
Output Format:

Float value representing mean age of crane birds
Sample Input:

birds = ['spoonbills',  'plovers',  'plovers',  'plovers',  'plovers',  'Cranes',  'plovers',  'plovers',  'Cranes',  'spoonbills']
age = [5.5, 6.0, 3.5, 1.5, 3.0, 4.0, 3.5, 2.0, 5.5, 6.0]
Sample Output:

4.75
Note:

To round off the result, use np.round()
Documentation link: np.round()

'''


import numpy as np

def calculate_mean_age(birds, age):
    '''
    INPUT: birds, age -> 1D array
    
    OUPUT: mean_age -> float variable
    '''
    
    mean_age = None
    
    ## STEP1. Create mask to get Crane birds from birds array
    mask = birds == 'Cranes'
    
    ## STEP2. Get the age of crane birds
    
    crane_ages = age[mask]
    
    ## STEP 3. Calculate mean age of crane birds
    
    mean_age = np.mean(crane_ages)
    
    ## STEP 4. Round off the mean age to 2 decimal points
    
    mean_age = np.round(mean_age,2)
    
    
    
    return mean_age