#1.Да се напише код на Пайтън който дефинира Class Person с полета име 
#(name), фамилия (family), възраст(age), националност(nationality).
#Да се дефинира конструктор (init) който инициализира полетата на класа.
#Да се добави метод print който отпечатва имената и националноста на съответното лице. 
#Да се създадат обекти инстанции на класа. За тях да се извика методът print.

'''1 nacin'''

class Person:
    def __init__ (self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality
MyPerson = Person("Stefan","Stoilkov","Bulgarian",19)
print(MyPerson)
print(MyPerson.name)
print(MyPerson.family)
print(MyPerson.age)
print(MyPerson.nationality)         #printira
                                    #Stefan
                                    #Stoilkov
                                    #Bulgarian
                                    #19


'''2 nacin'''

class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality
p1 = Person(name = input("Enter name: "), family = input("Enter family: "), age = input("Enter age: "), nationality = input("Enter nationality: "))
print(p1.name, p1.family, p1.age, p1.nationality)   #printira Stefan Stoilkov 19 Bulgarian


'''3 nacin'''

class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality
    
    def __str__(self):
        return f'{self.name} {self.family} is {self.age} age and {self.nationality} nationality '
person1 = Person('Stefan','Stoilkov',19,'Bulgarian')
print(person1)  #printira Stefan Stoilkov is 19 age and Bulgarian nationality



#2.Съставете клас на Пайтън с името Student с две свойства : student_ID и student_name . 
#Добавете ново свойство student_class. Създайте функция за извеждане на цялото свойство и 
#техните стойности в класа Student.


'''1 nacin'''

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def add_class(self, student_class):
        self.student_class = student_class

    def Print(self):
        print(self.student_name, self.student_id, self.student_class)

student1 = Student(1212121, "Stefan")
student1.add_class(43)
student1.Print()                         #printira Stefan 1212121 43


'''2 nacin'''

class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def __add__(self, student_class):
        self.student_class = student_class
    def print(self):
        print(self.name)
        print(self.id)
        print(self.student_class)

p1=Student("Ivan", 221)
p2=Student("Mitko", 222)
p1.__add__("Mathematics")
p2.__add__("Physics")
p1.print()
print()
p2.print()                  #printira
                            #Ivan
                            #221
                            #Mathematics

                            #Mitko
                            #222
                            #Physics

'''3 nacin'''

class Student:
    def __init__(self, Student_ID, Student_name):
        self.Student_ID = Student_ID
        self.Student_name = Student_name
        self.Student_class = None
    def get_info(self):
        return f'Student_ID {self.Student_ID} with Student_name {self.Student_name} is in the class {self.Student_class}'

student1 = Student(16423,'Stefan')
print(student1.get_info())    #printira Student_ID 16423 with Student_name Stefan is in the class None
