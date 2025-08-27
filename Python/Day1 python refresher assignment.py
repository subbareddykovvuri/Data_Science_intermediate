score = 2
if False:
    score = 66

def batting():
    if True:
        score = 40

batting()
print(score)


arr = [a+" "+b for a in [ 'Hello', 'Good'] for b in ['Dear', 'Bye']]
print(arr)


def lcm(arr):
    
    # arr-> The list of integer numbers
    # Output-> The LCM of the list of Integer numbers is to be returned
    result=1 
    # YOUR CODE GOES HERE

    def gcd(a,b):
        if a == 0:
            return b
        if b == 0:
            return a
        
        if a == b:
            return a
        
        if a>b:
            return gcd(a%b,b)
        return gcd(a,b%a)
    
    def get_lcm(a,b):
        return (a*b)//gcd(a,b)
    
    for i in arr:
        result = get_lcm(result,i)
    return result

arr = [13,6,17,18,19,20,37]
print(lcm(arr))


arr = [[1,2,3],[10,11,12],[4,5,6],[13,14,15],[10,1,2]]

print(max (arr, key=sum ) )




#Question 5
var=1
def ML():
     print("Inside ML:", var, end=" ")

def AI():
     var=2
     print("Inside AI:", var, end=" ")

def DL():
     global var
     var =3
     print("Inside DL:",  var, end=" ")
ML()
print(var, end=" ")

AI()
print(var, end=" ")

DL()
print(var, end=" ")

#Question 7
list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
list2 = list1
list3 = list1[:]
print("\n")
list2[0] = 'Guava'
list3[1] = 'Kiwi'
print(list1,list2,list3)

#question 9
l = ['a','b','c']

def Reverse1(lst):
    return [ele for ele in reversed(lst)]
print(l)
print(Reverse1(l))

def Reverse2(lst):
    lst.reverse()
    return lst
print(l)
print(Reverse2(l))

def Reverse3(lst):
    return lst[::-1]
print(l)
print(Reverse3(l))
