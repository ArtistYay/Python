#The remove() method removes the specified item.
thislist17 = ["apple", "banana", "cherry"]
thislist17.remove("banana")
print(thislist17)

#The pop() method removes the specified index. If you do not specify the index, the pop() method removes the last item.
thislist18 = ["apple", "banana", "cherry"]
thislist18.pop(1)
print(thislist18)

#The del keyword also removes the specified index. The del keyword can also delete the list completely.
thislist19 = ["apple", "banana", "cherry"]
del thislist19[0]
print(thislist19)

#The clear() method empties the list. The list still remains, but it has no content.
thislist20 = ["apple", "banana", "cherry"]
thislist20.clear()
print(thislist20)

#Doing it myself
Fish = ["Snapper", "Tuna", "Cod", "Salmon", "Goldfish"]
del Fish[3]
print(Fish)

Video_Games = ["Zelda", "Destiny 2", "Mario Kart", "Elden Ring", "Smash Bros"]
Video_Games.pop(4)
print(Video_Games)
