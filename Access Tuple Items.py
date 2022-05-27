#You can access a certain item in the tuple by referring to the index number
thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) 

#Negative indexing means start from the end.
thistuple2 = ("apple", "banana", "cherry")
print(thistuple2[-1])

#You can specify a range of indexes by specifying where to start and where to end the range.
thistuple3 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple3[2:5])

#This will stop at orange
thistuple4 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple4[:4])

#This will start at cherry
thistuple5 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple5[2:])

#Remember negative index always start from the end. Sp if you specify -4:-1 it will start from melon and end at orange.
thistuple6 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple6[-4:-1])

#To check if an item exist in a tuple use the in keyword
thistuple7 = ("apple", "banana", "cherry")
if "apple" in thistuple7:
    print("Yes!")


