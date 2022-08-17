'''Tuples'''

numbers = (1,2,3)
print(numbers[0]) #1
numbers[0]=10 
print(numbers)    #'tuple' object does not support item assignment

coordinates=(1,2,3)
x, y, z = coordinates 
print(x) #1
print(y) #2
print(z) #3

'''Dictionaries'''

customer={
    "name":"John Smith",
    "age":30,
    "is_verified":True
}
print(customer['name']) #John Smith
print(customer.get("birthdate")) #None
print(customer.get("birthdate", "1 Jan 1978")) #1 Jan 1978
customer["name"]='Jack Smith'
print(customer["name"]) #Jack Smith

phone = input("Phone: ")
digits_mapping={
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

output=""
for ch in phone:
    output+=digits_mapping.get(ch , "!")
print(output) #Phone: 1345
              #OneThreeFour!


'''Emoji Converter'''

message = input(">")
words = message.split(' ')
print(words)  #>Good morning sunshine
              ['Good','morning','sunshine']

#didn't work with emoji

'''Functions'''

def greet_user():
    print("Hi there!")
    print("Welcome aboard")
print("Start")
greet_user()
print("Finish")   #Start
                  #Hi there!
                  #Welcome aboard
                  #Finish

'''Parameters'''

def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}')
    print('Welcome aboard')
print("Start")
greet_user("John", "Smith")
print("Finish")    #Start
                   #Hi John Smith
                   #Welcome aboard
                   #Finish

'''Keyword arguments'''

def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')
print("Start")
greet_user(last_name='Smith',first_name='John')
print("Finish")    #Start
                   #Hi John Smith!
                   #Welcome aboard
                   #Finish


'''Return statement'''

def square(number):
    return number*number
result = square(3)
print(result) #9
print(square(3)) #9

def square(number):
    print(number*number)
print(square(3)) #None

try:
    age = int(input('Age: '))
    print(age)
except ValueError:
    print('Invalid value')


try:
    age = int(input("Age: "))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid value.')

'''Classes'''

class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 = Point()
point1.draw()   #draw

class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1=Point()
point1.x=10   
point1.y=20
print(point1.x)
point1.draw()  #10
               #draw

point2=Point()
point2.x=1
print(point2.x)  #1

'''Constructors'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")

point=Point(10,20)
point.x=11
print(point.x) #11

class Person:
    def talk(self):
        print("talk")

john=Person()
john.talk()  #talk

class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print('talk')  #John Smith
                       talk

class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John Smith")
john.talk()  #Hi, I am John Smith
bob = Person("Bob Smith")
bob.talk()   #Hi, I am Bob Smith

'''Inheritance'''

class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    pass

class Cat(Mammal):
    pass

dog1=Dog()
dog1.walk()  #walk

#Python doesn't like empty class.

class Mammal:
    def walk(self):
        print("self")

class Dog(Mammal):
    def bark(self):
        print("bark")

class Cat(Mammal):
    def be_annoying(self):
        print("annoying")

cat1=Cat()
cat1.be_annoying()  #annoying
