#1.Напишете програма, която дава възможност на потребителя да въвежда неограничен брой цели числа. 
#Да се изведе какъв е процента на числата ,които са кратни на 7, резултата да се закръгли до втория знак след 
#десетичната запетая . Да се изведе каква е сумата на числата , които не са кратни на 7.
#Да се изведе максималното число измежду всички числа. Да се намери средноаритметичното на числата кратни на седем,
#резултата да се закръгли до втория знак след десетичната запетая.

print("Enter the word 'stop' to stop the loop")
li = []
li_dev_by_7 = []

while True:
    input_command = input("enter command or element ")
    if input_command=="stop":
        break
    elem = int(input_command)
    li.append(elem)
    if elem%7==0:
        li_dev_by_7.append(elem)
print(li)
print(li_dev_by_7)
print(f"{(len(li_dev_by_7)/len(li))*100:.2f}% ot chislata se delqt na 7")

print(f"Sumata na chislata koito ne sa kratni na 7 e {sum(li)-sum(li_dev_by_7)}")

print(f"Max={max(li)}")

print(f"Sredno na chislata kratni na 7 e {sum(li_dev_by_7)/len(li_dev_by_7):.2f}")

#2.Да се напише програма, която реализира играта „познай числото“ : потребителя въвежда цяло число в интервала от
#1 до 10. Програмата също генерира едно случайно число. Ако потребителя е въвел същото число ,което е генерирано от
#програмата се принтира съобщение : „Позна числото“ ,   в противен случай се принтира съобщение : 
#„Съжалявам не позна “. и така продължава този процес на въвеждане на число докато потребителя не въведе 0 , 
#нулата е знак за край на играта. След като приключи играта на екрана да се принтира общия брой опити на 
#потребителя, както и броя на познатите числа.


import random
br = random.randint(1,10)

for i in range(10, 0, -1):
    n = int(input("Enter n: "))
    
    if n==br:
        print("pozna chisloto")
        break

    if n!=br:
        print("Suzelqvam, ne pozna")
        print(f"Imas oshte {i-1} opita")

print(f"The computer imagined the number {br}.")


'''2 nacin'''
import random, sys

count, trys = 0, 0
while True:
    rand_num = random.randint(1, 10)
    while True:
        print(rand_num)
        ur_num = int(input("Guess the number: "))
        if rand_num > ur_num:
            print('WRONG!')
            trys += 1
        elif ur_num > rand_num:
            print('WRONG!')
            trys += 1
        else:
            print("You guessed the number: ", rand_num)
            count += 1
            break

        if ur_num == 0:
            print("Wins: ", count, "Trys", trys - 1)
            sys.exit()


#3.Сезона за каране на ски е вече тук. Сформира се голяма група приятели, които възнамеряват да отидат на ски 
#почивка. Някои от тях се нуждаят от подновяване на  екипировката си. Ето защо първоначално трябва да се прочете 
#броя на скиорите, които ще купят екипировка. След това на отделни редове  получаваме броя на якета, каски и ски
#обувките, които ще бъдат закупени от  един скиор. Трябва да се има предвид следния ценоразпис: 
#• Якета - 120 лв. 
#• Каски – 75 лв. 
#• Комплект обувки – 299,90 лв. 
#Към крайната сума се начислява допълнително 20% ДДС. Да се напише програма,  която изчислява общата сумата, която скиорите трябва да заплатят.
#Забележка: Един скиор съвсем спокойно може да закупи повече от 1 яке, каска или  комплект обувки.

count = int(input("broq na skiorite: "))
sum = 0

for i in range(count):
    jacket = int(input("jackets: "))
    helmet = int(input("helmet: "))
    ski = int(input("ski: "))

    sum += jacket*120 + helmet*75 + ski*299.90

print("Sumata e ",round((sum*20/100 + sum), 2))


