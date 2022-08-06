'''Da se sastavi programa, koqto izvezda vsichki prosti chisla
v diapazona ot 25 do 50.'''

for i in range(25, 51):
    if i>0:
        for a in range(2, i):
            if i%a==0:
                break
        else:
            print(i)
