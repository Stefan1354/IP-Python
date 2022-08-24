'''71.Napisati program koji za dati pozitivan ceo broj N
ispisuje zbir svih brojeva od 1 do N.'''

#N=int(input("Unesite N= "))
#suma=0
#for a in range(1,N+1):
    #suma=suma+a
#print("Zbir brojeva od 1 do {} je {}".format(N,suma))

'''72.Napisati program koji ce stampati kvadrate i kvadratne
korene prvih n prirodnih brojeva.'''

#import math
#n=int(input("Unesite do kojeg broja zelite "))
#for a in range(1,n+1):
    #print(a,a*a,math.sqrt(a))

'''73.Napisati program koji izracunava N!.'''

#N=int(input("Unesite N "))
#f=1        #rezultat
#for a in range(1,N+1):
    #f=f*a
#print("{}!={}.".format(N,f))

'''74.Za dati broj N(0<N<11) ispisati tablicu mnozenja 
#brojem N.'''

#N=int(input("Unesite broj N= "))
#print("Tablica mnozenja brojem",N)
#for a in range(11):
    #print(a,'*',N,'=',a*N)

'''75.Ispisati sve dvocifrene brojeve koji su deljivi
sa 3 i sa 7.'''

#for a in range(10,100):
    #if a%3==0 and a%7==0:
        #print(a)

'''76.Ispisati sve trocifrene brojeve deljive sa 5 i sa 7 i
koliko ih ima.'''
#br=0
#for a in range(100,1000):
    #if a%5==0 and a%7==0:
        #br=br+1
        #print(a)
#print("Ima ih",br)

'''77.Ispisati sve cetvorocifrene brojeve kojima je zbir
cifara 12, a proizvod veci od 40.'''
 #N=1234
 #ABCD

#for n in range(1000,10000):
    #A=n//1000     #cifra hiljada 
    #B=n//100%10   #cifra stotina
    #C=n//10%10    #cifra desetica
    #D=n%10        #cifra jedinica
    #if A+B+C+D==12 and A*B*C*D>40:
        #print(n)

'''78.Sa tastature se unosi n celih pozitivnih brojeva.Ispisati
sumu svih neparnih i najveci od tih brojeva.'''

#n=int(input("Koliko brojeva unosite "))
#sumaNep=0
#Najveci=0
#for a in range(1,n+1):
    #x=int(input("Unesite broj "))
    #if x%2==1:
        #sumaNep=sumaNep+x
    #if x>Najveci:
        #Najveci=x
#print("Suma neparnih je ",sumaNep)
#print("Najveci broj je ",Najveci)

'''79.Sa tastature se unosi n celih pozitivnih brojeva.
Ispisati aritmeticku sredinu svih brojeva koji su 
deljivi sa 3. (voditi racuna ako nema nijedan deljiv sa 3).'''

#n=int(input("Unesite koliko brojeva unosite "))
#s=0         #zbir deljivih sa 3
#br=0        #broj deljivih sa 3
#for a in range(n):
    #x=int(input("Unesite broj "))
    #if x%3==0:
        #s=s+x      #dodajemo broj na sumu
        #br=br+1    #uvecavamo brojac deljivih sa 3
#if br==0:      #nema deljivih sa 3
        #print("Nema deljivih sa 3")
#else:          
      #ars=s/br           #aritmeticka sredina deljivih sa 3
      #print("Aritmeticka sredina je ",ars)

'''80.Ispisati sve neparne dvocifrene brojeve ciji je
zbir cifara 10.'''

#for n in range(10,99):
    #a=n//10       #cifra desetica
    #b=n%10        #cifra jedinica
    #if n%2==1 and a+b==10:
        #print(n)
        