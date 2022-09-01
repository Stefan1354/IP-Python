#1.Милица купује патике. Допала су јој се три пара. Напиши програм који исписује цене та три пара патика од
#најјефтинијих до најскупљих.
'''
prvi_par=int(input("Unesite cenu prvog para patika "))
drugi_par=int(input("Unesite cenu drugog para patika "))
treci_par=int(input("Unesite cenu treceg para patika "))

def sortiraj3(a,b,c):
    if (a>b):
        (a,b)=(b,a)
    if (a>c):
        (a,c)=(c,a)
    if (b>c):
        (b,c)=(c,b)
    return (a,b,c)
(prvi_par, drugi_par, treci_par)=sortiraj3(prvi_par, drugi_par, treci_par)
print(prvi_par, drugi_par, treci_par, sep="\n")'''

#2.Napisati program koji ispisuje prosek na kontrolnom, bez najlosije dobijene ocene.

#ocene=[int(input("Unesite prvu ocenu ")), int(input("Unesite drugu ocenu ")), int(input("Unesite trecu ocenu ")), 
#int(input("Unesite cetvrtu ocenu ")), int(input("Unesite petu ocenu "))]
#ocene=sorted(ocene)
#prosek_bez_najlosije=(ocene[1]+ocene[2]+ocene[3]+ocene[4])/4
#print(format(prosek_bez_najlosije, '.2f'))

#3.Бројевна права је трима различитим тачкама a, b и c подељена на четири дела. Написати програм који одређује у ком
#делу, првом, другом, трећем или четвртом, се налази унета (четврта) тачка x, различита од тачака a, b и c.

'''def sortiraj3(a,b,c):
    if a>b:
        (a,b)=(b,a)
    if a>c:
        (a,c)=(c,a)
    if b>c:
        (b,c)=(c,b)
    return (a,b,c)

a=float(input("Unesite tacku a "))
b=float(input("Unesite tacku b "))
c=float(input("Unesite tacku c "))
x=float(input("Unesite tacku x "))
(a,b,c)=sortiraj3(a,b,c)
if x<a:
    print(1)
elif x<b:
    print(2)
elif x<c:
    print(3)
else:
    print(4)'''


#4.Од цифара четвороцифреног природнog броја треба формирати најмањи троцифрен број.

'''def sortiraj4(a,b,c,d):
    if a>b:
        (a,b)=(b,a)
    if a>c:
        (a,c)=(c,a)
    if a>d:
        (a,d)=(d,a)
    if b>c:
        (b,c)=(c,b)
    if b>d:
        (b,d)=(d,b)
    if c>d:
        (c,d)=(d,c)
    return (a,b,c,d)

def trocifreni_broj(a,b,c):
    return 100*a+10*b+c

broj=int(input("Unesite broj "))
c0=broj%10
c1=broj//10%10
c2=broj//100%10
c3=broj//1000
(c0, c1, c2, c3) = sortiraj4(c0, c1, c2, c3)
if c0!=0:
    x=trocifreni_broj(c0, c1, c2)
elif c1!=0:
    x=trocifreni_broj(c1, c0, c2)
elif c2!=0:
    x=trocifreni_broj(c2, c0, c1)
else:
    x=trocifreni_broj(c3, c0, c1)
print(x)'''

#5.У рачунарству се често користе тзв. октални бројеви - бројеви записани у основи 8, коришћењем само цифара
#од 0 до 7. Напиши програм који врши конверзију четвороцифрених окталних бројева у декадне вредности и
#обратно.

'''def iz_oktalnog(c3, c2, c1, c0):
    return c3*8*8*8 + c2*8*8 + c1*8 + c0

def u_oktalni(n):
    c0=(n//(1))%8
    c1=(n//(8))%8
    c2=(n//(8*8))%8
    c3=(n//(8*8*8))%8
    return (c3, c2, c1, c0)

c3=int(input("Unesi prvi broj "))
c2=int(input("Unesi drugi broj "))
c1=int(input("Unesi treci broj "))
c0=int(input("Unesi cetvrti broj "))
print(iz_oktalnog(c3, c2, c1, c0))

n=int(input("Unesi n "))
(c3, c2, c1, c0)=u_oktalni(n)
print(c3, c2, c1, c0, sep='')'''


