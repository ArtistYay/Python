#A class is like a template or a blueprint. For example a movie concept can be a class
#Objects are the actual thing you built. Like out of the movie concepts you choose to make a super hero movie and the object is 'The Batman'
#Variables => attributes 
#Functions => methods
#All classes have a function called __init__(), use the __init__() fucnction to assign values to object properties

class Movie:
    def __init__(self, title, year, rating): #The __init__() function is called automatically everytime the class is being used to create a new object.
        self.title = title
        self.year = year
        self.rating = rating

    def myfunction(self):   #Self is used to access variables that belongs to the class.
        print("Title: " + self.title)
        print("Year of release: " + self.year)
        print("Overall rating: " + self.rating)

M1 = Movie('The Batman', '2022', '6.4')

M1.myfunction()


class Grades:
    def school_year(self):
        print(self.name + " has a grade of " + self.average)

P1 = Grades()
P1.name = "Jake"
P1.average = '50.8'

P2 = Grades()
P2.name = "Artist"
P2.average = '90.8'

P1.school_year()

#you can not leave a class empty but if it is use the pass statement to avoid getting an error