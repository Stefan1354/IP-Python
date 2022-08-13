#1.Napishete programa v koqto potrebitelq vavejda tekst, 
#i na negova baza se sazdava rechnik. Za klucovete na recnika
#slujat simvolite ot teksta, a stoinostta na elementite
#se opredelq ot broq na saotvetnite simvoli v teksta.


text = input("Enter text: ")
d = dict()
for i in range(len(text)):
    if text[i] in d:
        d[text[i]]+=1
    else:
        d[text[i]]=1   
print(d)                                     #Enter text: Stefan
                                             #{'S': 1, 't': 1, 'e': 1, 'f': 1, 'a': 1, 'n': 1}

#2 nacin
text = (input("Enter text: "))
d = dict()
for i in text:
    d[i]=text.count(i)
print(d)


#3 nacin
string = input("Add string: ")
my_dict = dict()

for letter in string:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)                                           #Add string: dell
                                                         #{'d': 1, 'e':1, 'l':2}


#2.Napishete programa v koqto potrebitelq vavejda cqlo cislo.
#Ot nego se sazdava spisuk, sastoiasht se ot cislata ot 1 do
#tova cislo. Vaz osnova na tozi spisuk se sazdava rechnik
#v koito elementite ot spisuka sa klucove na elementite na
#recnika a stoinostite na tezi elementi na recnika sa 
#stoinostite na spisuka, no v obraten red.

num = int(input("Enter num: "))
l = list()
for i in range(num):
    l.append(i+1)
reversedlist = list(l)
reversedlist.reverse()
d = dict()
for i in range(num):
    d[l[i]]=reversedlist[i]
print(d)                                      #Enter num: 4
                                              #{1: 4, 2: 3, 3: 2, 4: 1}

'''2 nacin'''

num = int(input("Enter num: "))
keys = list(i for i in range(1,num+1))
my_dict = {}
for i in range(len(keys)):
    my_dict[keys[i]]=keys[len(keys)-i-1]
print(my_dict)
