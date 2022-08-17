#6.Напишете програма, в която е описана функция , която 
#проверява дали едно цяло число е просто, числото се 
#предава като аргумент на функцията. Функцията връща
#резултат 1 ако числото е просто и 0 ако числото не е
#просто. Да се принтират всички прости числа в интервала
#от 2 до това число.

num = int(input("Enter num: "))
def isPrime(num:int):
    for i in range(2,num):
        if num%i==0:
           return 0
    return 1
def printNumbers(num:int):
    for i in range(2,num):
        if isPrime(i)==1:
            print(i)
print(isPrime(num))
printNumbers(num)

#7.Програма английско - български речник, запълнен речник 
#със  стойности.Потребителя прави своя избор , който може 
#да е :
# - търсене на дума в речника
# - добавяне на дума
# - изтриване на дума
# - показване на всички думи в речника .
#Програмата продължава докато не се въведе  символа q- изход .
#За всяка една от опциите реализирайте отделни функции.

def add_to_dict(my_dict, key, val):
    my_dict[key] = val

def del_word(my_dict, key):
    del my_dict[key]

def search_word(my_dict, key):
    return my_dict[key]

def show_all(my_dict):
    print(my_dict)

my_dict = dict()

# preset data
my_dict['cat'] = 'kotka'
my_dict['dog'] = 'kuce'
my_dict['person'] = 'covek'

print("s - tursene na duma v recnika\n"
      "a - dobavqne na duma\n"
      "d - iztrivane na duma\n"
      "all - pokazvane na vsicki dumi v recnika\n"
      "q - izhod")

while True:
    cmd = input("Command: ")
    if cmd == 'q':
        print("END")
        break
    elif cmd == 's':
        print(search_word(my_dict, input("Enter word: ")))
    elif cmd == 'a':
        add_to_dict(my_dict, input("Enter engl word: "), input("Enter bg meaning: "))
    elif cmd == 'd':
        del_word(my_dict, input("Enter word: "))
    elif cmd == 'all':
        show_all(my_dict)
    else:
        print("invalid Input")


#8.Напишете програма, която отпечатва перфектните числа от
#даден списък с цели числа.Програмата включва   функция,
#която  получава като аргумент число и принтира числото, a
#ако то е перфектно.

# Примерен вход: [14, 20, 6, 78, 28]
#Изход:   6, 28

def perfect(num):
    delitel = [1]
    for i in range(2, num//2+1):
        if num%i==0:
            delitel.append(i)
    if sum(delitel)==num:
        print(num)
my_list = [14,38,6,78,28]
for n in my_list:
    perfect(n)

'''2 nacin'''
def perfect_number(n):
    sum = 0
    for x in range(1,n):
        if n%x==0:
            sum+=x
    return sum==n
n=int(input("Enter n: "))
print(perfect_number(n))

#9. Напишете функция,  която получава като аргумент числов
#списък. Елементите с четни индекси се сортират по възходящ 
#ред, а елементите с нечетни индекси  се сортират в 
#низходящ ред. Функцията връща като резултат променения 
#списък.

    #Пример:   Enter count : 7
    #[11, 20, 19, 4, 1, 8, 4] #първоначален списък
    #11, 19, 1, 4   # елементи с четни индекси(0,2,4,6...) 
    #1, 4, 11, 19   #сортирани във възходящ ред
    #20, 4, 8       # елементи с нечетни индекси(1,3,5,7...)
    #20, 8, 4       #сортирани в низходящ ред 
    #[1, 20, 4, 8, 11, 4, 19]  #променения списък

def new_list(list):
    list_even = [list[i] for i in range(len(list)) if i % 2 == 0]
    print("list_even: ", list_even)
    list_odd = [list[i] for i in range(len(list)) if i % 2 != 0]
    print("list_odd: ", list_odd)
    list_even.sort()
    list_odd.sort(reverse=True)

    res = []
    try:
        for i in range(len(list)):
            res.append(list_even[i])
            res.append(list_odd[i])
    except:
        pass
    return res

size = int(input("List size:"))
list = [11, 20, 19, 4, 1, 8, 4]
print(list)

print("Result:", new_list(list))


#10. Напишете програма, в която е описана функция, 
#която намира НОК на две числа. Числата се подават като 
#аргументи на функцията.

def calc_lcm(num1, num2):
    if num1 > num2:
        gr_num = num1
    else:
        gr_num = num2

    while (True):
        if gr_num % num1 == 0 and gr_num % num2 == 0:
            lcm = gr_num
            break
        gr_num += 1

    return lcm

num1, num2 = int(input("Enter num1: ")), int(input("Enter num2: "))
print("LCM:", calc_lcm(num1, num2))
