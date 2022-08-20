'''61.Napisati funkciju koja vraca zbir cifara prirodnog
broja N.'''

 #Izdvajanje cifara broja kada ne znamo broj cifara
 #Primer N=256
 #SumaCifara=0
 #Radi sve dok je N>0
     #Izdvoj poslednju cifru
     #Dodaj je na SumuCifara
     #Ponisti poslednju cifru u N

def ZbirCifara(N):
    suma = 0
    while (N>0):
        c = N%10
        suma = suma + c
        N = N//10
    return suma   #vraca zbir cifara
n = int(input("Unesite broj N= "))
print("Zbir cifara je ", ZbirCifara(n))

'''62.Napisati funkciju koja vraca obrnuti broj unetom broju N.
(1234->4321).'''

def Obrni(N):
    NO = 0
    while N>0:
        c = N%10      #Izdvajamo poslednju cifru
        NO = NO*10 + c  #Dodajemo cifru
        N = N//10     #Ponistavamo poslednju cifru
    return NO
broj = int(input("Unesite broj: "))
ob = Obrni(broj)
print("Obrnuti broj je ", ob)

'''63.Napisati funkciju koja za neki trocifren broj odredjuje
proizvod prve dve cifre.Koristeci ovu funkciju,napisati program
Koji stampa sve trocifrene brojeve kod kojih je proizvod
prve dve cifre jednak 8.'''

def ProizvodPrve2(N):
    a = N//100     #cifra stotina
    b = N%100//10  #cifra desetica
    return a*b
for n in range(100, 1000):
    if ProizvodPrve2(n)==8:
        print(n)

'''64.Napisati funkciju koja ispisuje 10 najvecih trocifrenih
brojeva ciji je zbir cifara 20.'''

def Ispisi():
    br = 0
    n = 999
    while br<10:
        a = n//100
        b = n//10%10
        c = n%10
        if a+b+c==20:
            br = br + 1
            print(n)
        n = n - 1
Ispisi()

'''65.Napisati program,koji koristeci funkciju prost,
izracunava sumu svih dvocifrenih prostih brojeva.'''

'''1 nacin'''

def Prost(n):
    if n==1:
        return False
    for a in range(2, n):
        if n%a==0:
            return False
    return True

s = 0
for a in range(10, 100):
    if Prost(a):
        s = s + a
print("Suma prostih dvocifrenih je ", s)

'''2 nacin'''

import math
def Prost(n):
    if n==1:
        return False
    if n==2 or n==3:
        return True
    if n%2==0:
        return False
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
    for a in range(2, n):
        if n%a==0:
            return False
        return True
s = 0
for a in range(10, 100):
    if Prost(a):
        s = s + a
print("Suma prostih dvocifrenih je ", s)

'''66.Ispisati 100 prvih prirodnih brojeva ciji je zbir 
cifara 8.Zbir cifara realizovati kao funkciju.'''

def ZbirCifara(n):
    zc = 0         #Zbir cifara
    while n>0:
        zc = zc + n%10
        n = n//10
    return zc
n = 1
br = 0
while br<100:
    if ZbirCifara(n)==8:
        br = br + 1
        print("{}. {}".format(br,n))
    n = n + 1

'''67.Sa tastature se unosi n prirodnih brojeva.Sabrati sve
deljive sa 3.Deljivost sa 3 realizovati kao funkciju koja
vraca True ili False.'''

'''1 nacin'''
def Deljiv3(n):
    if n%3==0:
        return True
    else:
        return False
n = int(input("Koliko brojeva unosite n= "))
s = 0          #Promenljiva za zbir
for a in range(1, n+1):
    print("Unesite {}.broj".format(a),end=' ')
    x = int(input())
    if Deljiv3(x):       #Ako je broj x deljiv sa 3 dodaj ga na zbir
        s = s + x
print("Zbir deljivih sa 3 je", s)

'''2 nacin'''
def DivisibleBy3(n):
    return n % 3 == 0
    
n = int(input('How many numbers you enter? '))
sum = 0
list = []
for a in range(1, n + 1):
    print('Enter {}. number:'.format(a), end = ' ')
    num = int(input())
    if num % 3 == 0:
        sum = sum + num
        list.append(num)
DivisibleBy3(n)
if len(list) > 0:
    print(f'Sum of numbers divisible by 3 is {sum}.')
elif len(list) == 0:
    print('There are no numbers divisible by 3.')


'''68.Napisati funkciju koja vraca n-ti Fibonacijev broj.
Fibonacijevi brojevi su definisani kao
F(1)=1 F(2)=1 F(n)=F(n-1)+F(n-2)   1,1,2,3,5,8,13,21,34,55...'''

def Fib(n):
    f1 = 1
    f2 = 1
    if n==1 or n==2:
        return 1
    for a in range(n-2):
        f = f1 + f2
        f1 = f2
        f2 = f
        print(f2/f1)
    return f
n = int(input("Unesite broj n= "))
print("{}. Fibonacijev broj je {}".format(n,Fib(n)))


#ciklusi for
#range(<pocetak>, <kraj nije ukljucen>, <korak>)
#range(10) #skup vrednosti od 0 do 9
#range(1,11) #skup vrednosti od 1 do 10
#range(0,10,3) #skup vrednosti 0,3,6,9
#range(0,-10,-1) #skup vrednosti od 0,-1,...-9
#range(0)        #generise prazan skup vrednosti
#range(1,0)      #generise prazan skup vrednosti

#naredbe za prekid ponavljanja
 #break
 #continue

#for a in range(5, 101, 5):
    #print(a,end=' ')
#print("kraj")

'''69.Napisati program koji ispisuje sve brojeve od 1 do 20
i njihovu sumu.'''

zbir = 0
for a in range(1, 21):
    zbir = zbir + a      #novi zbir je stari zbir + a
    print(a)
print("Zbir je", zbir)

'''70.Napisati program koji ispisuje sve neparne brojeve od
1 do 100 i njihovu sumu.'''

suma = 0
for a in range(1, 100, 2):
    suma = suma + a
    print(a)
print("Zbir je", suma)
