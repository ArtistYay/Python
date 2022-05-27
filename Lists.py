#List is a collection which is ordered and changeable. Allows duplicate members.
#Lists are used to store multiple items in a single variable. There created using square brackets.
thislist = ['apple', 'banana', 'cherry']
print(thislist)

#lists have a defined order and is changeable. It can also allow duplicates.

#To determine how many items a list has, use the len() function.
thislist2 = ['apple', 'banana', 'cherry']
print(len(thislist2))

#List items can be of any data types (string, int, boolean)

#List can contain different data types.
list1 = ['abc', 34, True, 40, 'male']

#From Python's perspective, list are defined as objects with the data type 'list'
mylist = ['apple', 'banana', 'cherry']
print(type(mylist)) #will print <class 'list'> instead of string

#You can also make a list using the list() constructor.
thislist3 = list(('apple', 'banana', 'cherry'))
print(thislist3)

#List items are indexed and you can access them by referring to the index number. The first item is always 0
thislist4 = ['apple', 'banana', 'cherry']
print(thislist[1])

#Negative indexing means start from the end. -1 refers to the last item, -2 refers to the second last item
thislist5 = ['apple', 'video games', 'weed']
print(thislist5[-1])

#You can specify a range of indexes by specifying where to start and where to end the range
thislist6 = ['pussy', 'money', 'orange', 'kiwi', 'watermelon', 'mango', 'grapes']
print(thislist6[2:5])

#Returns the items from the beginning to
thislist7 = ['apple', 'banana', 'grapes', 'orange', 'kiwi', 'melon', 'cherry']
print(thislist7[:4])

#Vice versa
thislist8 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#Negative indexing means starting from the end of the list. This example returns the items from index -4 (included) to index -1 (excluded)
thislist9 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist9[-4:-1])

#To determine if a specified item is present use the in keyword
thislist10 = ["apple", "banana", "cherry"]
if "apple" in thislist10:
  print("Yes, 'apple' is in the fruits list")

#To change the value of a specific item, refer to the index number.
thislist11 = ["apple", "banana", "cherry"]
thislist11[1] = "blackcurrant"
print(thislist11)

#To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values.
thislist12 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist12[1:3] = ["blackcurrant", "watermelon"]
print(thislist12)

#If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly.
thislist13 = ["apple", "banana", "cherry"]
thislist13[1:2] = ["blackcurrant", "watermelon"]
print(thislist13)

#To insert a new list item, without replacing any of the existing values, we can use the insert() method.
thislist14 = ["apple", "banana", "cherry"]
thislist14.insert(2, "watermelon")
print(thislist14)

#To insert a list item at a specified index, use the insert() method.
thislist15 = ["apple", "banana", "cherry"]
thislist15.insert(1, "orange")
print(thislist15)

#To append elements from another list to the current list, use the extend() method. The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist16 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist16.extend(tropical)
print(thislist16)












  