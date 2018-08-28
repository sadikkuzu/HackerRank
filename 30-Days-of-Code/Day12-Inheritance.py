# https://www.hackerrank.com/challenges/30-inheritance
# Python 3
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        av = sum(self.scores) / float(len(self.scores))
        if av>=90 and av<=100:
            return 'O'
        elif av>=80 and av<90:
            return 'E'
        elif av>=70 and av<80:
            return 'A'
        elif av>=55 and av<70:
            return 'P'
        elif av>=40 and av<55:
            return 'D'
        else:
            return 'T'

import builtins
def print(*args,**kwargs):
    if "sep" not in kwargs and args[0] =="Grade: ":
        builtins.print(*args,**kwargs,sep="")
    else:
        builtins.print(*args,**kwargs)

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade: ", s.calculate())