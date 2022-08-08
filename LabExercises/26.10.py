import random
s=[1,3,5,7]
s[1]=11 #na pozicija 1 pise umesto 3 11
print(s)

s=list()
s1=list("Python")
print(s1)

s=[]
s.append(5)
s.append(10)
s.append(20) #dodava elementi
print(s)

s=[2,4,6,8]
print(s[0])

s=[1,2,3,4,5,6]
print(s[::-1]) #pise elementite u obrnut redosled
print(s[:-1]) #printira bez poslednjio element
print(s[1:]) #printira bez prvio element
print(s[0:2]) #printira prvite dva elementa
print(s[-1:]) #printira poslednjio element

s=[1,2,3,4,5,6]
for i in s:
    print(i, end="") #stampa u edin red

s=[1,2,3,4,5,6]
for i in range (len(s)):
    print(s[i], end="")

s=[2,4,6,8,2]
print(s.count(2)) #kolko puti go ima brojo u listata
print(s.index(2)) #prva pozicija na koja e brojo
print(min(s))
print(max(s))

s.insert(0,90) #dodava element ispred drugite u listata 
print(s)

s.pop(0)
print(s)

s=[2,4,6,8,2]
random.shuffle(s)
print(s)
s.reverse() #stampa u obrnut redosled
print(s)

s=[45,50,60,70]
s.sort #od najmalecak do najgolem
print(s)

s1=["s", "T", "a", "F"]
s1.sort(key=str.lower) #prvo golemi slova pa tegaj malenki
s1.sort()
print(s1)

tup=tuple([10,20,30])
print(tup)

tup1=tuple("python")
print(tup1)
tup2=tuple()
print(tup2)  #prazen kortez


'''1.Da se napise programa v koqto potrebitelq vavezda cqlo chislo,
a programata formira dva korteza sastoiashti se ot cifrite
vlizashti v tova chislo.Ediniat s cifrite na cislata v prav red,
i vtori v koito cifrite sa v obraten red.'''

# tup1=()
# n1=int(input("Enter n:"))
# for i in range(1, n1+1):
#     tup1+=(i,)
#     tup2=sorted(tup1, reverse=True)
# print(tup1)
# print(tup2)

'''2.Napisete programa v koqto se sazdava cislov spisuk.
Toi se zapulva s slucaini chisla.Sled tova mezdu svaka
dvojka elementi ot tozi spisuk se vm'kva nov element
raven na sumata na stoinostite ot prehodnite dva.'''

# import random
# random.seed()
# list=[random.randint(10,20) for i in range (16)]
# print(list)

# for i in range(0,22,3):
#     list.insert(i+2, list[i]+list[i+1])
# print(list)





