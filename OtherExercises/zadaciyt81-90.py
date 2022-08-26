'''81.Napisati program koji racuna zbir brojeva od 1 do 100
cija je zadnja cifra 9.'''

s = 0       #promenljiva za zbir
for n in range(1, 100):
    if n%10==9:       #ako je poslednja cifra 9
        s+=n
        print(n, s)
print("Suma brojeva je ", s)

'''82.Napisati program za izracunavanje n-tog stepena celog 
broja a.'''

a = int(input("Unesite broj a: "))
n = int(input("Unesite broj n: "))
p = 1          #rezultat
for i in range(n):
     p*=a
print("Rezultat je",p)

'''83.Dat je prirodan broj N.Ispisati sve njegove delioce
i njihovu sumu.'''

n = int(input("Unesite broj n= "))
s = 0
for a in range (1, n+1):
    if n%a==0:   #da li je n deljivo sa a
        s+=a    #dodajemo delioc na sumu
        print(a)
print("Suma delioca je", s)

'''84.Napisati program kojim se stampaju svi trocifreni
brojevi koji su deljivi brojem koji se dobija
izbacivanjem srednje cifre.'''

for n in range(100, 1000):
    a = n//100       #cifra stotina
    b = n%10         #cifra jedinica
    br = a*10+b
    if n%br==0:
        print(n)      #npr 132 odbacujemo 3 132 je deljivo sa 12

'''85.Ispisati sve trocifrene brojeve koji imaju svojstvo
ABC=A+B*B+C*C*C.   (135=1+3*3+5*5*5)'''

for n in range(100, 1000):
    a = n//100        #stotine
    b = n//10%10      #desetice
    c = n%10          #jedinice
    if n==a+b**2+c**3:
        print(n)

'''86.Ispisati sve trocifrene brojeve koji su deljivi sa 7 cije
su cifre poredjane u rastucem poretku.'''

for n in range(100, 1001):
    a = n//100
    b = n//10%10
    c = n%10
    if n%7==0 and a<b and b<c:
        print(n)

'''87.Napisati program koji za dva uneta prirodna broja a i b
ispisuje onaj koji ima veci zbir delilaca.'''

a, b = map(int,input('Unesite 2 cela broja: ').split())
za = 0
for i in range(1, a+1):
    if a%i==0:
        za+=i
zb = 0
for i in range(1, b+1):
    if b%i==0:
        zb+=i
print("Zbir delilaca za {} je {}".format(a,za))
print("Zbir delilaca za {} je {}".format(b,zb))
if za>zb:
    print(a)
elif zb>za:
    print(b)
else:
    print("Zbir delilaca je isti ")

'''88.Napisati program koji za uneti dan, mesec i godinu ispisuje
koji je to po redu dan u godini.
(voditi racuna da li je godina prestupna)'''

d, m, g = map(int,input("Unesite dan, mesec i godinu d.m.g ").split('.'))
rb = d        #Broj dana u unetom mesecu
for mes in range(1, m):
    if mes==4 or mes==6 or mes==9 or mes==11:
        brd = 30
    elif mes==2:
        if (g%4==0 and g%100!=0) or (g%400==0):
            brd = 29
        else:
            brd = 28
    else:
        brd = 31
    rb+=brd       #Dodajemo broj dana u mesecu koji proveravamo
print(rb)


day, month, year = map(int, input("Input day, month and year [day.month.year]: ").split('.'))
days_until_month = day        #number of days in the entered month
for mon in range(1, month):
    if mon == 4 or mon == 6 or mon == 9 or mon == 11:
        number_of_days = 30
    elif mon == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            number_of_days = 29
        else:
            number_of_days = 28
    else:
        number_of_days = 31
    days_until_month = days_until_month + number_of_days    #We add the number of days in the month we are checking
print(days_until_month)


'''89.Napisati program koji za uneti redni broj dana u godini
i godinu ispisuje koji je to datum u godini.
(voditi racuna da li je godina prestupna)'''

rb, g=map(int, input("Unesite redni broj dana i godinu: ").split())
m = 1
for mes in range(1, 13):
    if mes==4 or mes==6 or mes==9 or mes==11:
        brd = 30
    elif mes==2:
        if (g%4==0 and g%100!=0) or (g%400==0):
            brd = 29
        else:
            brd = 28
    else:
        brd = 31
    if rb>brd:
        rb=rb-brd
        m+=1
print("Datum je {}.{}.{}".format(rb,m,g))

'''90.Napisati program kojim se racuna kolicnik 2 prirodna broja
A i B na K decimala koristeci postupak rucnog deljenja.'''

a = int(input("Unesite deljenik: "))
b = int(input("Unesite delilac: "))
k = int(input("Unesite broj decimala: "))
print(a//b,"," ,sep='',end='')   #da ne bi imalo razmaka izmedju brojeva
                                 #i da nam ne predje u sledeci red
ost = a%b * 10                   #ostatak deljenja pomnozen sa 10 (dodajemo nulu)
for i in range(k):
    print(ost//b,sep='',end='')
    ost = ost%b * 10  #ostatak deljenja pomnozen sa 10 (dodajemo nulu)
