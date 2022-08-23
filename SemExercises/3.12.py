#1.Напишете програма, в която е дефиниран клас със следните характеристики:
#Класът има конструктор, на който се предават две стойности.Тези стойности се присвояват 
#на полетата на обекта от дадения клас. В класа трябва да бъде описан метод, при извикването на 
#който се показват стойностите на полетата на класа. Проверете функционалността на класа , 
#като създадете на негова основа няколко обекта.

# class Person:
#     def __init__(self, name, family):
#        self.name=name 
#        self.family=family

#     def print_information(self):
#         print(self.name, self.family)

# Person1=Person("Lebron","James")
# Person2=Person("Ray","Allen")

# Person1.print_information()
# Person2.print_information()

#2.Напишете програма, в която е описан клас. Обектите на класа трябва да имат поле, 
#представляващо числов списък. Този списък се формира на основата на списък, 
#предаден като аргумент на конструктора. При това от  списъка аргумент в списъка поле се включват само
#числовите елементи (елементите от други типове се игнорират). Също така трябва да се дефинират два метода :
#първият метод показва съдържанието на полето списък, а вторият метод изчислява средната стойност
#на елементите на полето списък.

# class Numbers:
#     def __init__(self, newList:list):
#         self.list=[]
#         self.setList(newList)
#     def print(self):
#         print(self.list)
#     def setList(self,list):
#         for i in range(len(list)):
#             try:
#                 a=int(list[i])
#                 self.list.append(a)
#             except ValueError:
#                 print(str(list[i]) + " is not a number ")

#     def average(self):
#         sum=0
#         for i in range(len(self.list)):
#             sum+=self.list[i]
#         print(sum/len(self.list))

# b=[5,6,40,"cat",646,"horse"]
# a=Numbers(b)
# a.print()
# a.average()

#2 nacin

# class List:
#     def __init__(self,l1):
#         self.l1=[el for el in l1 if type(el)==int]

#     def print(self):
#         print(self.l1)

#     def Average(self):
#         print(sum(self.l1)/len(self.l1))

# l1=[5,10,'abc',100,'fly',50]

# n=List(l1)
# n.print()
# n.Average()


#3.Напишете програма, в която е описан клас и функция , предназначена за създаване на списък от обекти.
#Обектите на класа трябва да имат поле (предназначено за записване на целочислена стойност). 
#При извикване на функцията се предава като аргумент цяло число, определящо броя на обектите в списъка. 
#Полетата на обектите се запълват с цели нечетни числа.

# class List:
#     def __init__(self,n):
#         self.number=n

# def class_generator(count):
#     list_of_obj=[]
#     for i in range(count,0,-1):
#         if i%2==0:
#             j=i-1
#         else:
#             j=i
#         n=List(j)
#         list_of_obj.append(n)
#     return list_of_obj

# obj_list=class_generator(5)
# for obj in obj_list:
#     print(obj.number)


#4.Напишете програма, в която е описана функция. На функцията се предават като аргументи два обекта
#от един и същи клас. Всеки обект има поле представляващо списък от цели числа. Функцията връща като резултат
#обект от същия клас. Полето списък на този обект се получава посредством сумирането на съответните елементи от
#полетата списъци на обектите , предадени като агументи на функцията. Ако в тези обекти списъците са с различна
#дължина, то недостигащите елементи в списъка се запълват с нули.


# class Data:
#     def __init__(self, new_list):
#         self.new_list = new_list


# obj1 = Data([1,3,5,8])
# obj2 = Data([1, 2, 3, 4])


# # obj1 = Data([1, 2, 3, 4])
# # obj2 = Data([1])


# def get_obj_sum(a: Data, b: Data):
#     list_a = a.new_list
#     list_b = b.new_list
#     diff = len(list_a) - len(list_b)

#     if diff > 0:
#         for i in range(diff):
#             list_b.append(0)
#         length = len(list_a)
#     else:
#         for i in range(abs(diff)):
#             list_a.append(0)
#         length = len(list_b)

#     list_res = list()

#     for i in range(length):
#         list_res.append(list_a[i] + list_b[i])
#     return Data(list_res)


# print(get_obj_sum(obj1, obj2).new_list)




