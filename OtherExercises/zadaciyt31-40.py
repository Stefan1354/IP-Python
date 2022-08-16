'''31.Data su dva razlicita dvocifrena broja.Ispisati onaj
ciji je zbir cifara veci.Ukoliko je zbir isti ispisati broj
koji je veci.'''

a = int(input("Unesite prvi broj: "))
b = int(input("Unesite drugi broj: "))
za = a//10 + a%10  #a celobrojno sa 10 plus a ostatak sa 10 
               #cifra desetica plus cifra jedinica
zb = b//10 + b%10
if za>zb:
    print(a)
elif zb>za:
    print(b)
else:
    if a>b:
        print(a)
    else:
        print(b)

'''32.Data su 4 cela broja.Ispisati zbir parnih brojeva.'''

a = int(input("Unesite prvi broj: "))
b = int(input("Unesite drugi broj: "))
c = int(input("Unesite treci broj: "))
d = int(input("Unesite cetvrti broj: "))
zbir = 0
if a%2==0:
    zbir = zbir + a
if b%2==0:
    zbir = zbir + b
if c%2==0:
    zbir = zbir + c
if d%2==0:
    zbir = zbir + d 
print("Zbir je", zbir)

'''33.Data su 4 cela broja.Ispisati artitmeticku sredinu
brojeva koji su deljivi sa 3.'''

a = int(input("Unesi prvi broj: "))
b = int(input("Unesi drugi broj: "))
c = int(input("Unesi treci broj: "))
d = int(input("Unesi cetvrti broj: "))
s = 0   #zbir deljivih sa 3
br = 0  #brojac deljivih sa 3
if a%3==0:
    s = s + a
    br = br + 1
if b%3==0:
    s = s + b
    br = br + 1
if c%3==0:
    s = s + c
    br = br + 1
if d%3==0:
    s = s + d
    br = br + 1
if br==0:
    print("Nema deljivih sa 3")
else:
    print(s/br)


'''34.Data su 3 cela broja.Sabrati sve dvocifrene brojeve.'''

a = int(input("Unesi prvi broj: "))
b = int(input("Unesi drugi broj: "))
c = int(input("Unesi treci broj: "))
zbir = 0
if a>9 and a<100:
    zbir = zbir + a
if b>9 and b<100:
    zbir = zbir + b
if c>=10 and c<=99:
    zbir = zbir + c
print("Zbir dvocifrenih je", zbir)

'''35.Dat je cetvorocifren broj.Ispisati kolicnik najmanje
i zbira ostale tri cifre.'''


n = int(input("Unesi cetvorocifreni broj "))
a = n//1000    #cifra hiljada
b = n//100%10  #cifra stotina
c = n//10%10   #cifra desetica
d = n%10       #cifra jedinica
najc = a
if b<najc:
    najc = b
if c<najc:
    najc = c
if d<najc:
    najc = d
zbir = a + b + c + d - najc
print("Kolicnik je", najc/zbir)

#2.nacin
n = int(input("Unesite cetvorocifreni broj: "))
a = n//1000
b = n//100%10
c = n//10%10
d = n%10
najc = min(a,b,c,d)
zbir = a + b + c + d - najc
print("Kolicnik je", najc/zbir)

'''36.Generisati slucajan trocifren broj.Ispisati najveci 
trocifreni broj koji se moze formirati od njegovih cifara.'''

import random
n = random.randint(100,999)
#n=275
a = n//100   #cifra stotina
b = n//10%10 #cifra desetica
c = n%10     #cifra jedinica
najmanja = min(a,b,c)
najveca = max(a,b,c)
srednja = a + b + c - najmanja - najveca
broj = najveca*100 + srednja*10 + najmanja
print("Slucajan broj {}   Najveci broj {}".format(n,broj))

'''37.Napisati program kojim se za uneti redni broj meseca
ispisuje broj dana u tom mesecu.Smatrati da godina nije
prestupna.Smatrati da je mesec ispravno unet(1-12).'''

