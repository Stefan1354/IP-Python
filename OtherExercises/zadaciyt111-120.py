'''111.Napisati program kojim se stampaju svi trocifreni brojevi
koji su deljivi brojem koji se dobija izbacivanjem srednje cifre.'''

n = 100    #prvi trocifreni broj
while n<1000:
    a = n//100   #cifra stotina
    c = n%10     #cifra jedinica
    if n%(a*10+c)==0:   #ako je trocifreni deljiv sa dvocifrenim
        print(n)
    n+=1    #sledeci broj

'''112.Ispisati sve trocifrene brojeve koji imaju svojstvo
ABC=A+B*B+C*C*C. (135=1+3*3+5*5*5)'''

n = 100
while n<=999:
    a = n//100    #cifra stotina
    b = n//10%10  #cifra desetica
    c = n%10      #cifra jedinica
    if n==a+b**2+c**3:
        print(n)
    n+=1

'''113.Ispisati sve trocifrene brojeve koji su deljivi sa 7
cije su cifre poredjane u rastucem poretku.'''

n = 100
while n<1000:
    a = n//100
    b = n//10%10
    c = n%10
    if n%7==0 and a<b and b<c:
        print(n)
    n+=1

'''114.Napisati program koji za dva uneta prirodna broja a i b
ispisuje njihov najveci zajednicki delilac.'''

a = int(input("Unesite 1.broj: "))
b = int(input("Unesite 2.broj: "))
if a<b:
    manji = b
else:
    manji = b
while manji>=1:
    if a%manji==0 and b%manji==0:
        print(manji)
        break
    manji-=1

#2.nacin (Euklidov algoritam)

a = int(input("Unesite 1.broj: "))
b = int(input("Unesite 2.broj: "))
while b!=0:
    a, b = b, a%b  #a dobija vrednost b, a b dobija vrednost a ostatak sa b
print(a)

'''115.Napisati program koji za unet prirodan broj N ispisuje
njegovu najvecu cifru i zbir cifara.'''

n = int(input("Unesite broj: "))
najveca = 0
zbir = 0
while n>0:
    c = n%10     #Uzimamo poslednju cifru
    n = n//10    #Odbacujemo poslednju cifru
    zbir+=c
    if c>najveca:
        najveca = c
print("Najveca cifra je", najveca)
print("Zbir cifara je", zbir)

'''116.Napisati program kojim se od datog broja N formira broj
od istih cifara ali u obrnutom poretku.'''
   #Na primer 123   321

n = int(input("Unesite broj: "))
obrnuti = 0
while n>0:
    c = n%10   #poslednja cifra
    n = n//10  #ponistavamo poslednju cifru
    obrnuti = obrnuti*10 + c
print(obrnuti)

#objasnjenje
#uneli smo broj 123
#obrnuti je 0
#123>0
#poslednja cifra 123%10=3
#novi broj je 123//10=12
#obrnuti je 0*10+3=3

#da li je 12>3, jeste
#izdvaja poslednju cifru od broja 12 - 2
#novi broj je 12/10=1
#obrnuti je 3*10+2=32

#da li je 1>0, jeste
#izdvaja cifru 1%10=1
#1//10=0
#obrnuti je 32*10+1=321

#da li je 0>0, nije
#ispisuje 321  

'''117.Napisati program kojim se prirodan broj N>=10 transformise
u broj u cijem su zapisu prva i poslednja cifra zamenile mesta.
(broj cifara nije poznat)'''

n = int(input("Unesite broj: "))
nk = n  #kopija broja n
br = 0  #broj cifara
while nk>0:
    br+=1
    nk//=10
prva = n//(10**(br-1))   #prva cifra
posl = n%10              #poslednja cifra
broj = n-prva*10**(br-1) + posl*10**(br-1) - posl+prva   #novi broj
print(broj)

'''118.Napisati program koji za uneti dan, mesec i godinu
ispisuje koji je to po redu dan u godini. (voditi racuna
da li je godina prestupna)'''

d, m, g = map(int, input("Unesite dan, mesec i godinu ").split('.'))
rbd = d
mesec = 1
while mesec<m:
    brd = 31
    if mesec==4 or mesec==6 or mesec==9 or mesec==11:
        brd = 30
    else:
        if mesec==2:
            if (g%4==0 and g%100!=0) or g%400==0:
                brd = 29
            else:
                brd = 28
    rbd+=brd
    mesec+=1
print(rbd)

'''119.Napisati program kojim se racuna kolicnik 2 prirodna broja
A i B na K decimala koristeci postupak rucnog deljenja.'''

a = int(input("Unesite deljenik: "))
b = int(input("Unesite delilac: "))
k = int(input("Unesite broj decimala: "))
print(a//b,end=".")
ost = a%b*10
while k>0:
    print(ost//b,end='')
    ost = ost%b*10
    k-=1

'''120.Napisati program koji za dati prirodni broj N ispisuje
da li je stepen broja 3.'''

n = int(input("Unesite broj: "))
while n%3==0:
    n//=3
if n==1:
    print("Jeste stepen broja 3")
else:
    print("Nije stepen broja 3")
