#A variable is a container for storing data values.
x = 5
print(x)

#If you want to specify the data type of a variable, this can be done with casting.
x = str(3) #x will be '3'
y = int(3) #y will be 3
z - float(3) #z will be 3.0

#You can get the data type of a variable with the type() function.
x = 5
print(type(x)) #x will be an int

#Variable names are case sensitive
a = 4
A = "Sally"
#A will not overwrite a

#Python allows you to assign values to multiple variables in one line
x, y, z = "Orange", "Banana", "Cherry"

#You can also assign the same value to multiple variables in one line.
x = y = z = "Orange"

#If you have a tuple python allows you to extract the values into variables
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x) #will print apple
print(y) #will print banana
print(z) #will print cherry

#Variables that are created outside of a function are known as global variables.
x = "awesome"
def myfunc(): #making a function
    print("Python is " + x) #giving it a rule so we're printing "Python is awesome"
myfunc() #calling the function

#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
x = "awesome"
def myfunc2():
    x = "fantastic"
    print("Python is " + x)
myfunc2()

#To create a global variable inside a function, you can use the global keyword.
def myfunc3():
    global x
    x = "fantastic"
myfunc3
print("Python is " + x)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword.
x = "awesome"
def myfunc4():
    global x #can use global to change the variable from local
    x = "fantastic"
myfunc4()
print("Python is " + x)

#Python has the following data types built in default:
#Text type - str
#Numeric types - int, float, complex
#Mapping type - dict
#Set types - set, frozenset
#Boolean type - bool
#Binary type - bytes, bytearray, memoryview