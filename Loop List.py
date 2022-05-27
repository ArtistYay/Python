#You can loop through the list items by using a for loop. Print all items in the list, one by one
thislist21 = ["apple", "banana", "cherry"]
for x in thislist21:
  print(x)

#You can also loop through the list items by referring to their index number. Use the range() and len() functions to create a suitable iterable.
thislist22 = ["apple", "banana", "cherry"]
for i in range(len(thislist22)):
  print(thislist22[i])
#Print all items by referring to their index number.

#You can loop through the list items by using a while loop. Print all items, using a while loop to go through all the index numbers.
thislist23 = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist23):
  print(thislist23[i])
  i = i + 1
#Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by refering to their indexes.Remember to increase the index by 1 after each iteration.

#A short hand for loop that will print all items in a list.
thislist24 = ["apple", "banana", "cherry"]
[print(x) for x in thislist24]