#price=10
#price=20
#print(price)  #20

#name=input("What is your name? ") #John
#favourite_color=input("What is your favourite color? ")
#print(name+' likes ' + favourite_color) #John likes red

'''birth_year=input("Birth year: ")
print(type(birth_year)) #class str
age=2019-int(birth_year)
print(type(age)) #class int
print(age) #17'''

#weight_lbs=input('Weight (lbs): ') #50
#weight_kg=int(weight_lbs)*0.45
#print(weight_kg) #22.5

#course="Python's Course for Begginers"
#print(course) #Python's Course for Begginers



course='''
Hi John,
Here is our first email to you.
Thank you,
The support team
'''
#print(course)   #Hi John,
                #Here is our first email to you.
                #Thank you,
                #The support team

#course='Python for begginers'
#print(course[0]) #P
#print(course[6]) #prazan red(razmak)
#print(course[3]) #h
#print(course[10]) #prazan red (razmak)
#print(course[:]) #Python for begginers

#name='Jennifer'
#print(name[1:-1]) #ennife

'''first='John'
last='Smith'
message=first+'[' + last + '] is a coder'
msg=f'{first} [{last}] is a coder'
print(msg) #John [Smith] is a coder
print(message) #John [Smith] is a coder'''

'''course='Python for Beginners'
print(len(course)) #20
print(course.upper()) #PYTHON FOR BEGINNERS
print(course.lower()) #python for beginners
print(course.find('P')) #0
print(course.find('o')) #4
print(course.find('Beginners')) #11
print(course.replace('Beginners', 'Absolute Beginners')) #Python for Absolute Beginners
print(course.replace('P','J')) #Jython for Beginners
print('Python' in course) #True'''


#print(10/3) #3.3333333335
#print(10%3) #1
#print(10**3) #1000

#x=10
#x=x+3
#print(x) #13

#x=10
#x+=3
#print(x) #13

#x=5
#x-=3
#print(x) #2

#x=10+3*2
#print(x) #16
#parenthesis
#exponentation 2**3
#multiplication or division 
#addition or subtraction

#x=10+3*2**2
#print(x) #22 (10+3*2^2=10+3*4=10+12=22)

#x=(10+3)*2**2
#print(x) #52

#x=2.9 
#print(round(x)) #3
#print(abs(-2.9)) #2.9

#import math
#x=int(input("Enter x "))
#y=int(input("Enter y "))
#print (math.pow(x,y)) #stepen nekog broja

#import math
#print(math.floor(2.9)) #2
#print(math.factorial(5)) #120

# is_hot=True
# if is_hot:
#     print("It's a hot day") #It's a hot day
#     print("Enjoy your day") #Enjoy your day
    
'''is_hot=False
if is_hot:
    print("It's a hot day") #It's a hot day
    print("Enjoy your day") #Enjoy your day
else:
    print("It's a cold day")
    print("Wear warm clothes")
print("Enjoy your day")

printira 
It's a cold day
Wear warm clothes
Enjoy your day'''

''' 1.Price of a house is #1M.If buyer has good credit,
the need to put down 10%
Otherwise
they need to put down 20%
Print the down payment.'''

# price=1000000
# has_good_credit=True

# if has_good_credit:
#     down_payment=0.1*price
# else:
#     down_payment=0.2*price
# print(f"Down payment: ${down_payment}")  #Down payment: $100000.0

'''Logical operators'''

'''if applicant has high income AND good credit
    Eligible for loan'''

#has_high_income=True
#has_good_credit=True

#if has_high_income and has_good_credit:
    #print('Eligible for loan')  #Eligible for loan

# has_high_income=False
# has_good_credit=True
# if has_high_income or has_good_credit:
#     print("Eligible for loan")   #Eligible for loan

'''AND: both
OR: at least one 
NOT '''

# has_good_credit=True
# has_criminal_record=True
# if has_good_credit and not has_criminal_record:
#     print("Eligible for loan") #Eligible for loan


# temperature=30
# if temperature>30:
#     print("It's a hot day")
# else:
#     print("It's not a hot day")  #It's not a hot day


# name="Stefan"
# print(len(name)) #1
# if len(name)<3:
#     print("Name must be at least 3 characters ")
# elif len(name)>50:
#     print("Name must be a maximum of 50 characters")
# else:
#     print("Name looks good!")

#Weight converter:

# weight=int(input("Weight: "))
# unit=input("(L)bs or (K)kg: ")
# if unit.upper()=="L":
#     converted=weight*0.45
#     print(f"You are {converted} kilos")
# else:
#     converted=weight/0.45
#     print(f"You are {converted} pounds")     #Weight: 160
                                              #(L)bs or (K)kg: l
                                              #You are 72.0 kilos

                                              #Weight: 72
                                              #(L)bs or (K)kg: K
                                              #You are 160.0 pounds


#While Loops

#i=1
#while i<=5:
    #print(i)
    #i=i+1 #bez ovaj red programo nema da prestae da raboti jer e 1 po malenko od 5
#print("Done")    #1 2 3 4 5 Done (sve edno ispod drugo)

