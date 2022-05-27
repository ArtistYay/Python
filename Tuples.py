#Tuples is a collection which is ordered and unchangeable. Allows duplicate members. It's used to store multiple items in a single variable. They are written with round brackets.
thistuple = ("apple", "banana", "cherry")
print(thistuple)

 #Tuples allow duplicate values
thistuple2 = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple2)

 #To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple3 = ("apple",)
print(type(thistuple3))

 #You can also use the tuple() constructor to make a tuple.
thistuple4 =tuple(("apple", "banana", "cherry"))

 