
# *****************************************************

# Functional Programming - 1|
# =====================
#     - Intermediate Functional Programming
#     - Higher Order Function
#     - Decorator



# Functional Programming - 1|Lecture.ipynb
# ------------------------------------------
# https://colab.research.google.com/drive/1snOqqrVmZhG-r-8vci-tegPc1EgJVP5k?usp=sharing

# ***********************************************************



'''
Funtional Programming
    is a paradigm where computation is 

    - Anonymous functions
        - 
        - lambda functions are anonymous functions
    - High Order function 
        - function inside a function
    - Immutable Data
        - No changing state of muttable data is allowed
    -Declarative Style
        - Instead of focusing  "how" focus on "what can be acheived"
'''

def square(x):
    return x**2

#lambda function 

square1 = lambda x : x**2

print(square1(3)) # 9


'''
Benifits of lambda
    - Concide and readable
    - More Maintainable
    - Efficient
'''

# Quiz
'''
1.Why can functional programs be more efficient compared to imperative programs?

    A.They always use fewer lines of code.
    B They operate directly on the hardware without needing an OS.
    C. They do not require state updates, which can be a costly operation. 
    D. They utilize a special compiler that speeds up the execution.

Ans : C
'''

# anonymous
print( (lambda x : x **2)(4))



# add two numbers
def add_num(a,b):
    return a+b

add_num(5,6) #11

c = lambda a,b : a+b
print(c(3,4)) # 7

# Even or Odd
even = lambda x: x%2==0

print(even(9)) #False


'''
if condition:
    x
else:
    y


The same in lambda

lambda x : x if x>5 else 0 
       1   2    3        4

1. parameters that to be passed to the function
2. if conditon is true then return some value
3. if condtion
4. if condtion is false then return some value
'''

a = lambda y:y if y>5 else 0
print(a(10)) # 10
print(a(2))  # 0



students = [
    {"name": "A", "marks": 50},
    {"name": "B", "marks": 100},
    {"name": "C", "marks": 40},
    {"name": "D", "marks": 70},
    {"name": "E", "marks": 60},
]

# Sort the dictionary on marks in desc order
print(sorted(students,key= lambda x:x["name"],reverse=True))

print(sorted(students,key= lambda x:x["marks"],reverse=True))

print(sorted(students,key= lambda x:x["marks"]))

# The Sorted will only work for the dicitonary


print((lambda x,y : x**y)(4,5)) # 1024


'''
2.How can you sort a list of dictionaries based on a specific key using a lambda function?

    A. Using the sort() method and specifying the key with the lambda function.
    B. Using the sorted() function and specifying the key with the lambda function.
    C. Using the order() method and specifying the key with the lambda function.
    D. Lambda functions cannot be used for sorting.

Ans : B
'''

# Find maximum of two numbers using lambda
print((lambda x,y : x if x>y else y)(4,5)) # 4


# Reverse a string using lambda
print((lambda x:x[::-1])("Amit")) #timA

#Sorting tuples by second element using lambda

pairs = [(1,3),(2,1),(4,5),(3,2)]
print(sorted(pairs, key = lambda x:x[1]))

# [(2, 1), (3, 2), (1, 3), (4, 5)]



'''
***************************************
Higher Order Function
    - Takes another function as input
    - It can return another function as output

    Advantages
    ----------
    - More reusable
    - More concise
    - More flexible
    - 
'''

def square(x):
    return x**x

def abc(n):
    return 3*n

print(abc(3)) #30


def abc(n):
    def exp(x):
        return x ** n
    return exp

print(abc(3)) 
#<function abc.<locals>.exp at 0x000001D4C28A80E0> 
# It is returning the function

print(type(abc(3)))
#<class 'function'>

#exp(2)
# It will give error


print(abc(3)(2)) # 8




# def student_discount(price):
#     return price * 0.9

# def senior_discount(price):
#     return price * 0.85

# def no_discount(price):
#     return price


