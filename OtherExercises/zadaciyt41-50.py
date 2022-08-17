'''41.Data su 2 datuma u obliku(d.m.g). Ispisati datum koji
je pre (stariji).'''

d1, m1, g1 = map(int,input("Unesi 1. datum: ").split('.'))
d2, m2, g2 = map(int,input("Unesi 2. datum: ").split('.'))
if g1<g2:
    print(d1,'.',m1,'.',g1)
elif g2<g1:
    print(d2, '.',m2,'.',g2)
else:
    if m1<m2:
       print(d1,'.',m1,'.',g1)
    elif m2<m1:
        print(d2,'.',m2,'.',g2)
    else:
        if d1<d2:
            print(d1,'.',m1,'.',g1)
        elif d2<d1:
            print(d2,'.',m2,'.',g2)
        else:
            print("Datumi su isti")

#2.nacin

d1,m1,g1 = map(int,input("Unesite 1. datum: ").split('.'))
d2,m2,g2 = map(int,input("Unesite 2.datum: ").split('.'))
  #15.02.2020
  #20200215=2020*10000+2*100+15

dat1 = g1*10000 + m1*100 + d1
dat2 = g2*10000 + m2*100 + d2
if dat1<dat2:
    print(d1,'.',m1,'.',g1)
elif dat2<dat1:
    print(d2,'.',m2,'.',g2)
else:
    print("Datumi su isti")

'''42.Dat je datum(dan,mesec,godina). Ispisati da li je ispravan
ili ne.'''

d, m, g = map(int,input("Unesite dan,mesec i godinu (d.m.g): ").split('.'))
if m<1 or m>12:
    print("Datum nije ispravan")
else:
    broj_dana = 31
    if m==4 or m==6 or m==9 or m==11:
        broj_dana=30
    elif m==2:
        if (g%4==0 and g%100!=0) or g%400==0:  #prestupna godina
            broj_dana=29
        else:
            broj_dana=28  #nije prestupna
    if d>0 and d<=broj_dana:
        print("Datum je ispravan")
    else:
        print("Datum nije ispravan")
        
'''43.Napisi program koji na osnovu dana i meseca i godine
rodjenja osobe odredjuje da li je ta osoba rodjena 16.marta
i ako jeste ispisati da, a u suprotnom ne. Mesec je zadat
rednim brojem.'''

dan = 2
mesec = 5
if dan==16 and mesec==3:
    print('da')
else:
    print('ne')

'''44.Svake godine se odrzavaju 4 grend slem turnira:otvoreno
prvenstvo Australije,Francuske,Engleske,SAD. Ako se znaju
pobednici proslogodisnjih turnira,napisi program koji 
proverava da li je Nadal i te godine uspeo da osvoji
otvoreno prvenstvo Franuske(ako jeste ispisati da,a u suprotnom ne).'''

aus = 'Djokovic'
fr = 'Nadal'
eng = 'Djokovic'
sad = 'Nadal'
if fr=='Nadal':
    print('da')
else:
    print('ne')

'''45.Leto traje od 20.juna do 22.septembra(pretpostavimo da su
u oba datuma ukljucena leto). Napisi program koji za uneti datum
ispisuje da li je tokom leta i ispisuje da tj. ne.'''

dan = int(input("Unesite dan: "))
mesec = int(input("Unesite mesec: "))
if mesec==7 or mesec==8 or (mesec==6 and dan>=20) or (mesec==9
and dan<=22):
    print('da')
else:
    print('ne')

'''46.Joca je kupio poklon za rodjendan mladjem bratu i
starijoj sestri. Napisi program koji proverava da li je
razlika u ceni ta dva poklona veca od 1000 dinara(tada Joca
treba da dokupi jos nesto, da se onaj ko je dobio jeftiniji
poklon ne bi osetio povredjenim). Ako je razlika mala, ispisati
u redu, a u suprotnom ispisati nije u redu.
Osiguraj da tvoj program radi i u slucaju kada je brat
dobio skuplji poklon i kada je sestra dobila skuplji poklon.'''

brat = int(input("Cena bratovljevog poklona je: "))
sestra = int(input("Cena sestrinog poklona je: "))
razlika = max(brat,sestra) - min(brat,sestra)
if razlika>1000:
    print('nije u redu')
else:
    print('u redu')

'''47.Na dopunsku nastavu iz matematike treba da idu ucenici
cija je prosecna ocena na prva tri kontrolna zadatka strogo
manja od 3. Napisi program koji ispisuje da ili ne u
zavisnosti od toga da li Djordje treba da ide na dopunsku,
ako su poznate njegove tri ocene iz matematike.'''

ocena1 =  int(input("Unesi prvu ocenu: "))
ocena2 = int(input("Unesi drugu ocenu: "))
ocena3 = int(input("Unesi trecu ocenu: "))
if (ocena1+ocena2+ocena3)/3 <3:
    print('da')
else:
    print('ne')

'''48.Svake goodine se odrzavaju 4 grend slem turnira:otvoreno
prvenstvo Australije, Francuske, Engleske i SAD. Ako se znaju
pobednici proslogodisnjih turnira,napisi program koji 
proverava da li je Novak Djokovic uspeo da osvoji sva 4
(ako jeste ispisati da,a u suprotnom ne).'''

aus = "Djokovic"
fr = "Nadal"
eng = "Djokovic"
sad = "Nadal"
if aus=='Djokovic' and fr=='Djokovic' and eng=='Djokovic' and sad=='Djokovic':  
    print('da')
else:
    print('ne')

#2.nacin
aus = "Djokovic"
fr = "Nadal"
eng = "Djokovic"
sad = "Nadal"
if aus==fr==eng==sad=="Djokovic":
    print('da')
else:
    print('ne')

#Funkcije

def IspisiPoruku(poruka):
    print(poruka)
#Glavni program
p = "Danas je lep dan."
IspisiPoruku(p)
print("Opet smo u glavnom programu")

def Zbir2Broja(a,b):
    return a+b
c = Zbir2Broja(4,5)
print(c)

def Zbir2Broja(a,b):
    return a+b
print(Zbir2Broja(4,5))

'''49.Napisati funkcije za izracunavanje obima i povrsine
kvadrata stranice a.'''

def Obim(a):
    return 4*a
def Povrsina(a):
    return a*a
stranica = int(input("Unesite stranicu kvadrata: "))
O = Obim(stranica)
P = Povrsina(stranica)
print("Obim je ", O, "Povrsina je ",  P)

#2.nacin
def Obim(a):
    return 4*a
def Povrsina(a):
    return a*a
stranica = int(input("Unesite stranicu kvadrata: "))
print("Obim je ",Obim (stranica)," Povrsina je", Povrsina(stranica))

'''50.Napisati funkcije za izracunavanje obima i povrsine
kruga poluprecnika r.'''

def Obim(r):
    return 2*r*3.14
def Povrsina(r):
    return r*r*3.14
r = float(input("Unesite poluprecnik kruga: "))
print("Obim je ", Obim (r))
print("Povrsina je {:.2f}".format(Povrsina(r)))   #Ispis na 2 decimale
