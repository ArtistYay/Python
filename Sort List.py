# List objects have a sort() method that will sort the list alphanumerically, ascending, by default.
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# You can also do it numerically.
thislist2 = [100, 50, 65, 82, 23]
thislist2.sort()
print(thislist2)

# To sort descending, use the keyword argument reverse = True
thislist3 = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist3.sort(reverse = True)
print(thislist3)

# You can customize your own function by using the keyword argument key = function
def myfunc(n):
  return abs(n - 50) # Sort the list based on how close the number is to 50

thislist4 = [100, 50, 65, 82, 23]

thislist4.sort(key = myfunc)

print(thislist4)

# By default the sort() method is case sensitive. Capital will be sorted before lower case. You can use built in key functions.
def myfunc2(n):
  return abs(n - 50)

thislist5 = [100, 50, 65, 82, 23]

thislist5.sort(key = myfunc2)

print(thislist5)

# You can use the reverse() method to reverse the orger of a list regardless of the alphabet.
thislist6 = ["banana", "Orange", "Kiwi", "cherry"]
thislist6.reverse()
print(thislist6)