#6.Наставница жели да оцене својих ученика препише у дневник, али је приметила да се редослед ученика у
#свесци и дневнику не поклапа. Напиши програм који исписује све оцене у жељеном редоследу.

'''def prosek(ocene):
    return sum(ocene) / len(ocene)
broj_ucenika = int(input("Unesite broj ucenika "))
ocene = []
for i in range(broj_ucenika):
    ocene.append(list(map(int, input().split())))
for i in range(broj_ucenika):
    rbr = int(input("Unesite redni broj ucenika "))
for ocena in ocene[rbr-1]:
    print(ocena, end=" ")
print(format(prosek(ocene[rbr-1]), '.2f'))'''

#7. Написати програм који за дати природан број n проверава да ли је тај број Армстронгов. k-то цифрен број
#је Армстронгов ако је једнак суми k-тих степена својих цифара. На пример, 370 је Армстронгов јер је
#370 = 33 + 73 + 03
#1634 је Армстронгов јер је 1634 = 14 + 64 + 34 + 44
#док 12 није Армстронгов јер је
#12 ̸= 12 + 22

'''
def broj_cifara(n):
    broj = 0
    while True:
        broj = broj + 1
        n = n // 10
        if n == 0:
            break
    return broj
# funkcija izracunava zbir k-tih stepena cifara broja n
def zbir_ktih_stepena_cifara(n, k):
    zbir = 0
    while True:
        zbir = zbir + (n % 10) ** k
        n = n // 10
        if n == 0:
            break
    return zbir
# funkcija proverava da li je dati broj Armstrongov tj. ako broj ima k
# cifara, da li mu je zbir k-tih stepena cifara jednak njemu samom
def armstrongov(n):
    return zbir_ktih_stepena_cifara(n, broj_cifara(n)) == n
# ucitavamo broj i proveravamo da li je Armstrongov
n = int(input("Unesite broj "))
if armstrongov(n):
    print("DA")
else:
    print("NE") '''


#8.Оцена на испиту одређује се на основу броја освојених поена (може се освојити између 0 и 100 поена). Сви
#студенти који су добили мање од 51 поен аутоматски падају испит и добијају оцену 5. Оцена 6 се добија за
#број поена већи или једнак од 51, а мањи од 61, оцена 7 за број поена већи или једнак од 61, а мањи од 71,
#оцена 8 за број поена већи или једнак од 71, а мањи од 81, оцена 9 за број поена већи или једнак од 81 а мањи
#од 91, а оцена 10 за број поена већи или једнак од 91. '''


'''num_of_points=int(input("Enter number of points: "))
if num_of_points < 51:
    print("FAILED")
elif num_of_points in range(51, 61):
    print("GRADE IS 6 ")
elif num_of_points in range(61,71):
    print("GRADE IS 7")
elif num_of_points in range(71,81):
    print("GRADE IS 8")
elif num_of_points in range(81,91):
    print("GRADE IS 9")
elif num_of_points in range(91,101):
    print("GRADE IS 10")
else:
    print("WRONG INPUT")'''



#9.Познате су температуре за сваки дан неког периода. Написати програм којим се одређује редни број дана у
#том периоду када је температура први пут била негтивна.'''

'''n = int(input('Enter number: '))
day = -1
lst = []
for t in range(n):
    temp = int(input(f'Enter {t + 1}. temperature: '))
    lst.append(temp)
    if temp < 0:
        day = t
        break
print(day + 1)'''


#10.Написати програм којим се одређује број и збир цифара декадног записа природног броја.


def func(num):
    return num

num = input("Enter number: ")
sum = 0
for i in num:
    sum += int(i)
print(f'{len(num)} , {sum}') 
func(num)

