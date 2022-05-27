#Creating a tuple is called packing.

#Extracting the values back into variables is called unpacking
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.
fruits2 = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits2

print(green) #Will print out apple
print(yellow) #Will print out banana
print(red) #Will put out the rest of the tuple

