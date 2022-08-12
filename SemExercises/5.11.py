'''1.Napisete programa v koqto potrebitelq zapulva spisuk s chisla.
posle se suzdava vtori spisuk, koito se sastoi ot dva elementa:
stoinostta na nai-golemiq element v spisuka i indeksa na tozi element
v spisuka.'''

# li1=[]
# li1_size=int(input("Size: "))

# for n in range(li1_size):
#     num=int(input("Numbers "))
#     li1.append(num)

# li2=[]
# li2.append(max(li1))
# li2.append(li1.index(max(li1)))
# print(li2)

'''2.Napisete programa v koqto potrebitelqt trqbva da vavede 
tekstova stoinost.Na osnovata na teksta, se formira recnik.
Klucovete na recnika sa simvolite na tozi tekst, a stoinostta
na saotvetniq element predstavlqva izhoodniqt element s 
iztrit simvol, koito se qvqvat kluchut.Klucovete ne trqbva
da se povtarqt, ako ima povtarqshti se simvoli, te se 
propuskat.'''

#Na primer:
#Vhod: abesae
#Izhod 'a': "besae", 'b': "aesae", 'e':"absae",'s':"abeae"

# n=input("Enter text: ")
# text=dict()
# for i in n:
#     text[i]=n.replace(i, "",1)
# print(text)



'''3.Napisete programa v koqto na osnovata na tekst vaveden
ot potrebitelq, se sazdava kortez.Na osnovata na tozi kortez
se sazdava nov kortez, v nego se vklqcvat ravnootstoqshtite
elementi, zapochvayki ot purviq (s nulev indeks).Razstoqnieto
mezdu elementite se vavezda ot potrebitelq.'''

# text=input("Enter a string: ")
# step=int(input("Enter a num:"))
# tup=tuple(text)
# print(tup)
# new_tup=tuple()
# new_tup=tup[0:len(tup):step]
# print(new_tup)