friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']

print('Eric' in friends and 'John' in friends) 
#Python will look in friends to see if eric and join is in the set using the and operator. If both is in it will print true, if only one is present it will print false.

print(friends.union(my_friends))
#Just joining both the sets together

print(friends.intersection(my_friends))
#All the names are in both the sets

print(friends.difference(my_friends))
#Finds the names that are only in friends

print(my_friends ^ friends)
#Shows only the names that are only in friends

print(set(cars))
