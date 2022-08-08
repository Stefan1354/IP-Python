'''1.Da se sastavi programa, koqto izcislqva stipendiqta
na studenti. Studenta trqbva da vavede svoq uspeh i maks. stipendiq
v tozi universitet.
Ako studenta ima uspeh >=5.50 polucava maks. stip.
Ako studenta ima uspeh >=5.00 i <5.50 poluchava 70% ot maks. stip.
Ako studenta ima uspeh >=4.50 i <5.00 poluchava 50% ot maks. stip.
Ako studenta ima uspeh pod 4.50 ne poluchava stipendiq.'''

n=float(input("Vavedi uspeh: "))
Max=int(input("Maksimalnata stipendiq na universiteta e: "))
if n>=5.50:
    print("Studentut poluchava Max stipendiq", Max)
elif n>=5.00 and n<5.50:
    print("Poluchava 70% ot Max stipendiq", Max*0.7)
elif n>=4.50 and n<5.00:
    print("Poluchava 50% ot stipendiq", Max*0.5)
else:
    print("Nqma stipendiq, slab uspeh")


'''2.Napishete programa, koqto izcislqva liceto S i obikolkata P
na geom.figura, kato purvo se izbira vida na figurata:
kvadrat, pravougulnik, pravougulen triugulnik, sled koeto
vavejdate stoinosti za stranite na figurata.'''

vid=input("figura: ")
P = 0
S = 0
if   vid=="kvadrat":
       a=int(input("strana: "))
       S = a*a
       P = 4*a
       print("Liceto e:", S)
       print("Obikolkata e:", P)
elif vid=="pravougulnik":
       a=int(input("strana: "))
       b=int(input("strana: "))
       S = a*b
       P = 2*a+2*b
       print("Liceto e:", S)
       print("Obikolkata e:", P)
elif vid=="pravougulen triugulnik":
       a=int(input("strana: "))
       b=int(input("strana: "))
       c=int(input("strana: "))
       S=a*b/2
       P=a+b+c
       print("Liceto e:", S)
       print("Obikolkata e:", P)
else:
    print("Greshna figura")

  
'''3.Napishete programa, koqto namira srednoaritmetichnoto
na chislata, koito se delqt na 3 v intervala ot 7 do 70.'''

sum = 0
count = 0
for i in range(7, 71):
    if i%3==0:
        sum += i
        count += 1
print(sum/count)

'''4.Napishete programa, koqto po vavedeno ot potrebitelq chislo opredelq:
Cifrata na edinicite deli li se na 5, a cifrata na deseticite
chetno chislo li e.'''

n = int(input("Enter n: "))
if (n%10)%5==0:
    print("Cifrata na edinicite se deli na 5")
if ((n%100)//10)%2==0:
    print("Cifrata na deseticite e chetno cislo")
else:
    print("Cifrata na deseticite ne e chetno cislo")    

'''5.Napishete programa, koqto po zadaden broi dni(n)
izvejda koi den ot sedmicata shte bude. Dneshniqt den
i broqt na dnite se vavejdat ot potrebitelq. Da se
izvede na ekrana n-tiq den sled dneshniq koi den
ot sedmicata e. Broeneto na dnite zapochva ot edno t.e.
1-ponedelnik,...,7-nedelq.'''

 #primeren vhod: 1  3
 #primeren izhod: cetvurtuk

this_day = int(input("this day: "))
searched_day = int(input("searched day: "))
sum = searched_day + this_day
if sum>7:
    sum -= 7

if sum==1:
    print("ponedelnik")
elif sum==2:
    print("vtornik")
elif sum==3:
    print("sreda")
elif sum==4:
    print("cetvurtuk")
elif sum==5:
    print("petuk")
elif sum==6:
    print("subota")
elif sum==7:
    print("nedelq")
