#1. Написати програм где корисник уноси време у секундама, а програм исписује време у данима, сатима, минутама и секундама 
#(нпр: 184.713 секунда = 2 дана, 3 сата, 18 минута и 33 секунде). 

sek = int(input("Unesi vreme u sekundama: "))
# potrebno je broj sekundi podeliti danima izraženim u sekundama
dan = sek//86400                      #jedan dan ima 24*60*60=86400 sekundi
# ostatak delјenja potrebno je podeliti satima izraženim u sekundama
sat = (sek%86400)//3600            #jedan sat ima 60*60=3600 sekundi 
# ostatak delјenja potrebno je podeliti minutima izraženim u sekundama
minut = ((sek%86400)%3600)//60  
# ostatak delјenja će predstavlјati broj sekundi
sekunda = ((sek%86400)%3600)%60
print("Dani: ",dan,"; Sati: ",sat,"; Minuti: ",minut,"; Sekunde: ",sekunda)

#2.Напишите програм који ће израчунати просечну (средњу) вредност бројева. Корисник на почетку уноси за колико бројева
# жели да израчуна средњу вредност, а затим уноси бројеве. Програм израчунава и приказује средњу вредност свих 
#унетих бројева.

#Srednja vrednost brojeva
n = int( input("Za koliko brojeva želite da se izračuna srednja vrednost? "))
# početna vrednost promenlјive koja će čuvati zbir brojeva je uvek 0
S = 0
br = 0
for brojac in range(n):
# pri svakom prolazu kroz petlјu korisnik unosi broj
    broj = int(input("Unesite broj: "))
# uneti broj dodaje se prethodnom zbiru
    S+=broj 
    br+=1
# po izlasku iz petlјe računa se srednja vrednost
SrednjaVrednost = S/br
print("Srednja vrednost iznosi: ", SrednjaVrednost)


#3.Написати програм који ће рачунати производ бројева које уноси корисник све док не унесе 0.

n = int(input("Unesi broj: "))
# početna vrednost promenlјive koja će čuvati proizvod brojeva je 1
P = 1
# čim se ispuni uslov izlazi se iz petlјe tj njeno telo se ne izvršava 
while n!=0: 
    P*=n
# od korisnika se zahteva da unese novi broj
    n = int(input("Unesi broj: "))
print("Proizvod unetih brojeva iznosi: ", P)

#4.Написати програм који исписује таблицу множења бројева од 1 до n. На почекту корисник уноси за колико бројева 
#исписује таблицу множења.

n = int(input("Za koliko brojeva se ispisuje tablica množenja? "))
for i in range(1, n+1):
    for j in range(1, n+1):
        print(i, "*", j, "=",i*j, end=" ", sep="")
        print()

#5.Написати програм који тражи просте бројеве од 2 до 10.

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'je jednako ', x, '*', n//x)
            break
    else:
    # ugnježdena petlja je prošla bez pronalaženja faktora
     print(n)


#6.Написати програм који ће штампати све бројеве од 1 до 10 са назнаком уколико је број дељив са три.

for num in range(1, 10):
    if num % 3 == 0:
        print("Broj deljiv sa 3 je ", num)
        continue    # prelazi se na sledeću iteraciju bez štampe u sledećem redu
    print("Broj je ", num)

#7.Написати програм којим корисник најпре уноси број редова и колона матрице, а затим је попуњава бројевима. 
#На крају програм штампа унету матрицу.

n = int(input("Unesite broj redova matrice "))
m = int(input("Unesite broj kolona matrice "))
a = []
for i in range(n):
   b = []
   for j in range(m):
      b.append(int(input("unesite elemente matrice: ")))
   a.append(b)
print(a)

#8.Написати програм који формира списак земаља тако што за сваку земљу у посебном реду напише њен назив и површину.
#У програму је дат речник који садржи називе неколико земаља и њихове површине.

 povrsine = {"Srbija": 88361,
            "Hrvatska": 56594,
            "Crna Gora": 13812,
            "Bosna i Hercegovina": 51197,
            "Slovenija": 20273,
            "Makedonija": 25713} 
for zemlja in povrsine:
       print("Naziv: ", zemlja, "Površina: ", povrsine[zemlja])

#9.Написати функцију која проналази најмањи број у унетој листи бројева.

def minimum (b):
    min = b[0];
    for i in range(len(b)):
        if b[i] < min:
            min = b[i]   #promenlјiva min uzima novu manju vrednost 
        else: 
          continue
    return min
moja_lista = [2, 5, 8, 3, 1, 4]
minimum_liste = minimum(moja_lista)
print("Minimalna vrednost unete liste brojeva je: ", minimum_liste)


#10.Написати програм који исцртава кружницу.
# Алгоритам:
# 1. Нацртати кратку линију (нпр. 2 корака)
# 2. Окренути се за 1 степен
# 3. Поновити претходне кораке 360 пута


