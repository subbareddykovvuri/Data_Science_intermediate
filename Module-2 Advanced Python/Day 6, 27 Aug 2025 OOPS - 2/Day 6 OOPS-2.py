
# ***********************************************

# OOPS -2 | Lecture
# =======

#  - Using Dunder/Magic methods
#  - Inheritence
#  - Private Properties
#  - Multiple Inheritence
#    -> Method Resolution Order

# OOPS 2 - Dunders,Inheritence.ipynb:
# ----------------------------------
# https://colab.research.google.com/drive/1JNVq3LUcH__TviPT42-G0-73W7d96tCM?usp=sharing
# ***********************************************


# Using Dunder/Magic methods
# =========================

#  - Double Underscore
#  - These are called magic methods

 
# https://www.geeksforgeeks.org/python/dunder-magic-methods-python/


class Car:
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

c1 = Car("Nexon",15)
c2 = Car("Scorpio",13)

print(c1)
#<__main__.Car object at 0x00000157B07E27B0>



# By using __str__ we can override the default print

class Car:
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def __str__(self):
        return f"{self.name} name with mileage as {self.mileage}"
    

c1 = Car("Nexon",15)
c2 = Car("Scorpio",13)

print(c1)
#Nexon name with mileage as 15



'''
# Inheritence
'''
#         SchoolMember
#             |
#     ----------------------
#     |                     |
# Student                 Staff
#                             |
#                         Teacher


class SchoolMember:
    def __init__(self, name):
        self.name = name

class Student(SchoolMember):
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

class Staff(SchoolMember):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Teacher(Staff):
    def __init__(self, name, salary, subject):
        self.subject = subject


s1 = Student("Nishtha","A")
print(type(s1))
#<class '__main__.Student'>
print(s1.name)
# Nishtha



#Example-2
class SchoolMember:
    def __init__(self, name):
        self.name = name

class Student(SchoolMember):
    def __init__(self, name, grade):
        # self.name = name
        self.grade = grade

class Staff(SchoolMember):
    def __init__(self, name, salary):
        # self.name = name
        self.salary = salary

class Teacher(Staff):
    def __init__(self, name, salary, subject):
        self.subject = subject


s1 = Student("Nishtha","A")
# print(s1.name) # Error

# To get the name we need call the super in Student class then it calls the parent 


#Example-3
class SchoolMember:
    def __init__(self, name):
        self.name = name

class Student(SchoolMember):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

class Staff(SchoolMember):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

class Teacher(Staff):
    def __init__(self, name, salary, subject):
        super().__init__(name,salary)
        self.subject = subject


s1 = Student("Nishtha","A")
print(s1.name) # Nishtha
s1.name = "Random"
print(s1.name) # Random

t1 = Teacher("Amit", 1000, "Sql And Python")
print(t1.name,t1.salary,t1.subject)
# Amit 1000 Sql And Python


'''
************************************************
#  - Private Properties
************************************************
'''

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def withdrawl(self, amount):
        self.balance -= amount
    def deposit(self, amount):
        self.balance += amount

b1 = BankAccount(10000)
b1.deposit(2000)
b1.withdrawl(5000)
print(b1.balance) #7000

b1.balance = 12456215673127817837189372189
print(b1.balance) # 12456215673127817837189372189

b1.withdrawl(77867868687678)
print(b1.balance) # 12456215673127739969320684511


'''
In Above Example we can access the balance directly but if we want to restrict it by using below method

1.Private (__)
    - 2 underscores
    - Nothing can be completely Private in Python
    - __ make your variable as Private
    - Python internally creates it with name of _classname__private
    - Hence we can still access with above name

2.Protected (_)
    - 1 Underscore

3.Public (default)

 - In python we don't have any 
 - In python by default all will be in public

==========================================================================================
Feature     1.Acess within same class   2.Access is derived class   3.Access outside class
-------------------------------------------------------------------------------------------
Private         yes                     No                          No
-------------------------------------------------------------------------------------------
Protected       yes                     yes                         No
==========================================================================================


'''



# Default Python behaviour
class Demo:
    def __init__(self):
        self.name = "Public"

obj = Demo()
print(obj.name) #public


# protected Pytohn behaviour
class Demo:
    def __init__(self):
        self._name = "Protected"

obj = Demo()
print(obj._name) #Protected

# Private Pytohn behaviour
class Demo:
    def __init__(self):
        self.__name = "Private"

obj = Demo()
# print(obj.__name) #We cannot access as it is private

# There is a loop hole in private 
print(obj._Demo__name) #Private



'''
To get hidden 
'''
print(dir(obj))
# ['_Demo__name', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__']



class Base:
    def __init__(self):
        self.__data = "Base data"

