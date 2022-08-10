'''1.Za 2 uneta cela broja ispisati celobrojni kolicnik i ostatak
pri deljenju (divmod funkcija).'''

a = int(input("Unesite 1.broj "))
b = int(input("Unesite 2.broj "))
div = a//b #celobrojni kolicnik
mod = a%b #ostatak pri deljenju
print("Celobrojni kolicnik je {}, a ostatak je {}".format(div,mod))

'''2.Date su stranice pravougaonika a i b. Ispisati O, P, D pravougaonika.'''

import math
a = int(input("Unesite stranicu a "))
b = int(input("Unesi stranicu b "))
O = 2*a+2*b
P = a*b
d = math.sqrt(a*a+b*b)
print("Obim je" , O)
print("Povrsina je", P)
print("Dijagonala je", d)

'''3.Napisati program za izracunavanje obima i povrsine kruga
poluprecnika r.'''

import math
r = int(input("Unesi r "))
O = 2*r*math.pi
P = r*r*math.pi
print("Obim je", O)
print("Povrsina je", P)

'''4.Data su 3 pozitivna broja a,b i c.Proveriti da li to mogu 
biti stranice trougla i ako mogu ispisati O i P trougla.'''

import math
a = int(input("Enter a "))
b = int(input("Enter b "))
c = int(input("Enter c "))
if a+b>c and a+c>b and b+c>a:
    s = a+b+c/2  #poluobim
    O = a+b+c
    P = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Obim je", O)
    print("Povrsina je", P)
else:
    print("Ne mogu biti stranice trougla")

'''5.Napisati program za izracunavanje povrsine, zapremine
i dijagonale kocke ivice a.'''

import math
a = int(input("Enter a "))
P = 6*a*a
V = a*a*a
d = a*math.sqrt(3)
print("Povrsina je", P)
print("Zapremina je", V)
print("Dijagonala je", d)

'''6.Date su ocene iz 3 predmeta. Ispisati prosek na 2 decimale.'''

geo = int(input("Unesite 1.ocenu "))
ist = int(input("Unesite 2.ocenu "))
fiz = int(input("Unesite 3.ocenu "))
prosek = (geo+ist+fiz)/3
print("Prosek je {:.2f}".format(prosek))

#2.nacin:
import math
geo = int(input("Unesite 1.ocenu "))
ist = int(input("Unesite 2.ocenu "))
fiz = int(input("Unesite 3.ocenu "))
prosek = (geo+ist+fiz)/3
print("Prosek je",round(prosek,2))

'''7.Dat je dvocifren broj.Ispisati zbir cifara, obrnuti broj
i najvecu cifru.'''

#primer   N=37
          #AB   (A-cifra desetica i B-cifra jedinica)

N = int(input("Unesite dvocifreni broj "))
A = N//10
B = N%10
Z = A+B
OB = B*10+A
NAJC = max(A,B)
print("Zbir je", Z)
print("Obrnuti broj je", OB)
print("Najveca cifra je", NAJC)

'''8. Dat je trocifren broj.Ispisati zbir cifara, obrnuti
broj i najmanju cifru.'''

#primer   N=156
           #ABC
    
N = int(input("Unesite troifreni broj "))
A = N//100  #cifra stotina
B = N//10%10  #cifra desetica
C = N%10      #cifra jedinica
Z = A+B+C
OB = C*100+B*10+A
NAJMANJA = min(A,B,C)
print("Zbir cifara je", Z)
print("Obrnuti broj je", OB)
print("Najmanja cifra je", NAJMANJA)

'''9.Dat je cetvorocifreni broj.Ispisati zbir cifara,obrnuti
broj i najmanju cifru.'''

#primer N=2345
#         ABCD

N = int(input("Unesite cetvorocifreni broj "))
A = N//1000
B = N//100%10
C = N//10%10
D = N%10
Z = A+B+C+D
OB = D*1000+C*100+B*10+A
NAJMANJA = min(A,B,C,D)
print("Zbir cifara je", Z)
print("Obrnuti broj je", OB)
print("Najmanja cifra je", NAJMANJA)

'''10.Ispisati broj koji se dobija kada se prirodnom broju N
izbaci cifra desetica.'''

N = int(input("Unesite broj "))
#2345   23*10+5
pc = N%10 #poslednja cifra
novi = N//100*10+pc #ponistimo poslednje dve cifre pa 
pomnozimo sa 10 i dodamo pc
print(novi)
