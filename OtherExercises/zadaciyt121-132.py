'''121.Napisati program koji za dati prirodni broj N ispisuje
prvi veci od N koji je deljiv sa 7.'''

n = int(input("Unesite broj: "))
n+=1
while n%7!=0:
    n+=1
print("Prvi veci deljiv sa 7 je", n)

'''122.Napisati program koji za dati prirodni broj N ispisuje
najblizi broj broju N koji je deljiv sa 7.'''

n = int(input("Unesite broj: "))
k = 0
while k<7:
    if (n+k)%7==0:
        print(n+k)
        break
    if (n-k)%7==0:
        print(n-k)
        break
    k+=1

'''123.Ispisati 20 najvecih trocifrenih brojeva ciji je zbir
cifara 20.'''

n = 999    #krecemo od 999
br = 0
while br<20:
    a = n//100       #cifra stotina
    b = n//10%10     #cifra desetica
    c = n%10         #cifra jedinica
    if a+b+c==20:
        br+=1
        print(n)
    n-=1

'''124.Napisati program koji za n unetih prirodnih brojeva ispisuje
onaj koji ima najveci proizvod cifara.'''

n = int(input("Koliko brojeva unosite? "))
maxpr = 0
maxbroj = 0
while n>0:
    x = int(input("Unesite broj: "))
    xk = x    #kopija broja x
    p = 1
    while xk>0:
        p = p*(xk%10)    #izdvajamo poslednju cifru i mnozimo sa prethodnim proizvodom
        xk = xk//10
    if p>maxpr:          #nasli smo novi broj sa najvecim proizvodom
        maxpr = p        #novi najveci proizvod
        maxbroj = x      #novi broj sa najvecim proizvodom
    n-=1        #sledeca iteracija
print("Broj sa najvecim proizvodom je", maxbroj)

'''125.Ispisati koliko se puta pojavljuje svaka cifra u broju n
(n manje od 50 cifara) koristeci maksimalno 2 promenljive.'''

n = int(input("Unesite broj n: "))
p = 0          #brojac pojavljivanja svake cifre broja n
while n>0:     #izdvajamo cifre broja n
    p = p+10**((n%10)*2)
    n = n//10
for n in range(10):
    print("Cifra {0} se pojavljuje {1} puta".format(n,p%100))
    p = p//100

#ako zelimo da nam pokazuje one cifre koje se pojavljaju (ne one koje su 0 puta)

n = int(input("Unesite broj n= "))
p = 0          #brojac pojavljivanja svake cifre broja n
while n>0:     #izdvajamo cifre broja n
     p = p+10**((n%10)*2)
     n = n//10
for n in range(10):
    if p%100>0:
     print("Cifra {0} se pojavljuje {1} puta".format(n,p%100))
    p = p//100

#drugi nacin ispisa (formatiranja)

n = int(input("Unesite broj n= "))
p = 0     #brojac pojavljivanja svake cifre broja n
while n>0:     #izdvajamo cifre broja n
     p = p+10**((n%10)*2)
     n = n//10
for n in range(10):
    if p%100>0:
        print(f"Cifra {n} se pojavljuje {p%100} puta")
    p = p//100

'''126. Ispisati koliko se puta pojavljuje svaka cifra u broju n
(n manji od 50 cifara) koristeci samo jednu promenljivu
u programu (bez nizova, bez funkcija, bez stringova).'''

n = int(input("Unesite broj: "))
while n%(10**50)>0:
    n = n+10**((n%10)*2+50)
    n = n-(n%(10**50))+(n%(10**50))//10
n = n//(10**50)*10+9
while n>=0:
    print(f"Cifra {9-n%10} se pojavljuje {(n//10)%100}")
    n = n//1000*10+(n%10-1)

#da nam ne ispisuje one cifre koje se ponavljaju 0 puta

n = int(input("Unesite broj: "))
while n%(10**50)>0:
     n = n+10**((n%10)*2+50)
     n = n-(n%(10**50))+(n%(10**50))//10
