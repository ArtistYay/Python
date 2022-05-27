from re import L
from tkinter import N, Y


a = (input("What's your first number?"))
b = (input("What's your second number?"))
if b > a: 
    print(b + " is greater than " + a)
elif b < a: #If the previous conditions were not true, then try this condition.
    print(b + " is less than " + a)
else:
    print(b + " is equal to " + a)

#You can also use the short hand if it make the code cleaner

x =  (input("How much money do you have? "))
if x > 100: print("Congrats! you have more money then me.") 

#You can use if and else on the same line for one statement
y =  (input("How much money do you have? "))
print("Do you need a dollar?") if y < 100 else print("Lemme hold a dollar.")

#You can also have 3 conditions in one statement.
p = (input(""))

#This is also known as Ternary Operators or Conditional expressions.

#The 'and' keyword is a logical operator, and is used to combine conditional statements.
N = 800
L = 6000
S = 12

if N > S and L < N:
    print("Both statement are True")
else:
    print("Both statements are False")

#You can also use 'or' keyword to combine conditional statements

#You can have an 'if' statement inside another 'if' statement which is called nested if
k = 41

if k > 10:
    print("above ten")
if k > 20:
    print("also above 20!")
else:
    print("but not above 20.")

#'if' statements cannont be empty. If it is use the 'pass' statement
w = 33
o = 200

if w > o:
    pass