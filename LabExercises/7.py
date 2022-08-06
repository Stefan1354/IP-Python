'''Da se sastavi programa, koqto obrshta cifrite
na dadeno cislo:'''
# primer: 76542  da se izvede 24567

num = input("Enter num: ")
for i in range(len(num) -1, -1, -1):
    print(num[i], end='')
