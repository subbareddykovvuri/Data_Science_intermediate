

# *****************************************************

# Functional Programming - 2|
# =====================
#     - Intermediate Functional Programming
#     - Higher Order Function
#     - Decorator



# Functional Programming - |Lecture.ipynb
# ------------------------------------------
# https://colab.research.google.com/drive/1nGY8gbJLAuB4UVlsiSv6fX_MzOHi04DO?usp=sharing

# ***********************************************************


'''
Functional Programming - 2|Lecture
    - Principles of Functional Programming
    - Maps
    - Filter
    - Zip
    - Reduce
    - Args and Kwargs

'''

# Principles of Functional Programming
'''
Principles of Functional Programming
    - Data should be Sepated from mutations
    - Treat variables as immutable (unchangable)
    - Treat fucnitons as FCC 
        - HOF
        - Ano f(x)
'''

x = 5
x = 3 * x
x += 1

print(x)
# 16


# option 1 create a new object every time
x = 5
x1 = 3*x
x2 = x1 + 1
print(x)
# 5

# The above example will create a object each time and readibility will be decreased

x = 5
def mutation(x):
    x = 3*x
    x += 1
    return x

print(mutation(x))
# 16


'''
1. map() 
    - It applies a function to every item is a iterable(list, tuple, etc) and returns a map object (which can be converted to a List/Tuple)

Map Transformation
------------------
    - Takes one element and produces one element

Syntax
------
    map (a,b)
        - a : function to perform 
            (what to perform)
        - b : Iterables (List, Set, Tuples...)
            (on which to perform)
'''


a = [1,2,3,4,5]
# Need to perform so operation and need output as below
# [1,4,9,16,25]

res = [i**2 for i in a]
print(res)
# [1,4,9,16,25]

res_1 = map(lambda x: x**2,a)

print(res_1)
# <map object at 0x0000020C1076B130>

print(list(res_1))
# [1, 4, 9, 16, 25]


# Convert strings to uppercase
names = ["amit", "aryan", "rahul"]

res = list(map(lambda x : x.upper(),names))
print(res)
# ['AMIT', 'ARYAN', 'RAHUL']

#Add two lists element-wise
a = [1,2,3]
b = [10,20,30]

res = list(map(lambda x,y : x+y,a,b))
print(res)
# [11, 22, 33]



#Task 2: Convert given height to t-shirt size
#h < 150 -> S
#h >= 150 and h < 180 -> M
#h >= 180 -> L

heights = [144, 167, 189, 170, 190, 150, 165, 178, 200, 130]


def height_chart(height):
  if height < 150:
    return "S"
  elif height >= 150 and height < 180:
    return "M"
  else:
    return "L"
  

sizes = list(map(height_chart,heights))
print(sizes)
# ['S', 'M', 'L', 'M', 'L', 'M', 'M', 'M', 'L', 'S']


sizes_1 = list(map(lambda x:"S" if x < 150 else "M" if x >=150 and x < 180 else "L",heights))
sizes_1

# ['S', 'M', 'L', 'M', 'L', 'M', 'M', 'M', 'L', 'S']



#Task 3: Given two lists A and B having 1s and 0s,
# find another list with element at index i as True if A[i] == B[i] else False

A = [1,0,0,1,1,1,0,0,0,1,0,1]
B = [0,0,1,1,0,1,1,1,0,0,0,0]

# C = [True, True, False.........] True = if both A,B have same element else false

C = list(map(lambda x,y:x==y,A,B))
print(C)
# [False, True, False, True, False, True, False, False, True, False, True, False]


# Process multiple lists

marks = [80, 90, 70]
weights = [0.5, 0.3, 0.2]

# [40.0, 27.0, 14.0] --> # 81.0

res = list(map(lambda x,y:x*y,marks,weights))
print(sum(res)) # 81.0





'''
2.Filter




'''

