

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
