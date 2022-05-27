name = (input('What is your name? ')) #asked the user whats their name
distance = float(input('How far did you travel? ')) #asked the user how far they traveled and convert it into a float which is needed to divide with the distance
coversion = 1.609 #one mile is 1.609km
miles = distance / coversion
print('Hello ' f'{name.title()}  you traveled {distance} km which is {round(miles,1)} in miles')
#print statment added the user's name and capatilized the first letter, secondly added the distance in km they traveled, and lastly rounded the miles by 1