n = n//(10**50)*10+9
while n>=0:
     if (n//10)%100>0:
        print(f"Cifra {9-n%10} se pojavljuje {(n//10)%100}")
     n = n//1000*10+(n%10-1)


#Liste
#elementi liste se nalaze u uglastim zagradama

a = [1,4,8,3]
print(a)
b = []
print(b)
print(type(b))   #class 'list'
d = [0]*10
print(d)
print(type(d[1])) #class 'int'

a = [5,7,'Dragan',True,3.14]
print(type(a[2]))  #class 'str'
print(type(a[3]))  #class'bool'

a = [3,7,2,8,10]
print(a[0])  #3
print(a[1])  #7
print(a[-1]) #10
print(a[-2]) #8

a[3]=50
print(a)  #umesto 8 pise 50
#a[10]=5
#print(a) #indeks je van opsega elemenata liste
print(len(a)) #5

a = []
a.append('Ivana')
print(a)
a = a+[5]
print(a)
a = a+[3,7,5]
print(a)
a.extend([6,7,8])
print(a)

a = [3,7,5,2,1,9]
print(a[0:3]) #3,7,5
print(a[2:4]) #5,2
print(a[-1:-3]) #[]
print(a[-3:-1]) #2,1
print(a[:4])    #3,7,5,2
print(a[-1:])    #9
print(a[-1:-4:-1]) #9,1,2
print(a[::2])    #3,5,1
print(a[::-2])   #9,2,7
print(a[2:]) #5,2,1,9

b = a[::]
print(b)   #b ista lista kako a

a = [3,7,15,6,2,4]
for i in range(len(a)):
    print(a[i])  #ispisuje elemente liste jedan ispod drugog
a = [3,7,15,6,2,4]
for i in range(0, len(a), 2):
     print(a[i])  #stampa (3, 15, 2)

a = [3,7,15,6,2,4]
for i in range(1,len(a),2):
     print(a[i]) #stampa (7,6,4)


a = [3,7,15,6,2,4]
for el  in a:
    print(el)   #stampa sve elemente jedan ispod drugog

a = [3,7,15,6,2,4]
for el in a:
    if el%2==1:
        print(el) #stampa samo neparne - 3,7,15

a = [3,7,15,6,2,4]
for el in a:
    if el%2==0:
        print(el) #stampa samo parne - 6,2,4

#list comprehension
a = [3,7,15,6,2,4]
neparni = [el for el in a if el%2==1]
print(neparni)   #[3,7,15]
print(15 in a)   #True
print(20 in a)   #False

a = [3,7,2,15,6,8]
neparni = []
for el in a:
    if el%2==1:
        neparni.append(el)
print(neparni) #[3,7,15]

a = [3,7,2,15,6,8]
neparni = []
for el in a:
    if el%2==1:
        neparni = neparni+[el]
print(neparni)  #[3,7,15]

a = [3,7,2,15,6,8]
neparni = []
for el in a:
    if el%2==1:
        neparni = neparni+[el]
print(neparni)       #[3,7,15]
print(sum(neparni))  #25

a = [3,7,2,15,6,8]
neparni = []
for el in a:
    if el%2==1:
        neparni = neparni+[el]
print(neparni) #[3,7,15]
print(sum(neparni)/len(neparni))  #printira aritmeticku sredinu neparnih brojeva

a = [3,7,2,15,6,8]
neparni = []
for el in a:
    if el%2==1:
        neparni = neparni+[el]
print(neparni) #[3,7,15]
print("{:.2f}".format(sum(neparni)/len(neparni))) 

a = [3,7,15,24,64]
print(sum(a[:3])) #25 (3+7+15)

a = [1,3,20,100,6]
#a[-1]=300
#print(a) #[1,3,20,100,300]
a[2:]=[7,7]
print(a) #[1,3,7,7]
print(sum(a)) #18
print(len(a)) #4
a.extend([1]*4)
print(a) #[1,3,7,7,1,1,1,1]

a = [3,6,1,100,5,2]
print(min(a)) #1
print(max(a)) #100
print(max(a[1:3])) #6

b = [el for el in a if el%2==1]
print(b) #[3,1,5]
print(max(b)) #5

parni = [el for el in a if el%2==0]
print(parni) #[6,100,2]
print(min(parni)) #2
print(sum(parni)) #108


a = [3,1,5,6,75,2]
a.append(54)
print(a) #[3,1,5,6,75,2,54]
a.extend([7,14])
print(a) #[3,1,5,6,75,2,7,14]
print(a.count(3)) 
a.insert(2,44)
print(a) 
print(a.index(3)) 
print(a.index(5)) #2
print(a.index(75)) #4
a.sort()
print(a) 
a.reverse()
print(a) 

a = [2,7,3,17,5,5,1]
a.sort(reverse=True)
print(a) #[17,7,5,3,2,1]
a.remove(7)
print(a) #uklanja 7 iz listata
a.pop()
print(a) #uklanja poslednji element
a.pop(1)
print(a) #uklanja element na poziciji u zagradata
del a[2]
print(a) #brise element na poziciji 2
del a[:]
print(a) #brise celu listu

'''127.Kreirati listu od n elemenata koji se unose sa tastature.
Ispisati broj parnih, zbir parnih, aritmeticku sredinu
parnih elemenata liste.'''

lista = []
n = int(input("Unesite broj elemenata liste "))
for i in range(n):
    x = int(input("Unesite {}. element liste ".format(i+1)))
    lista.append(x)  #dodajemo element x u listu
brp = 0  #broj parnih
zbp = 0   #zbir parnih
for i in range(n):
    if lista[i]%2==0:
        brp+=1
        zbp+=lista[i]
print("Broj parnih je ",brp)
print("Zbir parnih je ",zbp)
print("Aritmeticka sredina parnih je ",zbp/brp)

#2.nacin

lista = []
n = int(input("Unesite broj elemenata liste: "))
for i in range(n):
    x = int(input("Unesite {}. element liste ".format(i+1)))
    lista.append(x)
brp = 0
zbp = 0
for el in lista:
    if el%2==0:
        brp+=1
        zbp+=el
print("Broj parnih je ",brp)
print("Zbir parnih je ",zbp)
print("Aritmeticka sredina parnih je ",zbp/brp)

#3.nacin

lista = []
n = int(input("Unesite broj elemenata liste: "))
for i in range(n):
    x = int(input("Unesite {}. element liste ".format(i+1)))
    lista.append(x)
parni = []
for el in lista:
    if el%2==0:
        parni.append(el)
print("Broj parnih je ", len(parni))
print("Zbir parnih je ", sum(parni))
print("Aritmeticka sredina parnih je ", sum(parni)/len(parni))

'''128.Uneti elemente liste sa tastature u jednom redu.Izbaciti
elemente liste na parnim pozicijama (sa parnim indeksima).
Ispisati broj elemenata i zbir novodobijene liste.'''

lista = list(map(int,input("Unesite elemente liste ").split()))    #elementi liste u jednom redu
parni_indeksi = []    #lista elemenata koje treba ukloniti
for i in range(len(lista)):
    if i%2==0:
        parni_indeksi.append(lista[i])  #dodajemo elemente u 2.listu koju treba ukloniti
for el in parni_indeksi:
    lista.remove(el)   #uklanja element el iz liste lista
#print(lista) #2 4 5 7 8    #stampa 4 i 7 jer su na parnoj poziciji
print("Broj elemenata liste je ", len(lista))    #2 6 4 1 99 5   stampa broj elemenata liste je 3
print("Zbir elemenata liste je ", sum(lista))                    #stampa zbir elemenata liste je 12

#2.nacin
lista = list(map(int,input("Unesite elemente liste ").split()))
lista = lista[1::2]
print(lista) #unesite elemente liste 2 4 6 5 7 8  stampa [4,5,8]
print("Broj elemenata liste je ",len(lista)) #stampa broj elemenata liste je 3
print("Zbir elemenata liste je ",sum(lista)) #stampa zbir elemenata liste je 17

'''129.Dat je prirodan broj n.Ispisati koliko puta se pojavljuje
svaka njegova cifra.'''

n = int(input("Unesite broj "))
cifre = [0]*10
while n>0:     #izdvajamo cifre broja n
    c = n%10     #poslednja cifra u broju
    cifre[c]+=1   #uvecavamo pojavljivanje cifre c
    n//=10     #ponistavamo poslednju cifru
#ispisujemo pojavljivanje cifara
for a in range(10):
    if cifre[a]>0:
        print("Cifra {} se pojavljuje {} puta".format(a,cifre[a]))

#2.nacin
n = int(input("Unesite broj: "))
cifre = []
while n>0:    #izdvajamo cifre broja n
    cifre.append(n%10)   #u listu cifre dodajemo poslednju cifru broja n
    n//=10    #ponistavamo poslednju cifru broja n
for a in range(10):
    print("Cifra {} se pojavljuje {} puta".format(a,cifre.count(a)))

#da nam ispisuje samo cifre koje se ponavljaju

n = int(input("Unesite broj: "))
cifre = []
while n>0:    #izdvajamo cifre broja n
   cifre.append(n%10)   #u listu cifre dodajemo poslednju cifru broja n
   n//=10    #ponistavamo poslednju cifru broja n
for a in range(10):
    if cifre.count(a)>0:
        print("Cifra {} se pojavljuje {} puta".format(a,cifre.count(a)))

'''130.Napisati program za izvlacenje brojeva u igri loto 7/39.'''

import random
kuglice = [a for a in range (1,40)]
izvucene = []        #izvucene kuglice (brojevi)
for i in range(7):   #izvlacimo 7 brojeva
    kuglica = random.choice(kuglice)   #izvlacimo kuglicu
    izvucene.append(kuglica)           #dodajemo kuglicu u listu izvucenih
    kuglice.remove(kuglica)            #uklanjamo kuglicu
izvucene.sort()
print(izvucene)

#2.nacin

import random
kuglice = [a for a in range(1,40)]
random.shuffle(kuglice)
izvucene = kuglice[:7]     #uzimamo prvih 7 brojeva iz liste kuglice
izvucene.sort()
print(izvucene)

'''131.Generisati listu slucajnih dvocifrenih brojeva od 20
elemenata.Zameniti elemente liste sa parom elemenata 
(broj,zbir,cifra).'''
   #Primer:      Lista=[21,54,19,...]
   #Nova lista:  Lista=[(21,3),(54,9),(19,10),...]

import random
lista = []
for i in range(20):
    lista.append(random.randint(10,99))
print(lista)
for i in range(20):
    n = lista[i]       #pamtimo element na poziciji i
    del lista[i]       #brisemo element na poziciji i
    lista.insert(i,(n,n//10+n%10))  #ubacujemo uredjeni par na poziciju i
print("Nova lista: ")
print(lista)
lista.sort(key=lambda x:x[0]) #lista uredjena u rastucem poretku
print(lista)

'''132.Data su 2 prirodna broja n i m.Ispisati "DA" ili "NE"
u zavisnosti da li se moze formirati broj m od cifara broja n.'''
   #primer:                    #primer:
   #1234567    541             #1234567   551
   #DA                         #NE

n, m = map(int,input('Unesite n i m ').split())
cifre = []      #kreiramo praznu listu
while n>0:      #sve dok imamo cifara u broju n
    c = n%10    #izdvajamo poslednju cifru
    n = n//10   #ponistavamo poslednju cifru
    cifre.append(c)
moze = True    #predpostavka da mozemo da formiramo broj
while m>0 and moze:
    c = m%10
    m = m//10
    if c in cifre:
        cifre.remove(c)    #uklanjamo cifru c iz liste cifre
    else:
        moze = False         #ne postoji cifra
if moze:
    print("DA")
else:
    print("NE")

#2.nacin

n, m = map(int,input('Unesite n i m ').split())
cifre = [0]*10
while n>0:
    c = n%10
    n = n//10
    cifre[c]+=1
moze = True
while m>0 and moze:
    c = m%10
    m = m//10
    if cifre[c]>0:
        cifre[c]-=1
    else:
        moze = False
if moze:
    print("DA")
else:
    print("NE")
