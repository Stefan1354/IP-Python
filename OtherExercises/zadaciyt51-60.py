'''51.Napisati funkciju koja vraca apsolutnu vrednost broja 
ne koristeci funkciju abs.'''

def AbsVr (a):
    if a<0:
        return -a
    else:
        return a
n = float(input("Unesite broj: "))
print("Apsolutna vrednost je ", AbsVr(n))

'''52.Napisati funkciju koja racuna aritmeticku sredinu 3 uneta broja.'''

def Prosek(a, b, c):
    return (a+b+c) / 3
prvi = int(input("Unesite prvi broj: "))
drugi = int(input("Unesite drugi broj: "))
treci = int(input("Unesite treci broj: "))
pr = Prosek(prvi, drugi, treci)
print("Aritmeticka sredina je ", pr)

'''53.Napisati funkciju koja vraca zbir i proizvod cifara
datog dvocifrenog broja.'''

def ZbirIProizvod(n):
    a = n//10        #cifra desetica
    b = n%10         #cifra jedinica
    return a+b, a*b
n = int(input("Unesite dvocifreni broj: "))
z, p = ZbirIProizvod(n)
print("Zbir cifara je {} Proizvod cifara je {}".format(z,p))

'''54.Napisati funkciju koja izracunava rastojanje izmedju 2
tacke zadate njihovim koordinatama.'''

import math
def Rast(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)
x1, y1 = map(int,input("Unesite koordinate 1.tacke: ").split(','))
x2, y2 = map(int,input("Unesite koordinate 2.tacke: ").split(','))
d = Rast(x1, y1, x2, y2)
print("Rastojanje je {:.2f}".format(d))

'''55.Napisati funkciju koja vraca zbir prvih N prirodnih brojeva.'''

def ZbirN(n):
    s = 0
    for a in range(1, n+1):
        s = s + a             #dodaje 1+2+3+...+n
    return s
n = int(input("Unesite broj n= "))
z = ZbirN(n)
print("Zbir brojeva od 1 do {} je {}".format(n,z))

#2.nacin
def ZbirN(n):
    s = 0
    a = 1
    while (a<=n):
        s = s + a
        a = a + 1
    return s
n = int(input("Unesite broj n= "))
z = ZbirN(n)
print("Zbir brojeva od 1 do {} je {}".format(n,z))


'''56. Napisati funkciju koja racuna faktorijal broja n.'''
   #n!=1*2*3*...*n

def Faktor(n):
    p = 1
    for a in range(1, n+1):
        p = p * a
    return p
n = int(input("Unesite n: "))
f = Faktor(n)
print("{}!={}".format(n,f))

'''57.Napisati funkciju koja ispisuje sve trocifrene brojeve
deljive sa 7 ciji je zbir cifara 15.'''

def Ispisi():
    for n in range(100, 1000):
        a = n//100       #cifra stotina
        b = n//10%10     #cifra desetica
        c = n%10         #cifra jedinica
        if n%7==0 and (a+b+c)==15:
            print(n)
Ispisi()

#2.nacin
def Ispisi():
    #100
    #999
    for a in range(1, 10):          #cifra stotina (od 1 do 9)
        for b in range(0, 10):      #cifra desetica(od 0 do 9)
            for c in range(0, 10):  #cifra jedinica(od 0 do 9)
                n = a*100 + b*10 + c
                if n%7==0 and a+b+c==15:
                    print(n)
Ispisi()

'''58.Napisati funkciju koja za dva uneta prirodna broja A i B
(A<B) vraca koliko ima brojeva izmedju A i B deljivih
sa 5 ili sa 7.'''

def Deljivi57(A, B):
    br = 0
    for n in range(A, B+1):
        if n%5==0 or n%7==0:
            br = br + 1
    return br
a, b = map(int,input("Unesite A i B ").split())
broj = Deljivi57(a,b)
print("Broj deljivih sa 5 ili sa 7 je ", broj)

'''59. Napisati funkciju koja ispisuje sve delioce prirodnog
broja N i vraca njihovu sumu.'''

def Delioci(N):
    zbir = 0      #Zbir delioca
    for a in range(1, N+1):
        if N%a==0:
           print(a)
           zbir = zbir + a
    return zbir
n = int(input("Unesite broj N= "))
print("Zbir delioca je ", Delioci(n))


'''60.Napisati funkciju koja ispisuje sve trocifrene brojeve
koji su deljivi sa 7 i cije su cifre poredjane u rastucem
poretku.'''

def Ispisi():
    for n in range(100, 1000):
        a = n//100
        b = n//10%10
        c = n%10
        if n%7==0 and a<b and b<c:
            print(n)
Ispisi()
