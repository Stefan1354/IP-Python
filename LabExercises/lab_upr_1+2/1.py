'''Da se sastavi programa, koqto namira vsichki chisla,
v intervala [1,1000], koito zavarshat na 7.'''

brojac = 7
while brojac<1001:
    print(brojac)
    broja+=10

2. nacin

for i in range(1, 1000):
    if i%10==0:
        print(i-3)