a = list(range(1,11))
print(a)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filter_output = filter(lambda x:x%2==0,a)
print(list(filter_output))
# [2, 4, 6, 8, 10]

words = ["python", "java", "c"]

filter_output = list(filter(lambda x:len(x)>3,words))

print(filter_output)



# Filter students who passes (score>=50)
students = [("Amit",85),("Aryan",40),("Rahul",72),("Neha",30)]

filter_output = list(filter(lambda x:x[1]>=50,students))
print(filter_output)
# [('Amit', 85), ('Rahul', 72)]


filter_output = list(map(lambda x:x[0],list(filter(lambda x:x[1]>=50,students))))
print(filter_output)
# ['Amit', 'Rahul']

# Filter prime numbers from 1 to 50
a = range(1,50)
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

primes = list(filter(lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)), a))
print(primes)
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

def prime_numbers(n):
  if n<2:
    return False
  res = list(map(lambda x : n%x!=0, range(2,int(n**0.5)+1)))
  return all(res)

ans = list(filter(prime_numbers,range(1,50)))


numbers = list(range(1,51))
primes = list(filter(
  lambda n:n>1 and len([i for i in range(2,int(n**0.5)+1) if n%i == 0]) == 0,
  numbers
))


numbers = list(range(1, 11))

result = list(
    map(lambda x: x**2, filter(lambda n: n % 2 == 0, numbers))
)

print(result)


'''
3.Zip:
    - It combines 2 or more iterables element wise paires
    - zip(iter1, iter2....)

    name = ["A","B","C"]
    marks = [85,90,80]
    zip(name,marks)
    [(A,85),(B,90),(C80)]

    - Zip stops at shortest iterable

    n = [A,B,C]
    m = [80,90]
    output = [(A,80),(B,90)]

'''

a = [1,2,3]
b = ["a", "b", "c", "d", "e"]

result = list(zip(a,b))

print(result)
# [(1, 'a'), (2, 'b'), (3, 'c')]



a = [1,2,3]
b = ["a", "b", "c", "d", "e"]
c = ["x", "y", "z", "m", "n"]

result = list(zip(c, b,a))
print(result)
# [('x', 'a', 1), ('y', 'b', 2), ('z', 'c', 3)]



'''
4.Reduce:
    - It is afunciton that combines/reduces the terms in sequence.
    
    - From functools import reduce

'''


from functools import reduce

numbers = [1,2,3,4,5]
result = reduce(lambda x,y : x+y,numbers)
print(result)
# 15

n = [ 7,11,9,3,6,4,2]
result = reduce(lambda x,y : x if x>y else y,n)
print(result)
# 11


#multiply all numbers
numbers = [1,2,3,4,5]
result = reduce(lambda x,y : x*y,numbers)
print(result)
# 120



'''
Given the lists a = [1, 2, 3] and b = ["a", "b"], what will be the result of list(zip(a,b))?

'''






def sum_number(x,y):
  return x+y

res = sum_number(6,7)
print(res)

# print(sum_numbers(5,6,7,8)) -> It will raise error          

'''
5. Args and Kwargs
    - *args (positional argument)
        - Allows a function to accept a variable no of positional arguments
        
    - **kwargs (keyword argument)
        - allows a function to accept a variable no of keyword arguments

    Order of passing arguments
        - Positional -> Arguments -> Keyword
'''
# *args
def sum_number(x,y,*args):
  result = x+y
  if args:
    result += sum(args)
  return x+y

res = sum_number(6,7,8,9,10)
print(res)



# **kwargs

def create_person(name, age, gender, **extra_info):
  Person = {
    "name" : name,
    "age" : age,
    "gender" : gender
  }
  if extra_info:
    Person.update(extra_info)
  
  return Person

p2 = create_person(name = "Rohit",age=1500,gender ="Male", color="blue",hobby="chess")

print(p2)



def random(x,y,*args, **kwargs):
  print(x)
  print(args)
  print(kwargs)

