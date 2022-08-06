'''Da se sastavi programa, koqto vavezda n na broj chisla ot
klaviaturata i namira srednoaritmeticnata stoinost na 
vsicki cetni cisla i proizvedenieto na vsichki necetni
cisla.'''

n=int(input("Enter n:"))
s=0
br=0
p=1
for numbers in range(n):
    numbers=int(input("Enter numbers:"))
    if numbers %2==0:
        s+=numbers
        br+=1
    else:
        p*=numbers
print("Srednoaritmeticnata stoinost na vsicki cetni cisla e", s/br)
print("Proizvedenieto na vsicki necetni cisla e", p)