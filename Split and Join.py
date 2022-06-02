csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'

friends_list = ((','.join(','.join(csv.split(';')).split(':'))).split(','))
#Split means to sperate a string into a list so .split(';') gets rid of the ; since it's sperated and its joined back together with a comma.

print(friends_list)

#Or to make life easier just replace the ; and : with commas then split it with a comma.
print(csv.replace(':', ',').replace(';', ',').split(','))