def apply_discount(price, discount_func):
    return discount_func(price)

# Discount functions
student = lambda p: p * 0.9
senior  = lambda p: p * 0.85
normal  = lambda p: p

print(apply_discount(1000, student))
print(apply_discount(1000, senior))
print(apply_discount(1000, normal))



'''
3.Consider the following scenario: You want to generate a function that can calculate the square of any number. How can you achieve this using a higher order function?

    A. By setting the inner function to raise the input to the power of 2 and returning the inner function.
    B. By multiplying the input number by 2 in the outer function.
    C. By dividing the input number by 2 in the outer function.
    D. By subtracting 2 from the input number in the inner function.

Ans : A
'''
##########################################################################################

'''
*********************************************
Decorator
    - It is a function that takes another function as input
    - add some extra behaviour and returns a new function


'''

def foo():
    print("hello everyone! How are you doing")

def bar():
    print("Randomly checking here")

foo() #hello everyone! How are you doing
bar() #Randomly checking here


def foo():
    print('-'*50)
    print("hello everyone! How are you doing")
    print('-'*50)


def bar():
    print('-'*50)
    print("Randomly checking here")
    print('-'*50)

foo()
bar()
# Without touching the function we can do th e same using decorators


# Decorator functions

def foo():
    print("hello everyone! How are you doing")

def bar():
    print("Randomly checking here")


def pretty(func):
    def inner():
        print("Decorator")
        print("-"*50)
        func()
        print("-"*50)
    return inner()
new_pretty = pretty(foo)
print(new_pretty)


# inner is 

def pretty(func):
    print("Decorator without inner")
    print("-"*50)
    func()
    print("-"*50)

pretty(foo)


'''
*******************************************
Annotations


'''


@pretty
def foo():
    print("Latest Functions will be executed Times")

# --------------------------------------------------     
# Latest Functions will be executed Times
# --------------------------------------------------  

def satya(symbol):
    def decorator(func):
        def inner():
            print("-"*50)
            func()
            print("-"*50)
        return inner
    return decorator

@satya("*")
def greet():
    print("Hello Amit")

greet()
# --------------------------------------------------     
# Hello Amit
# -------------------------------------------------- 

def satya(symbol):
    def decorator(func):
        def inner(name):
            print("-"*50)
            func(name)
            print("-"*50)
        return inner
    return decorator

@satya("*")
def greet(name):
    print(f"Hello {name}")

greet("Subba")

# --------------------------------------------------     
# Hello Subba
# -------------------------------------------------- 






def log(func):
    def inner(name):
        print("Function is starting..")
        func(name)
        print("Function has ended..")
    return inner

@log
def greet(name):
    print(f"Hello {name}")


greet("Amit")

# Function is starting..
# Hello Amit
# Function has ended..



def requires_login(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("is_logged_in"):
            print("Access Denied! Please login in first.")
            return None
        return func(user, *args, **kwargs)
    return wrapper

@requires_login
def view_profile(user):
    print(f"Welcome {user['name']}, here is your profile.")


user1 = {"name":"Amit","is_logged_in":True}
user2 = {"name":"Rahul","is_logged_in":False}

view_profile(user1)
# Welcome Amit, here is your profile.

view_profile(user2)
# Access Denied! Please login in first.


'''
4.Which of the following best describes the purpose of the @ symbol when used with decorators?

    A. To indicate a loop in Python.
    B. To mark the start of a comment in Python.
    C. To specify which decorator should be applied to a function.
    D. To declare a new variable.

Ans : C
'''



odd=lambda x: bool(x%2)
result=[n for n in range(10)]

for i in result:
    if odd(i):
        continue       
    else:
        print(i, end=" ")


#Which option represents the statement that is responsible for generating [2, [2, 3, 2, 3], 8, 10] as the output in the following code?
print()
a=[1,[2,3],4,5]
result = lambda x: list(map(lambda y:2*y, x)) if isinstance(x,list) else lambda x:3*x   
print(result(a))