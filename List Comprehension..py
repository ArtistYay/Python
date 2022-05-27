#List comprehension offers a shorter syntax when you want to create a new list based of an existing list.
#Instead of writing a for loop statement 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#You can use list comprehension you can do all that with one line of code.
fruits2 = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits2 if "a" in x]

print(newlist)

# The syntax for list comprehension is <newlist = [expression for item in iterable if condition == True]> so basically [newlist = x for x in fruits] 

# The condition is like a filter that only accepts the items that valute to True.
fruits3 = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist2 = [x for x in fruits3 if x != "apple"]

print(newlist2)

# The iterable can be any iterable object, like a list, tuple, set

# You can use the range() function to create an iterable
newlist3 = [x for x in range(10)]
print(newlist3)

# Another example. Accept only numbers lower than 5.
newlist4 = [x for x in range(10) if x < 5]
print(newlist4)

# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list
fruits4 = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist5 = [x.upper() for x in fruits4]

print(newlist5)

# You can set the outcome to whatever you like
fruits5 = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist5 = ['hello' for x in fruits5]

print(newlist5)

#The expression can also cantain conditions, not like a filter, but as a way to manipulate the outcome
fruits6 = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist6 = [x if x != "banana" else "orange" for x in fruits6] # Return the item if it is not banana, if it is banana return orange

print(newlist6)