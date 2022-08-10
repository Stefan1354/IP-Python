#kortezi=tuples
#operacii pri kortezi
k=(7,5,3,6,1)
print(k[0]) #7
print(k[2:3]) #(3,)
print(7 in k) #True
print(k*3) #(7,5,3,6,1,7,5,3,6,1,7,5,3,6,1)
tup=k+(2,4) #(7,5,3,6,1,2,4)
print(tup)

tup=(7,5,3,6,1)
print(tup.index(1)) #na koe mqsto se namira nomer 1   #4
print(tup.count(5)) #kolko pati se povtarq 5          #1

for i in tup:
    print(i, end="")   #75361

d=dict()
d1=dict(name="Ivan", last_name="Petrov")
d3=dict([("name", "Polina"), ("l_name", "Koleva")])
print(d3) #{'name': 'Polina', 'l_name':'Koleva'}
print(d1) #{'name': 'Ivan', 'last_name': 'Ivanov'}

d={}
d["name"]="Petar"
d["l_name"]="Kolev"
d={"name": "Ivan", "last_name":"Ivanov"}
print(d) #{'name': 'Ivan', 'last_name': 'Ivanov', 's_name': 'Petrov'}

d={"name": "Ivan","last_name":"Ivanov"}
d["name"]
print(d[f'name'])  #KeyError: 'fname'

b="fname" in d
print(b) #False

len(d)
print(len(d)) #3  (do zarezo e 1)

d["s_name"]="Petrov"
print(d) #{'name': 'Ivan', 'last_name': 'Ivanov', 's_name': 'Petrov'}

keys=list(d.keys())
keys.sort()
for key in keys:
    print("{0}=>{1} .format(key,d[key]), end=")
s=set([1,2,3,1])
print(s) #{1,2,3}
s2=set("hello")
for i in s2:
    print(i,end="") 
print(len(s2))

s=set([1,2,3])
s1=set([4,2,6])
s3=s|s1
print(s3) #{1,2,3,4,6}

s=set([1,2,3,4])
s1=set([2,4,6])
s2=s-s1
print(s2) #{1,3}
s3=s1-s
print(s3) #{6}

s=set([1,2,3,4])
s1=set([2,4,6])
s4=s&s1
print(s4) #{2,4}

s=set([1,2,3,4])
s1=set([2,4,6])
s5=s^s1
print(s5) #{1,3,6}

s1=set([2,4,6])
s1.add(8)
s1.remove(2)
print(s1) #{8,4,6}