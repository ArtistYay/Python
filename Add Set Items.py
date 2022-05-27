#You can not change a set but you can add items to a set with the add() method
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#To add items from another set into the current set, use the update() method.
thisset2 = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset2.update(tropical)

print(thisset2)

#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.)
thisset3 = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset3.update(mylist)

print(thisset3)