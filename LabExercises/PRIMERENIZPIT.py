#1.Напишете програма на Python, за да получите следващия ден от дадена дата.
     #Input a year: 2016                                                      
     #Input a month [1-12]: 08                                                
     #Input a day [1-31]: 23                                                  
     #The next date is [yyyy-mm-dd] 2016-8-24 

'''year = int(input("Input a year: "))

if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

month = int(input("Input a month [1-12]: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30


day = int(input("Input a day [1-31]: "))

if day < month_length:
    day += 1
elif day == month_length:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
        
if 1 <= day <= month_length and 1 <= month <= 12:
    print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))
else:
    print('Invalid date')'''

#2.Да се състави програма на Python, която дефинира клас Travel с полета: ID, Destination, Flight, Price. Да се добави
#метод „Reduce“, чрез който всички стойности от полето Price по-големи от 200 да бъдат заменени със стойност по-ниска
#с 10%. Да се добави и методът Print, чрез който да се отпечатят ID, Destination, Flight, Price.'''

'''class Travel:
    def __init__(self, ID, Destination, Flight, Price):
        self.ID = ID
        self.Destination = Destination
        self.Flight = Flight
        self.Price = Price

    def Reduce(self):
        if self.Price > 200:
            self.Price -= self.Price/10

    def Print(self):
        print(f"ID: {self.ID}\n"
              f"Destination: {self.Destination}\n"
              f"Flight: {self.Flight}\n"
              f"Price: {self.Price}")


bg_to_sb = Travel(ID = "1235BG-SB", Destination = "SB", Flight = "BG-TO-SB", Price = 250)
bg_to_sb.Print()
bg_to_sb.Reduce()
print("---------")
bg_to_sb.Print()'''


'''2 nacin'''

# class Travel:
#     def __init__(self, id, dest: str, flight, price: float):
#         self.id = id
#         self.dest = dest
#         self.flight = flight
#         self.price = price

#     def reduce(self):
#         if self.price > 200:
#             self.price = round(self.price - self.price * 10 / 100, 2)

#     def print(self):
#         print(str.format("ID {} - {}\n Flight: {}\n Price: {} \n", self.id, self.dest, self.flight, self.price))


# tr_list = [Travel("12B31", "Hamburg", "2:33", 176), Travel("41C7V", "Milan", "1:47", 88), Travel("77ZS2D", "New York", "4:18", 215)]

# for tr in tr_list:
#     tr.reduce()

# for tr in tr_list:
#     tr.print()