#4.Дефинирайте  клас Phone със следните полета : марка, модел, цена, количество. В класа е дефиниран и метод ,който принтира стойностите на полетата.
#Създайте функция, която връща списък с обекти от класа Phone .
#Принтирайте информация за телефона с максимална цена.
#Намерете средноаритметичното от цените на всички телефони в списъка.
#Изведете списък на всички телефони от дадена марка ( въвежда се от клавиатурата ).

class Phone:
    def __init__(self, brand, model, price, quantity):
        self.brand = brand
        self.model = model
        self.price = int(price)
        self.quantity = int(quantity)

    def __str__(self):
        return str.format("{} {}: {}, Quantity: {}", self.brand, self.model, self.price, self.quantity)


def get_phones(size):
    res = list()
    for i in range(size):
        res.append(Phone(input("Brand: "), input("Model: "), input("price: "), input("Quantity: ")))
    return res


def get_max_pr(ph_list: list):
    ph_list.sort(key=lambda el: el.price, reverse=True)
    return ph_list[0]


def get_arg_price(ph_list: list):
    count, total, = 0, 0
    for i in ph_list:
        count += i.quantity
        total += i.price * i.quantity
    return total / count


def get_brand(ph_list: list, brand):
    res = list()
    for i in ph_list:
        if i.brand == brand:
            res.append(i)
    return res


my_list = get_phones(2)
print(get_max_pr(my_list))
print(get_arg_price(my_list))
print(get_brand(my_list, input("Brand: ")))


'''2 nacin'''
class Phone:
    def __init__(self, brand, model, price, quantity):
        self.brand = brand
        self.model = model
        self.price = price
        self.quantity = quantity

    def print_info(self):
        print(f"{self.brand} {self.model}: {self.price}$\nOnly {self.quantity} left")

def phone_list():
    phones = []
    phones.append(Phone("Samsung", "S3", 400, 10))
    phones.append(Phone("Samsung", "S4", 500, 5))
    phones.append(Phone("Huawei", "p4", 200, 5))
    phones.append(Phone("Samsung", "S8", 450, 5))
    phones.append(Phone("Samsung", "S10", 550, 5))
    phones.append(Phone("Huawei", "P5", 600, 5))
    phones.append(Phone("iPhone", "20", 900, 1))

    return phones

# Finding the max price
phones = phone_list()
max_phone_price = phones[0]
for phone in phones:
    if phone.price > max_phone_price.price:
        max_phone_price = phone

max_phone_price.print_info()

sum_prices = 0
for phone in phones:
    sum_prices += phone.price
avg_price = round(sum_prices / len(phones), 2)
print(f"Average price of phones: {avg_price}$")

brand_check = input("What brand of phones do you wish to check?")
for phone in phones:
    if phone.brand == brand_check:
        phone.print_info()

#5.Напишете програма меню със следните опции:
#                                 -добавяне на студент
#                                 -търсене на студент по език
#                                 -извеждане на информация за всички студенти
#                                 -изход
#За целта създайте клас Student със полета: номер на студент, име на студент и език за програмиране. Дефинирайте и методи:
#get_id(self),  get_name(self), get_language(self) , които връщат стойностите на полетата.
#Информацията за студентите се пази в текстов файл.
#Дефинирайте функция Add_student(student),която се използва за добавяне на информация за нов студент в текстов файл.
#Дефинирайте функция Search(language) за търсене на  студент по език .
#Дефинирайте функция Display() за принтиране на информация за всички студенти .

import pandas

class Student:
    def __init__(self, id, name, lang):
        self.id = id
        self.name = name
        self.lang = lang

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_language(self):
        return self.lang

df = pandas.read_csv('table.csv')

def add_student(id, name, language):
    global df
    student = {
        'id': id,
        'name': name,
        'language': language
    }
    df = df.append(student, ignore_index=True)
    df.to_csv('table.csv', index=False)

def search_student(language):
    for index, row in df.iterrows():
        if row['language'] == language:
            print(row.to_string())

def display():
    print(df.to_string())

add_student(128, 'Giorno', 'C++')

search_student('Python')

display()
