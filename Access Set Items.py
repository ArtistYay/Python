#You cannot access items in a set by referring to an index or a key but you can loop through the set items using a for loop.
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Or ask if a specified value is present in a set, by using the in keyword.
thisset1 = {"apple", "banana", "cherry"}

print("banana" in thisset1)