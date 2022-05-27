#You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set4 = {"a", "b" , "c"}
set5 = {1, 2, 3}

set4.update(set5)
print(set4)

#The intersection_update() method will keep only the items that are present in both sets.
#Same with intersection()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x) #Will print out apple

#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
#Same with symmetric_difference()
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}

a.symmetric_difference_update(b)

print(a) #Will print out everything expect apple