import turtle
t = turtle.Turtle()
count = 0
while(count < 360):  
# koristi se while petlјa ali moguće je upotrebiti i for petlјu
    t.forward(2)
    t.left(1)
    count+=1

#11.За унети било који карактер преко тастатуре (слово, број, специјални знак) програм исписује његов ASCII/Unicode код.

a = input("Unesite znak: ")
b = ord("a")
print("Vas znak: ",a, "ima ASCII kod: ", b)

#12.Napisati program koji ce izracunati trosak u kupovini.Napraviti dvodimenzionalnu listu koja ce za svaku namirnicu
#sadrzati naziv namirnice i cenu - hleb(30) i jaja(14) i prikazati cenu hleba.Omoguciti korisniku da unese kolicinu hleba
#i jaja i te podatke smestiti u listu, izracunati trosak, prikazati celu listu i trosak.

namirnice = [["hleb",30],["jaja",14]]
namirnice[0].append(int(input("Unesite kolicinu hleba: ")))
namirnice[1].append(int(input("Unesite kolicinu jaja: ")))
print(namirnice)
trosak = namirnice[0][2]*namirnice[0][1]+namirnice[1][2]*namirnice[1][1]
print("Trosak: ", trosak)


'''13.Ispisati sve proste brojeve od 1 do 100.'''

def prosto (x):            # definisanje funkcije
    if (x==1):             # 1 nije prost broj
        return False       # povratak za 1 - nije prost broj
    for i in range(2, x):   # za sve od 2 do izabrano broja
        if (x%i == 0):     # djeljiv sa brojem i
            return False   # broj je djeljiv i nije prost
    return True            # nije djeljiv - nasao je prost broj
 
for p in range(1, 100):   # brojevi iz opsega    
    if prosto(p):          # poziv funkcije i provjera indikatora prost broj
        print(p)           #ispis broja



'''14.Učitati članove niza. Ispisati članove niza sa neparnim indeksom.'''

niz = list()
n = int(input("broj clanova liste: "))
for i in range(0, n):
    temp=int(input("clanovi liste: "))
    niz.append(temp)
 
for i in niz:
    print(i)
 
for i in range(0, n):
    if i%2!= 0:
        print("niz[",i,"] = " , niz[i])


'''15.Učitati članove niza. Izračunati i ispisati sumu članova niza sa parnim indeksom.'''

n = int(input("Enter n: "))
li = []
for i in range(0, n):
    num = int(input(f"Enter {i+1}.num "))
    li.append(num)

sum = 0
for i in range(0, n):
    if i%2!=0:
        sum+=li[i]
print("Suma clanova sa parnim indeksom je: ",sum)


'''16.Učitati članove niza. Izračunati i ispisati proizvod članova niza koji su djeljivi sa 2 (paran).'''

niz = list()
n = int(input("Unesite broj clanova niza: "))
for i in range(0,n):     # range(pocetak, kraj, korak) - pocetak i korak opcionalni i kraj nije ukljucen
    temp = int(input("Clanovi su "))  # privremena varijabla
    niz.append(temp)     # broj se dodaje na kraj niza
 
p = 1 # pocetna vrijednost proizvoda
for element in niz:
    if element % 2 == 0:
        p *= element
print ("Proizvod elemenata niza djeljivih sa 2 je ", p)
 
# II Varijanta
p = 1 # pocetna vrijednost proizvoda
for i in range(0,n):
    if niz[i] % 2 == 0:
        p *= niz[i]
print ("Proizvod elemenata niza djeljivih sa 2 =", p) 


'''17.Deklarirajte niz naziva niz i ograničite ga na 10 elemenata. Omogućite unos elemenata preko
tipkovnice. Ispišite neparne elemente niza.'''

niz = [0]*10
for i in range(0, 10):
    niz[i] = int(input("Unesite broj: "))

for i in range(0, 10, 2):
    print(niz[i])                               #Unesite broj: 1
                                                #Unesite broj: 2
                                                #Unesite broj: 3
                                                #Unesite broj: 4
                                                #Unesite broj: 5
                                                #Unesite broj: 6
                                                #Unesite broj: 7
                                                #Unesite broj: 8
                                                #Unesite broj: 9
                                                #Unesite broj: 10

                                                #1
                                                #3
                                                #5
                                                #7
                                                #9
 

#18.Написати програм којим се проверава да ли је број дељив са 7. Користити посебне функције за унос, обраду и штампу података.

def unos_podataka():
    broj = int(input("Unesi broj: "))
    return broj       #funkcija vraća broj koji je uneo korisnik
def obrada_podataka(br):     
    if br % 7 == 0:
           # deljivost sa 7
           return True        #funkcija vraća True ako je br delјiv sa 7
    else:
           return False       #funkcija vraća False ako br nije delјiv sa 7
def izlaz_podataka(broj, rezultat):   # procedura za štampu rezultata
    if rezultat:
        print("Broj {0} je deljiv sa 7".format(broj))
    else:
        print("Broj {0} nije deljiv sa 7".format(broj))


