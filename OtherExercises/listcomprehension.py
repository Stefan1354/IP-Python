fruits=['apple','banana','cherry','kiwi','mango']
newlist=[]

for x in fruits:
    if 'a' in x:
        newlist.append(x)
print(newlist) #printira onia dumi kade ima a

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[x for x in fruits if 'a' in x]
print(newlist) #printira onia dumi kade ima a - vtor nacin

newlist=[x for x in fruits if x!='apple'] #printira onia dumi kade ima a - tret nacin

newlist=[x for x in fruits]
print(newlist) #printira site elementi u listata

newlist=[x for x in range (10)]
print(newlist) #0,1,2,3,4,5,6,7,8,9

newlist=[x for x in range(10) if x<5]
print(newlist) #0,1,2,3,4

newlist=[x.upper() for x in fruits]
print(newlist) #printira listata s golemi slova

newlist=['hello' for x in fruits]
print(newlist) #printira hello tolko puti, kolko ima elementa u listata

newlist=[x if x!='banana' else 'orange' for x in fruits]
print(newlist) #umesto banana printira orange

thislist=['orange','mango','kiwi','pineapple','banana']
thislist.sort()
print(thislist) #printira po azbucan red

thislist=[100,50,65,82,23]
thislist.sort()
print(thislist) #ispisue od najmalecak do najgolem

thislist=['orange','mango','kiwi','pineapple','banana']
thislist.sort(reverse=True)
print(thislist) #printira po azbucan red ali nazad

thislist=[100,50,65,82,23]
thislist.sort(reverse=True)
print(thislist) #printira 100,82,65,50,23

def myfunc(n):
    return abs(n-50)
thislist=[100,50,65,82,23]
thislist.sort(key=myfunc)
print(thislist) #printira 50,65,23,82,100, printira broevete koj e najblizu do 50 i na dalje

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) #printira prvo s golemi bukvi, pa tegaj s malenki

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) #printira po azbucan red

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) #printira ozad napred

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist) #apple,banana,cherry

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist) #apple,banana,cherry