class Child(Base):
    def __init__(self):
        super().__init__()
        self.__data = "Child data"

obj = Child()
print(obj.__dict__)
# {'_Base__data': 'Base data', '_Child__data': 'Child data'} 



'''
*************************************************
Multiple Inheritence
*************************************************

    A
    |
-------------
|           |
B           C
|           |
-------------
    |
    D

Here B is the child of A, C is the child to A, but For D does this the child of B or C ?


Method Resolution order
    - C3 linearization (It will tell from which parent need to inherit)
    - left to right
    - we go to a Parent when all its children are considered


    A(5)
    |
-------------
|           |
B(3)        |
|           D(4)
C(2)        |
|           |
-------------
    |
    E(1)
'''

#Example 1
class A:
    x = 10

class B(A):
    pass

class C(B):
    pass

class D(A):
    x = 5

class E(C,D):
    pass

e1 = E()
print(e1.x) #5


#Example 2
class A:
    x = 10

class B(A):
    pass

class C(B):
    x = 6

class D(A):
    x = 5

class E(C,D):
    pass

e1 = E()
print(e1.x) #6

print(E.__mro__)
# (<class '__main__.E'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.D'>, <class '__main__.A'>, <class 'object'>)


#Example 3
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B,C):
    pass

d = D()
d.show() # B
print(D.__mro__) 
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)



#Example 3
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B,C):
    def show(self):
        print("D")

d = D()
d.show() # D
print(D.__mro__) 
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)



'''
************************************************
Quiz
************************************************
'''

# Quiz 1
class A:
    print("Am I a class?")

A()

obj1 = A()

if A():
    print(A()) 

# How many objects will be created ?
# Ans : 4


# Quiz 2



# Quiz 3
class A:
    def __init__(self, name):
        self.name = name
    
a1 = A("Bunty")
a2 = A("Babli")

print(id(a1) == id(a2)) 

# False


# Quiz 4
class Counter:
    def __init__(self):
        self.count=5
        '''self.count=count+1''' # Commented to bypass error

c = Counter()
print(c.count)

# What would be the output of the following?
# Ans : Error


# Quiz 5
# What are the functions inside a class called in python?
# Ans : Methods


# Quiz 6
class Random:
    def __init__(self, a = "Is it possible?"):
        self.a = a

    def display(self):
        print(self.a)

r = Random()
r.display()
# Is it possible?


# Quiz 7
class A:
    def __init__(self):
        self.variable = 'Old'
        self.update(self.variable)
        
    def update(self, var):
        var = 'New'
        
a = A()
print(a.variable)
# Old



#Quiz 8
# Which of the following code pieces would create an empty class in python?
# Ans : Class A : Pass


# Quiz 9
class A:
    def do_something(self):
        print("I do something!")

class B(A):
    def do_something(self):
        super().do_something()
        print("I also do something!")

b = B()
b.do_something()
# What would be the output of the following?
# Ans : I do something! I also do something!



class Parent:
  def __init__(self):
    pass
  def print(self):
    print("60")

class Child(Parent):
    def __init__(self):
        super().__init__()
    def type(self):
        super().print()

C=Child()
C.type()



# Quiz 1

class A:
    def __init__(self):
        print("IN A before calling multiply")
        self.multiply(15)
        print("IN A after calling multiply")
        print(self.i)
        print("IN A after print self.i")

    def multiply(self, i):
        print("IN A before  multiply")
        self.i = 4 * i
        print("IN A after multiply")

class B(A):
    def __init__(self):
        print("IN B before init")
        super().__init__()
        print("IN B after init")

    def multiply(self, i):
        print("IN B before  multiply")
        self.i = 2 * i;
        print("IN B after multiply")

obj = B()
print(B.__mro__)




#
class Employee:

    def __init__(self, name, val):

        self._name=name

        self._salary=val

e1=Employee("Rahul",200)

print(e1._salary)



#
class Demo:
    def __new__(self):
        self.__init__(self)
        print("Demo's __new__() invoked")

    def __init__(self):
        print("Demo's __init__() invoked")

class Derived_Demo(Demo):
    def __new__(self):
        print("Derived_Demo's __new__() invoked")
    
    def __init__(self):
        print("Derived_Demo's __init__() invoked")

def main():
    obj1 = Derived_Demo()
    obj2 = Demo()

main()



#
class A:
 def __init__(self, name, sound="Grrrr"):
   self.name = name
   self.sound = sound

 def make_noise(self):
   print("{} says, {}".format(self.name,self.sound))

class B(A):
 def __init__(self, name="Rachel"):
   super().__init__(name, "Meow!")

 def make_noise(self,sound="Grrrr!"):
   print("{} says, {}".format(self.name, sound))

pet_cat = B()
pet_cat.make_noise()