# random(1,2,4,5,6,m=1,n=2,o=3,8,9,0)

print(random(2,1,2,3,z=1))
# 2,(2, 3),{'z': 1}

'''
def sample_func(x, y, *args, **kwargs):
    return x, y, args, kwargs
What will be the output for the function call sample_func(1, 2, 3, 4, a=5, b=6)?

1,2,(3,4),{'a':5,'b':6}

'''










# Q1
# What will be the output of the following code snippet:

import functools
lists = [1,2,3,4]
print(functools.reduce(lambda x,y : x if x > y else y ,lists))
'''
Error

10

4

No Output
'''
# 4






# Q2
sentence = "abc cde def"
result = list(map(lambda x: list(x), sentence.split(" ")))
print(result)


'''
['abc'] ['cde'] ['def']

['a', 'b', 'c'] ['c', 'd', 'e'] ['d', 'e', 'f']

['abc', 'cde', 'def']

[['a', 'b', 'c'], ['c', 'd', 'e'], ['d', 'e', 'f']]
'''




# Q3
string = '''
We spent several years building our own database engine, Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible service with the same or better durability and availability as
the commercial engines, but at one-tenth of the cost. We were not surprised when this worked.
'''
result = lambda key, val: key[ key.find(val) -18 : key.find(val) +18 ] if val in key else -1

print(result(string, 'SQL'))

'''
We were not surprised when this worked

compatible service with the same or better durability

a fully-managed MySQL and PostgreSQL

None of the above
'''
# a fully-managed MySQL and 





# Q4

array = [ [1, [ [ 2 ] ], [ [ [ 3 ] ] ], [ [ 4 ], 5 ] ]]
result = lambda x: sum(map(result, x), [ ] ) if isinstance(x, list) else [x]
print(result(array))

'''
[1, [ 2 ], [ [ 3 ] ], [ 4 ], 5 ]

1 , 2, 3, 4, 5

15

[1, 2, 3, 4, 5]
'''

# [1, 2, 3, 4, 5]


# Which given option is equivalent to the following code:

array  = [1, 2, 3, 4, 5]
def func1(x):
    return x<0
result=filter(func1, array)
print(list(result))


'''
list(filter(lambda x:x<0, array))

list(filter(lambda x, y: x<0,array))

list(filter(reduce x<0, array))

list(reduce(x: x<0, array))
'''

# list(filter(lambda x:x<0, array))




# Q6
#You are given an incomplete code in which you have to print all the numbers from the list that are less than 6 using filter function. Complete the given code.

l=[1, 10, -3, 4, 15]

def f1(x):
 return x<6

m1 = None
# PUT YOUR CODE HERE

# print(list(m1))

'''
m1 = filter(f1, l)

m1 = filter(l, f1)

m1 = filter(f1, l, 6)

m1 = filter(f1, 6, l)
'''
# m1 = filter(f1, l)



# Additional

# Q1
# What will be the output of the following code snippet:

from functools import reduce
array = {1, 2, 3}
result = lambda array: reduce(lambda P, x: P + [subset | {x} for subset in P], array , [set()]) 

print(result(array)) 

'''
[set(), {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}]

[{1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}]

[{1, 2, 3}]

None of these
'''
# [set(), {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}]



# Q2
# Given a list containing email ids, help Sam in retrieving all the emails which have "SAM" or "sam" in their names.

ids = ["SAM@gmail.com", "Ram@gmail.com", "sam@gmail.com", "samJohnson@iit.com", "SAM@harvard.com"]
name = "sam"
# result = list(filter(lambda x : ??? , ids))
# print(result)

# Complete the code snippet given above to return all the email ids in the list that have either the uppercase or lowercase name as a substring. Choose the correct option which can be used to fill the blank (???) to get the required output.


'''
name in x.lower()

(name.lower() or name.upper()) in x

name.lower() in x and name.upper() in x

(name.lower() and name.upper()) in x
'''

# name in x.lower()



