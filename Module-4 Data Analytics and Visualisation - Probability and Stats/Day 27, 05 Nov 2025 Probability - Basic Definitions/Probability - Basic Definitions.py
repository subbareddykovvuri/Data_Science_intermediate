

# *****************************************************

# Probability - Basic Definitions | AGENDA
# =======================================
#   - Intro
#   - Experiment
#   - Probability of event

# ***********************************************************


# 1.Intro
'''
1.Intro
===============
    - Donot Focus or try to memorize formulas
    - This session is used to Building Intuition
    - 20% to 30% questions in interview will be from this module
'''


# 2 Experiment
'''
2.Experiment
===========
An activity with some data

2 types
    1.Deterministic
        The outcome stays constant no matter how amny times exp is repeated.

        Ex : a^2+b^2+2ab
            if a=3 and b=4 then ans =49
        Here the outcome won't change if we execute the same tomorrow
    
    2. Probabilistic Exp
        The outcome is 
        1.Rolling a die
            In trail-1 we got 6 and trail-2 we will get same or different

        Terminologies:
            1.Outcome : Result
                {1} , {2}, {3}, {4}, {5}, {6},

            2.Sample Space:
                Collection of all possible outcomes
                {1 2 3 4 5 6} 

            3.Event:
                - Any subset of sample space
                Ex : Getting Even Numbers as outcome
                {2,4,6}
                
                * Since empty set {} is a subset of every set, It is considered as a valid event
                    p({}) = 0 probability of get a empty set is zero

                Sample space for die
                set = {1 2 3 4 5 6}
                
                consider event {3 4 5 6} getting value getter than 2 which is the subset of the set
                
                Consider event {2 4 6} getting even value  which is the subset of the set

                If n outcomes -> 2^n events


Example of Tossing a coin
=========================
1.Head
2.Tail

Total outcomes = 2 (Head, Tail)
Total events = 2^2 = 4 ({}, {H}, {T}, {H,T})

what is the probability that you will get either Head or Tail is 100%

Event of getting 1 for dice roll. Is this valid event? Yes
Event of getting 1 in coin toss. Is this valid event? No



Key Takeaway : An event must always be subset of sample spaces
i.e Outcomes in event should be present in sample space

'''

# 3.Probability of event
# ========================

'''
Probability of event = Favourable Outcomes/ Total Outcomes


Coin
====
P(Head) = 1/2   {H}
P(Tail) = 1/2   {T}
P(Head, Tail) = 2/2 = 1 {H,T}
p() = 0/2 = 0   {}

Die
====
P(Even Number) = 3/6 = 50%

'''


# Quiz 1
'''
We are tossing a dice, where the sample space is {1, 2, 3, 4, 5, 6}. Which of following is not an event?

A {1}
B {1,3}
C {1, 3, 5}
D {1, 3, 5, 7}
'''
# Ans : D


# Quiz 2
'''
Q. We are tossing a coin followed by a dice.
How many possible outcomes will be there in the sample space?
Waiting for others to complete the quiz
A.10
B.8
C.12
D.16
'''
# Ans : C

# Explanation for quiz-2
'''
Tossing a coin and rolling a die

H-1, H-2, H-3, H-4, H-5, H-6  
T-1, T-2, T-3, T-4, T-5, T-6

Total outcomes are : 12
'''


'''
Shasank

Q: Event when mohit will lose the bet
    E_M (2 4 6)
    E_M'(1 3 5)
' Indicates the inverse 
'''


# Mutually Exclusive Events Disjoint Events
'''
A Intersect B = {}
we can say that A and B are mutually exclusive
M, S = Yes
A, S = No
'''

# Exhaustive Event
'''
If Union of two or more events is equal to sample space

Mohit, Shashank are exhaustivr
M, S, A are exhaustivr
S, A = No
M, A = No
'''

# Independent Events
'''
Exp1 - e1
Exp2 - e2

Outcome of exp2 -> e2 does not depend on e1
Then e1 and e2 are independent

A Box contains 2 color of balls (Red, Blue)
Picking of one color ball  doesn't effect another color ball

independent
===========
Pick a ball
check its outcome
put it back

Pick another ball


dependent
===========
Pick a ball
check its outcome

Pick another ball

If we doesn't put back the ball then the probability will we changed

'''

# Quiz 4
'''
There are 4 green balls, 6 yellow balls, and 2 blue balls in a bag.
A random ball is chosen.
Find the probability that a yellow or blue ball is chosen.

A.4/12
B.6/12
C.8/12
D.10/12
'''
# Ans : C


# Quiz 5
'''
Which of the following represent mutually exclusive sets?

A.Youtube premium Vs Non-premium users
B.People who like cappacinno vs Espresso
C.Users of Swiggy vs Zomato
D.Users of Amazon vs Flipkart
'''
# Ans : A

# Quiz 6
'''
 It is known that 60% people use Swiggy, 50% use Zomato. 20% people use both.
What percentage use Swiggy, but do not use Zomato?

A.60
B.50
C.40
D.20
'''
# Ans : C