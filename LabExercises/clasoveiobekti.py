#klasove i obekti
#sazdavane na klas s ime i svoistvo:
'''class MyFirstClass:
    x=5'''

#sazdavane na obekt, baziran na sazdadeniq klas:#
'''MyFirstObject=MyFirstClass()'''

#funkciq konstruktor  __init__()

'''class Person:
           def __init__(self,name,age):
               self.name=name
               self.age=age
MyPerson=Person("Ivan",35)
print(MyPerson.name)
print(MyPerson.age)'''

#Metodi:
'''class Person:
           def __init__(self,name,age):
               self.name=name
               self.age=age
            def greetings(self):
                print("Hello, my name is "+self.name)
MyPerson=Person("Ivan", 35)
MyPerson.greetings()'''

#parametur self

#promqna stoinostite na svojstva na obekti:
'''MyPerson.age=40'''

#iztrivane svojstva na obekti s del:
'''del MyPerson.age'''

#iztrivane na celi obekti s del:
'''del MyPerson'''

#definirane na klas bez sudurzanie (pass)
'''class Person:
          pass'''




# class Person:
#     count_instance=0
#     def __init__(self, first_name, last_name, age):
#         Person.count_instance+=1
#         self.first_name=first_name
#         self.last_name=last_name
#         self.age=age

#     def count_instances(cls):
#         return f"You have created {cls.count_instance} instances of Person class"

#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"

#     def is_above_18(self):
#         return self.age>18

# p1=Person('Stefan', 'Stoilkov', 19)
# p2=Person('Andrija', 'Stoilkov', 16)
# print(p1.count_instances())           #You have created 2 instances of Person class
# print(p1.full_name())                 #Stefan Stoilkov
# print(p2.full_name())                 #Andrija Stoilkov
# print(p2.age)                         #16
# print(p2.last_name)                   #Stoilkov



#How objects interact (students and courses example)

'''class Student:
    def __init__(self, name, age, grade):
        self.name=name
        self.age=age
        self.grade=grade 
    
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name=name
        self.max_students=max_students
        self.students=[]

    def add_student(self, student):
        if len(self.students)<self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value=0
        for student in self.students:
            value+=student.get_grade()
        return value/len(self.students)

s1=Student("Tim", 19, 95)
s2=Student("Bill", 19, 75)
s3=Student("Jill", 19, 65)

course=Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.students[0].name)    #Tim
print(course.students[1].age)     #19
print(course.students[0].grade)   #95
print(course.get_average_grade()) #85.0 (racuna samo na prvite dva studenta jer sme samo ni dodali)'''

#Inheritance (dog and cat example) 

'''class Pet:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what I say")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color=color

    def speak(self):
        print("Meow")
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p=Pet("Tim", 19)
p.show()             #I am Tim and I am 19 years old
p.speak()            #I don't know what I say
c=Cat("Bili",34,"Brown")
c.show()             #I am Bili and I am 34 years old and I am Brown
c.speak()            #Meow
d=Dog("Jill",25)
d.show()             #I am Jill and I am 25 years old
d.speak()            #Bark
f=Fish("Bubbles",10)
f.speak()            #I don't know what I say'''


#Class attributes (person example)

'''class Person:
    number_of_people = 0
    GRAVITY = -9.8

    def __init__(self, name):
        self.name=name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people+=1

p1=Person("Tim")
p2=Person("Jill")
print(Person.number_of_people_())   #2'''


#Static methods (math example)


class Math:
    @staticmethod
    def add5(x):
        return x+5

    @staticmethod
    def add10(x):
        return x+10

    @staticmethod
    def pr():
        print("run")

print(Math.add5(5))  #10
print(Math.add10(5)) #15
print(Math.pr())     #run
                     #None









