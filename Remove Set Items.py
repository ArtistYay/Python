#To remove an item in a set, use the remove(), or the discard() method.
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

thisset1= {"apple", "banana", "cherry"}

thisset1.discard("banana")

print(thisset1)

#You can also use the pop() method to remove an item, but this method will remove the last item.
thisset2 = {"apple", "banana", "cherry"}

x = thisset2.pop()

print(x)

print(thisset2)

#The clear() method empties the set
thisset3 = {"apple", "banana", "cherry"}

thisset3.clear()

print(thisset3)

#The del keyword will delete the set completely
thisset4 = {"apple", "banana", "cherry"}

del thisset4

print(thisset4)