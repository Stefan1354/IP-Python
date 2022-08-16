#1.Napisete programa koqto namira liceto na geometricna figura
#kato purvo se vavezda vida na figurata.S opciqta 1 da se izbira
#kvadrat, s nomer 2 pravougulnik, s nomer 3 pravougulen 
#triugulnik, s nomer 4 lice na usporednik, s nomer 5 
#lice na romb.Za premsqtaneto na liceto, na otdelnite figuri,
#da se napisat pothodqsti funkcii.

figure=int(input("Izberete nomera na figurata "))

if figure==1:
    def __square__(a):
        return (a*a)
    a=int(input("Enter a "))
    print(__square__(a))
if figure==2:
    def __rectangle__(a,b):
        return (a*b)
    a=int(input("Enter a "))
    b=int(input("Enter b "))
    print(__rectangle__(a,b))
if figure==3:
    def __triangle__(a,b):
        return ((a*b)/2)
    a=int(input("Enter a "))
    b=int(input("Enter b "))
    print(__triangle__(a,b))
if figure==4:
    def __paralelogram__(a,h):
        return (a*h)
    a=int(input("Enter a "))
    h=int(input("Enter h "))
    print(__paralelogram__(a,h))
if figure==5:
    def __romb__(a,h):
        return (a*h)
    a=int(input("Enter a "))
    h=int(input("Enter h "))
    print(__romb__(a,h))
if figure>5:
    print("Greshka")

