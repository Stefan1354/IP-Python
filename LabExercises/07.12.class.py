'''Nasledqvane'''

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname, self.lastname)

MyPerson=Person("Ivan", "Petrov")
MyPerson.printname()

class Student(Person):
    pass

MyStudent=Student("Petar","Vasilev")
MyStudent.printname()       #Ivan Petrov
                            #Petar Vasilev
                            


class Student(Person):
    def __init__(self,fname,lname):
        Person. __init__(self,fname,lname)

class Student(Person):
    def __init__(self,fname,lname):
        super(). __init__(self,fname,lname)
        self.graduationyear=2019

class Student(Person):
    def __init__(self,fname,lname,year):
           super().  __init__(self,fname,lname)
           self.graduationyear=year

MyStudent=Student("Petar", "Vasilev", 2019)


#Dopunuanje na zadaca za IZPIT:
#1) da imame nov spisak s ucenici koi sa s otlicen uspeh
#2) da se napise metod koito zapisva danni vuv fail, koito cete faila i suzdava spisuk na studentite
#3)Da se sazdade metod, koito vrushta dannite na student s ceten i oshte edin za neceten fak.nomer.