#19.Корисник уноси тежине девојчица и тежине дечака у једном одељењу. Направити листу тежина дечака и листу тежина
#девојчица, а затим израчунати број и просечну тежину свих ђака коришћењем функција и процедура.

def unos_decaka_i_devojcica():
    dev = int(input("Koliko devojčica ima u odeljenju? "))
    dec = int(input("Koliko dečaka ima u odeljenju? "))
    lista_dev = []
    lista_dec = []
    for brojac in range(dev):
        tez_dev = int(input("Unesi težinu {}. devojčice: ".format(brojac+1)))
        lista_dev.append(tez_dev)
    for brojac in range(dec):
        tez_dec = int(input("Unesi težinu {}. dečaka: ".format(brojac+1)))
        lista_dec.append(tez_dec)
    return lista_dec,  lista_dev
def prosek(lista1,lista2):
    zbir = sum(lista1)+sum(lista2)
    broj = len(lista1)+len(lista2)
    pros = zbir/broj
    print("Prosečna težina svih đaka iznosi: ", pros)
decaci, devojcice = unos_decaka_i_devojcica()
print("Ukupan broj učenika je: ", (len(decaci)+len(devojcice)))
prosek(decaci,devojcice)


#20.Написати програм који израчунава збир, разлику, производ и количник два броја, тј. симулира рад дигитрона 
#(коришћењем функција за израчунавање). На почетку корисник уноси бројеве, а затим бира жељену операцију.

def zbir(br1, br2):
    rezultat = br1 + br2
    return rezultat
def razlika(br1, br2):
    rezultat = br1 - br2
    return rezultat
def proizvod(br1, br2):
    rezultat = br1 * br2
    return rezultat
def kolicnik(br1, br2):
    rezultat = br1 / br2
    return rezultat
 

print("Pokrenuli ste kalkulator...")
print("Unesite brojeve i odaberite računsku operaciju")
prvi = int(input("Unesite prvi broj: "))
drugi = int(input("Unesite drugi broj: "))
print("Izaberite računsku operaciju: (1) Sabiranje, (2) Oduzimanje, (3) Proizvod, (4) Kolicnik")
izbor = input()
if izbor == "(1)":
    rezultat = zbir(prvi,drugi)
elif izbor == "(2)":
    rezultat = razlika(prvi,drugi)
elif izbor == "(3)":
    rezultat = proizvod(prvi,drugi)
elif izbor == "(4)":
    rezultat = round(kolicnik(prvi, drugi),2)
print("Rezultat je", rezultat)


#21.Написати функцију за превођење бинарног записа броја у декадни. У главном програму корисник уноси број у бинарном 
#запису, а програм позива написану функцију и исписује декадни запис броја, а затим се врши провера добијеног
#резултата позивом функције bin.

def bin_u_dek(bin):
       velicina = len(bin)
       potencija = 0
   #zadaje se početna vrednost stepena osnove 2
       broj = 0
   # postavlja se početna vrednost dekadnog broja
       for i in range (velicina-1, -1, -1):
   # i uzima vrednosti indeksa binarnog zapisa od poslednje cifre unazad do    
   # prve
            if int(bin[i])==1:
      #ispituje se da li je cifra na poziciji i binarnog zapisa broja jednaka 1
                broj = broj+2**potencija
            #ako jeste 1 računa se nova vrednost dekadnog broja
                potencija = potencija+1
      #svakako, vrednost stepena osnove 2 povećava se za 1
                return(broj)
   #funkcija vraća dekadnu vrednost unetog binarnog broja
 
binarni_broj = input("Unesite binarni broj: ")
dekadni_broj = bin_u_dek(binarni_broj)
print("broj u dekadnom zapisu iznosi:", dekadni_broj) 
provera = bin(dekadni_broj)
print("broj u binarnom zapisu iznosi:", provera)

#22.Написати програм који штампа збир два унета бинарна броја (бајта) у декадном запису. Користити функцију за 
#превођење бинарног записа броја у декадни.

def bin_u_dek(bin):
    velicina = len(bin)-1
    potencija = 0
    broj = 0
    for i in range (velicina, -1, -1):
        if int(bin[i])==1:
            broj = broj+2**potencija
        potencija = potencija+1
    return(broj)
binarni_broj1 = input("Unesite prvi binarni broj (kao bajt tj. 8 cifara): ")
while len(binarni_broj1)!=8:
    binarni_broj1 = input("Niste uneli dobar bajt, unesite ponovo: ")
binarni_broj2 = input("Unesite drugi binarni broj (kao bajt tj. 8 cifara): ")
while len(binarni_broj2)!=8:
    binarni_broj2 = input("Niste uneli dobar bajt, unesite ponovo: ")
zbir = bin_u_dek(binarni_broj1)+bin_u_dek(binarni_broj2)
print("Binarni brojevi u dekadnom zapisu iznose: ", bin_u_dek(binarni_broj1), bin_u_dek(binarni_broj2)) 
print("Njihov zbir iznosi: ", zbir) 
