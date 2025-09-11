

# *****************************************************

# Exception Handling and Modules|
# =====================
#     



# Exception Handling and Modules.ipynb
# ------------------------------------------
# https://colab.research.google.com/drive/1f9rMl51SbGfXZypqhnAnesLfX10Gvtq8?usp=sharing

# ***********************************************************


'''
Exception Handling and Modules |Lecture
    -Modules
'''

'''
Modules
========
    - It is a file containing a python code
    - .py extension

Types of Modules
    - Built in Modules
    - user defined modules
    - Third party modules
        numpy, pandas, flask
'''


# sqrt(16)
# It will give error name 'sqrt' is not defined


import math

print(math.sqrt(16))
# 4


# help(math)
# Give all the data about the module


print(isinstance(math,object))
# True

print(math.floor(4.5))
# 4

print(math.ceil(4.5))
# 5


import random
# print(random.randint(0,100))
'''
Random
=======
    - 2 parameters start and end
    - it includes start and end values also
    - loads random modules
    - PRNGS
        - Pseudo
        - Random


Start   --->|-------------|
            |Randomizer   | ---> Unique random value
End     --->|-------------|
                  |
            current Timestamp

If you don't set a seed, Python automatically
seeds the generator with current system time, so each run gives different


To control a behaviour of random 

Use Random.seed(100)
    - PRNG
        - deterministic way
        - Based on starting state, it will always produce
    
    
    - If you use same seed python will start from same position. you will get same sequence of nos.

'''

random.seed(100)
print(random.randint(1,10)) # 3
print(random.randint(1,10)) # 8
print(random.randint(1,10)) # 8
print(random.randint(1,10)) # 3


# import math
# math.sqrt(10)
# Pick only the 

# from math import *
# sqrt(10)
# Other modules may contain same function
# It creates a ambiguity while picking the function. 

import numpy as np


# Create a custom math module with 4 functions -

# add
# sub
# divide
# multiply


import math_test as mt
print(mt.add(1,2))
print(mt.sub(1,2))
print(mt.divide(1,2))
print(mt.multiply(1,2))



'''
Exception Handling
===================
    Error
    =====
        - Something went wrong in program
        - Most errors are actually represented as exception
        - Syntax error: (code structure)
        - Runtime error: (Mistakes while program runs)

    Exception
    =========
        - An exception is a specified object that python creates whenever an error happens at runtime
        - Exception can be caught and handled gracefully


'''

# print(dir(__builtins__))

# ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'PythonFinalizationError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '_IncompleteInputError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']


def divide_by_zero(n):
    return n/0


try:
    divide_by_zero(2)
    print(5+4) # This is not getting executed
except:
    print("Hey why are you divding by Zero! Apply some logic that's it")

# Hey why are you divding by Zero! Apply some logic that's it




# Getting what type exception is occuring
l = [2,0,"Hello",None]

for i in l:
    try:
        print(f"Current Element : {i}")
        result = 5/int(i)
        print(f"Result : {result}")
    except Exception as e:
        print(f"Exception caught is {e}")

    print(" - "*25)

print("Exection Succesfull")

'''
Current Element : 2
Result : 2.5
 -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
Current Element : 0
Exception caught is division by zero
 -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
Current Element : Hello
Exception caught is invalid literal for int() with base 
10: 'Hello'
 -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
Current Element : None
Exception caught is int() argument must be a string, a bytes-like object or a real number, not 'NoneType'       
 -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
Exection Succesfull
'''
        







# Getting what type exception is occuring
l = [2,0,"Hello",None]

for i in l:
    try:
        print(f"Current Element : {i}")
        result = 5/int(i)
        print(f"Result : {result}")
    except ZeroDivisionError as z:
        print(f"You divided by zero. Input Given is {i}")
    except Exception as e:
        print(f"Exception caught is {e}")

    print(" - "*25)

print("Exection Succesfull")


'''
Current Element : 2
Result : 2.5
 -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
Current Element : 0
You divided by zero. Input Given is 0
 -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
Current Element : Hello
Exception caught is invalid literal for int() with base 
10: 'Hello'
 -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
Current Element : None
Exception caught is int() argument must be a string, a bytes-like object or a real number, not 'NoneType'       
 -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
Exection Succesfull
'''





l1 = [2,0,"Hello",None]
for e in l1:
    try:
        result = 5/int(e)
        print("N")
    except Exception as ex:
        print("E")
    except ZeroDivisionError as z:
        print("Z")


# If you give ZeroDivisionError after the Exception both the exception and ZeroDivisionError will run


'''
Finally:
=======
    - Always runs no matter what happens
    - Helps Developers to clean up the task 
        - closing file
        - disconnect connection with Databases
        - Releasing Resources

    try:
    except:
    finally:
    
'''


try:
    x = 10/0
except ZeroDivisionError:
    print("Error in your calculations")
finally:
    print("This will get printed whether you like or not!!")

'''
Error in your calculations
This will get printed whether you like or not!!
'''


try:
    x = 10/2
except ZeroDivisionError:
    print("Error in your calculations")
finally:
    print("This will get printed whether you like or not!!")
#This will get printed whether you like or not!!




try:
    f = open('math_test.py','w')
    f.write("hello")
    x = 10/0
except ZeroDivisionError:
    print("Error : Divisible by zero")

finally:
    print("Closing the file")
    f.close()

'''
Error : Divisible by zero
Closing the file
'''

def process_data(data):
    try:
        try:
            value =int(data)
            print("Converted")
            result = 100/value
            print("Result")
        except ValueError as e:
            print("Value Error")
    except ZeroDivisionError as e:
        print("Outer catch -> Division by zero")
    finally:
        print("Process complete")

process_data("0")
'''
Converted
Outer catch -> Division by zero
Process complete
'''







'''
Raising Custom Exception
=======================

'''

# raise Exception("Insufficient Balance")


# num = 5
# if num%2!=0:
#     raise Exception("Number is odd")



class MyCustomException(Exception):

    def __init__(self, message):
        super().__init__(message)

name = "amit"
try:
    if len(name)<5:
        raise MyCustomException("Length of name should be above 5 characters")
    else:
        print("Name is ",name)
except MyCustomException as e:
    print(e)


# Length of name should be above 5 characters




try:
    assert False, "Error occurred!"
except AssertionError as e:
    print(e)



# In the code snippet below, why is the output "E" for the element 0 and not "Z"?
l1 = [2, 0, "hello", None]

for e in l1:
    try:
        result = 5 / int(e)
        print("N")
    except Exception as ex:
        print("E")
    except ZeroDivisionError as z:
        print("Z")
'''
A
ZeroDivisionError and Exception are distinct without a subclass relationship.
B
The "Z" block is placed after the "E" block.
C
The exception for element 0 is not ZeroDivisionError.
D
The code does not contain a ZeroDivisionError.
'''





#Q3
'''
Which of the given options is equivalent to “random.randint(3, 6)”?

random.choice([3, 6])

random.randrange(3, 6)

3 + random.randrange(3)

3 + random.randrange(4)

Ans : 3 + random.randrange(4)
'''

try:
  print(xadsfs)
except NameError:                       #1
  print("Variable x is not defined")
except:                                 #2
  print("Something else went wrong")


def even(x):
  try:
    if x%2==0:
      return "even"
    else:
      raise Exception
  except:
    return("odd")
  finally:
    return "integer"

print(even(5))    #A
print(even(4)) 