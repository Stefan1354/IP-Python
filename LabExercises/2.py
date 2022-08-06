'''Da se sastavi programa, koqto izcislqva sumata i 
proizvedenieto na vsichki chisla ot 1 do dadeno cislo n.'''

n=int(input("Enter n:"))
sum=0
p=1
for i in range(1,n+1):
    sum+=i
    p*=i
print("Sumata e ",sum)
print("Proizvedenieto e ",p)


