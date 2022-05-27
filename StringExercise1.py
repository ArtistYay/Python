#From the string "Welcome to Python 101: Strings", extract text and create a new string that says "1 Welcome Ring To Tyler"
msg = "Welcome to Python 101: Strings"
msg1 = msg[18] + ' ' + msg[:8] + msg[25:29] + msg[7:11] + msg[13] + msg[12] + msg[2] + msg[1] + msg[-5]
print(msg1)
#I used the slicing method. Basically I called a certain part of the string.

print(msg1.title())

#To reverse a string you want to tell python to start at the end of the string and end at position 0

print(msg1[::-1].title())