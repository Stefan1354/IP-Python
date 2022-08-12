'''21.Ispisati odnos 2 uneta broja bez koriscenja naredbe if.
"Veci je prvi", "Veci je drugi" ili "Isti su".'''

#a=int(input("Unesite prvi broj "))
#b=int(input("Unesite drugi broj "))
#rez=(a>b)*"Veci je prvi"+(a<b)*"Veci je drugi"+(a==b)*"Isti su"
#print(rez)

#Naredbe grananja
'''22.Za dati broj ispisati da li je neparan.'''

#n=int(input("Unesite broj "))
#if n%2==1:
    #print("Broj je neparan")

#2.nacin
#n=int(input("Unesite broj "))
#if n%2!=0:
    #print("Broj je neparan")

'''23.Za dati broj ispisati da li je paran ili neparan.'''

#n=int(input("Unesite broj "))
#if n%2==0:
    #print("Broj je paran")
#else:
    #print("Broj je neparan")

'''24.Za dati broj ispisati da li pozitivan, negativan ili nula.'''

#n=int(input("Unesite broj "))
#if n>0:
    #print("Broj je pozitivan")
#elif n<0:
    #print("Broj je negativan")
#else:
    #print("Broj je 0")

'''25.Data su 2 broja. Ispisati da li su isti ili razliciti.'''

#a=int(input("Unesi prvi broj "))
#b=int(input("Unesi drugi broj "))
#if a==b:
    #print("Brojevi su isti")
#else:
    #print("Brojevi su razliciti")

'''26.Data su 2 razlicita broja. Ispisati veci od njih.'''

#a=int(input("Unesite prvi broj "))
#b=int(input("Unesite drugi broj "))
#if a>b:
    #print(a)
#else:
    #print(b)

'''27.Data su 2 broja. Ispisati tekst "Veci je prvi",
"Veci je drugi" ili "Isti su".'''

#a=int(input("Unesite prvi broj "))
#b=int(input("Unesite drugi broj "))
#if a>b:
    #print("Veci je prvi")
#elif a<b:
    #print("Veci je drugi")
#else:
    #print("Isti su")

'''28.Data su 4 broja. Ispisati najveci.'''

#a=int(input("Unesite prvi broj "))
#b=int(input("Unesite drugi broj "))
#c=int(input("Unesite treci broj "))
#d=int(input("Unesite cetvrti broj "))
#najveci=a
#if b>najveci:
    #najveci=b
#if c>najveci:
    #najveci=c
#if d>najveci:
    #najveci=d
#print("Najveci je ", najveci)

'''29. Za dati prosek predmeta ucenika ispisati njegov uspeh.
Smatrati da nema nedovoljnih ucenika.'''

#prosek=float(input("Unesite prosek "))
#if prosek>2.00 and prosek<2.50:
    #print("Prosek je dovoljan")
#elif prosek>=2.50 and prosek<3.50:
    #print("Prosek je dobar")
#elif prosek>=3.50 and prosek<4.50:
    #print("Prosek je vrlo dobar")
#else:
    #print("Prosek je odlican")

'''30.Date su ocene ucenika iz 4 predmeta.Ispisati uspeh.'''

#ocena1=int(input("Unesi prvu ocenu "))
#ocena2=int(input("Unesi drugu ocenu "))
#ocena3=int(input("Unesi trecu ocenu "))
#ocena4=int(input("Unesi cetvrtu ocenu "))
#uspeh=(ocena1+ocena2+ocena3+ocena4)/4
#if ocena1==1 or ocena2==1 or ocena3==1 or ocena4==1:
    #print("Nedovoljan")
#elif uspeh>=2.00 and uspeh<2.50:
    #print("Dovoljan")
#elif uspeh>=2.50 and uspeh<3.50:
    #print("Dobar")
#elif uspeh>=3.50 and uspeh<4.50:
    #print("Vrlo dobar")
#else:
    #print("Odlican")

#2.nacin

#a=int(input("Unesi prvu ocenu "))
#b=int(input("Unesi drugu ocenu "))
#c=int(input("Unesi trecu ocenu "))
#d=int(input("Unesi cetvrtu ocenu "))
#if a==1 or b==1 or c==1 or d==1:
    #print("Nedovoljan")
#else:
    #pr=(a+b+c+d)/4
    #if pr>=4.5:
        #print("Odlican")
    #elif pr>=3.5:
        #print("Vrlo dobar")
    #elif pr>=2/5:
        #print("Dobar")
    #else:
        #print("Dovoljan")