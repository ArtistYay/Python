#You can loop through a tuple using a for loop
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#You can loop by referring to their index number. Use the range() and len()
thistuple2 = ("apple", "banana", "cherry")
for i in range(len(thistuple2)):
  print(thistuple2[i])

#You can also use the while function. Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by refering to their indexes. Remember to increase the index by 1 after each iteration.
thistuple3 = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple3):
  print(thistuple3[i])
  i = i + 1