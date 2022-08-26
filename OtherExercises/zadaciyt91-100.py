'''91.Ispisati 20 najvecih trocifrenih brojeva ciji je zbir 
cifara 20.'''

# br=0     #koliko smo brojeva pronasli
# for n in range(999,99,-1):
#     a=n//100       #cifra stotina
#     b=n//10%10     #cifra desetica
#     c=n%10         #cifra jedinica
#     if a+b+c==20:
#         br=br+1
#         print(n)
#     if br==20:
#         break

'''92.Sa tastature se unosi n celih pozitivnih brojeva.Ispisati:
     a) Broj parnih i neparnih brojeva
     b) Aritmeticku sredinu parnih i neparnih
     v) Broj brojeva deljivih sa 3 i 5
     g) Proizvod brojeva deljivih sa 4.'''

#a)
# n=int(input("Koliko brojeva unosite "))
# brpar=0
# for a in range(n):
#     x=int(input("Unesite broj "))
#     if x%2==0:
#         brpar=brpar+1
# print("Broj parnih je ",brpar)
# print("Broj neparnih je ",n-brpar)

#b)
# n=int(input("Koliko brojeva unosite "))
# brpar=0
# spar=0
# snep=0
# for a in range(n):
#     x=int(input("Unesite broj "))
#     if x%2==0:
#         brpar=brpar+1
#         spar=spar+x
#     else:
#         snep=snep+x
# print("Aritmeticka sredina parnih je ",spar/brpar)
# print("Aritmeticka sredina neparnih je ",snep/(n-brpar))

#v)
# n=int(input("Koliko brojeva unosite "))
# br35=0
# for a in range(n):
#     x=int(input("Unesite broj "))
#     if x%3==0 and x%5==0:
#         br35=br35+1
# print(br35)

#g)
# n=int(input("Koliko brojeva unosite "))
# p4=1
# for a in range(n):
#     x=int(input("Unesite broj "))
#     if x%4==0:
#         p4=p4*x
# print(p4)

'''93.Data su 2 prirodna broja A i B.Ispisati njihov najveci
zajednicki delilac.'''

# a=int(input("Unesite 1.broj "))
# b=int(input("Unesite 2.broj "))
# manji=min(a,b)
# for delioc in range(manji,0,-1):
#      if a%delioc==0 and b%delioc==0:
#           print("Najveci zajednicki delioc je ",delioc)
#           break 

'''94.Racunar generise slucajan broj od 1 do 100. Pogodite broj
u najvise 10 pokusaja.'''

# import random
# zb=random.randint(1,100)     #zamisljeni broj
# pogodio=False
# for pok in range(1,11):
#      print("Pokusaj broj ",pok)
#      broj=int(input("Unesite broj "))
#      if zb<broj:
#           print("Zamisljeni broj je manji")
#      elif zb>broj:
#           print("Zamisljeni broj je veci")
#      else:
#           pogodio=True      #Pogodili smo
#           print("Pogodili ste u pokusaju broj",pok)
#           break
# if not pogodio:
#      print("Niste pogodili,zamisljeni broj je",zb)

#Naredba While

'''95.Napisati program koji ispisuje sve neparne brojeve od
1 do 100 i njihovu sumu.'''

# for koristimo kada znamo unapred broj ponavljanja
#while koristimo kada ne znamo unapred broj ponavljanja

# n=1
# suma=0              #sumu postavljamo na nulu
# while n<=100:       #radi sve dok je n<=100
#      suma=suma+n    #dodajemo na sumu broj n
#      print(n,suma)
#      n=n+2
# print("Suma je: ",suma)

#sada isti uslov zadatka samo za parne brojeve

# n=2
# suma=0
# while n<=100:
#      suma=suma+n
#      print(n,suma)
#      n=n+2
# print("Suma je ",suma)

'''96.Napisati program koji za dati pozitivan ceo broj N
ispisuje zbir svih brojeva od 1 do N.'''

# N=int(input("Unesite N "))
# suma=0
# a=1        #pocetna vrednost od koje sabiramo
# while a<=N:
#      suma=suma+a   #Dodajemo na sumu
#      print("Dodajem ",a," i suma do sada je ",suma)
#      a=a+1          #Uvecavamo a za 1
# print("Suma je ",suma)

#sada ispisujeo zbir od N do 1

# N=int(input("Unesite N "))
# suma=0
# while N>=1:
#      suma=suma+N    #Dodajemo N na zbir
#      N=N-1          #Smanjujemo N za 1
# print("Suma je",suma)

'''97.Napisati program koji ce stampati kvadrate i kvadratne korene
prvih n prirodnih brojeva.'''

# import math
# n=int(input("Unesite n= "))
# a=1
# while a<=n:       #Ponavljaj dok je a<=n
#      print(a,a*a,math.sqrt(a))
#      a=a+1

'''98.Napisati program koji izracunava N!.'''

# N=int(input("Unesite N "))
# fakt=1
# a=1
# while a<=N:
#      fakt=fakt*a
#      a=a+1
# print(N,"!=",fakt)

'''99.Za dati broj N (0<N<11) ispisati tablicu mnozenja brojem N.'''

# N=int(input("Unesite N "))
# print("Tablica mnozenja brojem ",N)
# a=0
# while a<=10:
#      print(a,"*",N,"=",a*N)
#      a=a+1

#malo da sredimo resenje naredbom .format

# N=int(input("Unesite N "))
# print("Tablica mnozenja brojem ",N)
# a=0
# while a<=10:
#      print("{}*{}={}".format(a,N,a*N))
#      a=a+1

'''100.Sa tastature se unosi n celih pozitivnih brojeva.
Ispisati sumu svih neparnih i najveci od tih brojeva.'''

# n=int(input("Unesite koliko brojeva unosite "))
# a=1
# sumaN=0
# Najv=0
# while a<=n:     #radi sve dok je a<=n, dok ne unesemo n brojeva
#      br=int(input("Unesite broj "))
#      if br%2==1:    #da li je broj neparan
#           sumaN=sumaN+br
#      if br>Najv:
#           Najv=br
#      a=a+1    #Uvecavamo a za sledecu iteraciju
# print("Suma neparnih je ",sumaN)
# print("Najveci je ", Najv)