m=int(input("Unesite redni broj meseca "))
if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    broj_dana=31
elif m==4 or m==6 or m==9 or m==11:
    broj_dana=30
else:
    broj_dana=28
print("Broj dana je", broj_dana)

'''38.Napisati program kojim se za uneti mesec i godinu
ispisuje broj dana u tom mesecu. Smatrati da je vrednost
za mesec ispravna (1-12).'''

m,g=map(int,input().split('.'))
print(m,g)  #naredba map izrsava funkciju koju navedemo kao
            #prvi parametar, a split razdvaja podatke
            #ukoliko se u naredbi split ne stavi nikakav 
            #parametar, smatra se da su podaci razdvojeni razmacima.
if m==4 or m==6 or m==1 or m==11:
    broj_dana = 30
elif m==2:
    if(g%4==0 and g%100!=0) or (g%400==0):   #Prestupna godina
        broj_dana = 29
    else:
        broj_dana = 28        #Godina koja nije prestupna
else:
    broj_dana = 31
print("Broj dana je ", broj_dana)

'''39.Dat je datum(dan,mesec i godina).Ispisati datum narednog dana.'''

d,m,g=map(int,input("Unesite dan,mesec i godinu ").split('.'))
d = d + 1
if m==4 or m==6 or m==9 or m==11:
    broj_dana = 30
elif m==2:
    if(g%4==0 and g%100!=0) or (g%400==0):
        broj_dana = 29
    else:
        broj_dana = 28
else:
    broj_dana = 31
if d>broj_dana:
    d = 1
    m = m + 1
else:
    if m>12:
        m = 1
        g = g + 1
    
print("Naredni datum je ", d,'.',m,'.',g)

'''40.Dat je dan(dan,mesec,godina).Ispisati datum prethodnog dana.'''

year = int(input("Input a year: "))

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

if day > 1:
    day -= 1
elif day == 1:
    if month in (1, 2, 4, 6, 8, 9, 11):
        day = 31
    elif month == 3:
        if leap_year:
            day = 29
        else:
            day = 28
    else:
        day = 30
    if month == 1:
        month = 12
        year -= 1
    else:
        month -= 1
        
if 1 <= day <= month_length and 1 <= month <= 12:
    print("The previous date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))
else:
    print('Invalid date')

#BONUS ZADATAK

'''Dat je dan(dan,mesec,godina).Ispisati datum sledeceg dana.'''

'''1. nacin'''

# year = int(input("Input a year: "))

# if (year % 400 == 0):
#     leap_year = True
# elif (year % 100 == 0):
#     leap_year = False
# elif (year % 4 == 0):
#     leap_year = True
# else:
#     leap_year = False

# month = int(input("Input a month [1-12]: "))

# if month in (1, 3, 5, 7, 8, 10, 12):
#     month_length = 31
# elif month == 2:
#     if leap_year:
#         month_length = 29
#     else:
#         month_length = 28
# else:
#     month_length = 30


# day = int(input("Input a day [1-31]: "))

# if day < month_length:
#     day += 1
# else:
#     day = 1
#     if month == 12:
#         month = 1
#         year += 1
#     else:
#         month += 1
# print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))


'''2. nacin'''

# day, month, year = map(int, input("Enter date: ").split('/'))
 
# if month == 2:
#     if year % 4 != 0:
#         d_max = 28
#     else:
#         d_max = 29
         
# elif month in [4, 6, 9, 11]:
#     d_max = 30
 
# else:
#     d_max = 31
 
# if 1 <= day <= d_max and 1 <= month <= 12:
#     if day == d_max:
#         day = 1
#         if month == 12:
#             month = 1
#             year += 1
#         else:
#             month += 1
#     else:
#         day += 1
#     print(str(day) + "/" + str(month) + "/" + str(year))
# else:
#     print("Invalid date")