# i=1
# while i<=5:
#     print('*'*i)
#     i=i+1
# print("Done")    # *
                 # **
                 # ***
                 # ****
                 # *****
                 #Done


# secret_number=9
# guess_count=0
# guess_limit=3
# while guess_count<guess_limit:
#     guess=int(input("Guess: "))
#     guess_count+=1
#     if guess==secret_number:
#         print("You won! ") 
# #uvek imame 3 pokusaja, ako pogodime iz prva, pise ni You won! i dava ni jos 2 puti da pokusame

# secret_number=9
# guess_count=0
# guess_limit=3
# while guess_count<guess_limit:
#     guess=int(input("Guess: "))
#     guess_count+=1
#     if guess==secret_number:
#         print("You won! ") 
#         break
#ako pogodime iz prva pise ni You won! i nemame vise pokusaji

# secret_number=9
# guess_count=0
# guess_limit=3
# while guess_count<guess_limit:
#     guess=int(input("Guess: "))
#     guess_count+=1
#     if guess==secret_number:
#         print("You won! ")
#         break
# else:                              #ako e else: ispod if guess... ce printira posle svak netacan pokusaj Sorry, you failed!
#     print("Sorry, you failed! ")


#Car game

'''command=""
started=False
while True:
    command=input(">").lower()
    if command=="start":
        if started:
            print("Car is already started!")
        else:
            started=True
            print("Car started...")
    elif command=="stop":
        if not started:
            print("Car is already stopeed!")
        else:
            started=False
            print("Car stopped.")
    elif command=="help":
        print("""
start-to start the car
stop-to stop the car
quit-to quit
        """)
    elif command=="quit":
        break
    else:
        print("Sorry, I don't understand that!")'''

#For Loops

# for item in 'Python':
#     print(item)  #Python edno ispod drugo

# for item in ['Stefan','Mike']:
#     print(item) #Stefan Mike edno ispod drugo

# for item in [1,2,3,4,5]:
#     print(item) #1 2 3 4 5 edno ispod drugo

# for item in range(10):
#     print(item) #0 1 2 3 4 5 6 7 8 9

# for item in range(5,100,5):
#     print(item)  #5 10 15 20 25...95

# prices=[10,20,30]
# total=0
# for price in prices:
#     total+=price
# print(f"Total: {total}")  #Total: 60

#Nested Loops

# for x in range(4):
#     print(x) #0 1 2 3

# for x in range(4):
#     for y in range(3):
#         print(f"({x},{y})")  #(0,0)
                             #(0,1)
                             #(0,2)
                             #(1,0)
                             #(1,1)
                             #(1,2)
                             #(2,0)
                             #(2,1)
                             #(2,2)
                             #(3,0)
                             #(3,1)
                             #(3,2)

# numbers=[5,2,5,2,2]
# for x_count in numbers:
#     print('x'*x_count)  #xxxxx
#                         #xx
#                         #xxxxx
#                         #xx
#                         #xx

# numbers=[5,2,5,2,2]
# for x_count in numbers:
#     output=''
#     for count in range(x_count):
#         output+='x'
#     print(output)     #xxxxx
                      #xx
                      #xxxxx
                      #xx
                      #xx

#names=['John','Bob','Mosh','Sarah','Rianna']
#print(names[2:]) #['Mosh','Sarah','Rianna']
#print(names[:])  #printira site imenja

'''2.Write a program to find the largest number in a list.'''

#list=[5,10,20,100,500,501]
#print(max(list)) #501

#2 nacin
# numbers=[3,6,9,15,20]
# max=numbers[0]
# for number in numbers:
#     if number>max:
#         max=number
# print(max) #20


# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
#matrix[0][1]=20 #20
#print(matrix[0][1]) #20 #bez gornjio red printira 2

#for row in matrix:
    #for item in row:
        #print(item)    #1 2 3...9 edno ispod drugo

#numbers=[5,2,3,4,7,8]
#numbers.append(12)
#print(numbers) #[5,2,3,4,7,8,12]
#numbers.insert(0,10)
#print(numbers) #[10,5,2,3,4,7,8]
#numbers.remove(5)
#print(numbers) #[2,3,4,7,8]
#numbers.clear()
#print(numbers) #[]
#numbers.pop()
#print(numbers) #[5,2,3,4,7]
#print(numbers.index(5)) #0
#print(numbers.index(10)) #10 is not in the list
#print(50 in numbers) #False

#numbers=[5,3,4,7,5]
#print(numbers.count(5)) #2
#print(numbers.sort()) #None
#numbers.sort()
#numbers.reverse()
#print(numbers) #[3,4,5,5,7]

#ka e samo numbers.sort() printira ni #[3,4,5,5,7]
#ka sa numbers.sort() i numbers.reverse() printira ni #[7,5,5,4,3]

#numbers2=numbers.copy()
#numbers.append(10)
#print(numbers2) #[5,3,4,7,5]

'''3.Write a program to remove the duplicates in a list.'''

# numbers=[2,2,3,4,6,4,7,8]
# uniques=[]
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques) #[2,3,4,6,7,8]


