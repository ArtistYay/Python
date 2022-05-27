#You can not add, change, or remove items in a tuple once it's created but you can change it into a list, change the list, and change it back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#You can use append to add an item to a tuple. To remove an item change append to remove
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#Or you can make a variable and add the variable to the tuple
thistuple2 = ("apple", "banana", "cherry")
y = "orange"
thistuple2 += y
print(thistuple2)

#To delete a tuple use the del keyword