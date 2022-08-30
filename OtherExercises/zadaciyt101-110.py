'''101.Sa tastature se unosi n celih pozitivnih brojeva.Ispisati
aritmeticku sredinu svih brojeva koji su deljivi sa 3.
(voditi racuna ako nema nijedan deljiv sa 3).'''

# n=int(input("Koliko brojeva unosite "))
# a=1     #ciklicna promenljiva
# s=0     #suma deljivih sa 3 
# br=0    #brojac deljivih sa 3
# while a<=n:
#     broj=int(input("Unesite broj "))
#     if broj%3==0:    #ako je deljiv sa 3
#         s=s+broj     #dodajemo broj na sumu
#         br=br+1      #uvecavamo brojac
#     a=a+1
# if br>0:     #ima deljivih sa 3
#     ars=s/br
#     print("Aritmeticka sredine je ", ars)
# else:
#     print("Nema deljivih sa 3 ")   

'''102.Ispisati sve neparne dvocifrene brojeve ciji je zbir
cifara 10.'''

# n=10
# while n<=99:     #radimo sve dok su dvocifreni brojevi, moze i n<100
#     a=n//10      #cifra desetica
#     b=n%10       #cifra jedinica
#     if n%2==1 and a+b==10:     #uslov neparan i dvocifren
#         print(n)
#     n=n+1        #sledeca iteracija od 10 do 99

#2.nacin

# n=11
# while n<=99:
#     a=n//10
#     b=n%10
#     if a+b==10:
#         print(n)
#     n=n+2

'''103.Napisati program koji racuna zbir brojeva od 1 do 100
cija je zadnja cifra 9.'''

# n=1
# s=0            #zbir brojeva
# while n<=100:
#     if n%10==9:     #ako je zadnja cifra 9
#         s=s+n
#         print(s,n)
#     n=n+1      #sledeca iteracija
# print("Zbir je ",s)

#2.nacin

# n=9
# s=0
# while n<100:
#     s=s+n
#     print(n,s)
#     n=n+10
# print("Zbir je ",s)

'''104.Napisati program za izracunavanje n-tog stepena celog
broja a.'''

# a=int(input("Unesite a "))
# n=int(input("Unesite n "))
# stepen=1
# i=1
# while i<=n:
#     stepen=stepen*a
#     i=i+1
# print("Rezultat je ",stepen)

'''105.Napisati program kojim se odredjuje broj jedinica u
binarnom zapisu prirodnog broja n.'''

#n=3  11  2      15  1111   4

# n=int(input("Unesite broj "))
# br=0
# while n>0:
#     if n%2==1:
#         br=br+1
#     n=n//2
# print("Broj jedinica je ",br)

'''106.Napisati program koji ispisuje da li je prirodni broj 
N>1 prost.
Broj je prost ako je deljiv samo sa 1 i samim sobom.'''

# n=int(input("Unesite broj "))
# brdel=0
# a=1
# while a<=n:     #idemo od 1 do n i brojimo delioce
#     if n%a==0:  #ako je n deljivo sa a
#         brdel=brdel+1
#     a=a+1       #proveravamo sledeci delilac
# if brdel>2:
#     print("Broj nije prost")
# else:
#     print("Broj je prost")

'''107.Dat je prirodan broj N.Ispisati sve njegove delioce i
njihovu sumu.'''

# n=int(input("Unesite broj n="))
# suma=0
# delioc=1
# while delioc<=n:   #radi sve dok je delioc manji ili jednak od n
#     if n%delioc==0:  #da li je n deljivo sa delioc
#         print(delioc)
#         suma=suma+delioc   #dodaj na sumu
#     delioc=delioc+1    #sledeci broj
# print("Suma delioca je",suma)

'''108.Napisati ostatak pri deljenju A sa B (A i B su prirodni brojevi)
bez koriscenja DIV i MOD.
DIV-celobrojno deljenje  MOD-ostatak pri deljenju.'''

# a=int(input("Unesite 1.broj "))
# b=int(input("Unesite 2.broj "))
# while a>=b:    #radi sve dok je a>=b
#     a=a-b
# print("Ostatak pri deljenju je ",a)

'''109.Napisati program kojim se dati prirodni broj N rastavlja
na proste faktore.'''
#Na primer, za 28 racunar ce stempati 2 2 7  (28=2*2*7)

# n=int(input("Unesite broj "))
# a=2
# while a<=n:
#     if n%a==0:
#         print(a)
#         n=n//a
#     else:
#         a=a+1
# print("Kraj")

'''110.Napisati program koji ispisuje vrednost funkcije
y=(3-sqrt(4-x))/(2-x) na intervalu -5 do 5 sa korakom 0.5
uz kontrolu definisanosti funkcije.'''

# import math
# x=-5
# while x<=5:
#     if x==2 or x>4:    #funkcija nije definisana
#         print(x,"funkcija nije definisana")
#     else:
#         y=(3-math.sqrt(4-x))/(2-x)
#         print(x,y)
#     x=x+0.5
