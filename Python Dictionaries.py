#Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered, changeable and do not allow duplicates. They are written with curly braces.
thisdict = {
    "brand": "Ford", #Don't forget the commas
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

#You can access the items of a dictionary by referring to its key name, inside square brackets.
print(thisdict["brand"])

#You can also use the get() method.
x = thisdict.get("model")
print(x)

#The keys() method will return a list of all the keys in the dictionary.
y = thisdict.keys()
print(y)

#The values() method will return a list of all the values in the dictionary.

z = thisdict.values()
print(z)

#The update() method will update the dictionary.
thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict2.update({"year": 2020})
print(thisdict2)

#You can add an item using a new index key and assigning a value to it.
thisdict3 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict3["color"] = "red"
print(thisdict3)

#You can use popitem(), del, pop(), or clear to remove an item.
thisdict4 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict4.pop("model")
print(thisdict4)

#You can make a copy of a dictionary with copy() and dict().
thisdict5 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict5)
print(mydict)

#A dictionary can contain dictionaries, this is called nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}



