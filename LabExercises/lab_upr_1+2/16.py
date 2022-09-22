'''Da se sastavi programa, koqto vavejda n na broi chisla ot
klaviaturata i namira srednoaritmetichnata stoinost na 
vsicki chetni chisla i proizvedenieto na vsichki nechetni
chisla.'''

n = int(input("Enter n: "))
s = 0
br = 0
p = 1
for numbers in range(n):
    numbers = int(input("Enter numbers: "))
    if numbers %2==0:
        s += numbers
        br += 1
    else:
        p *= numbers
print("Srednoaritmeticnata stoinost na vsicki cetni cisla e", s/br)
print("Proizvedenieto na vsicki necetni cisla e", p)
