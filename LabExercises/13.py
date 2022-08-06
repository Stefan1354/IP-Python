'''Da se sastavi programa, koqto vavezda n na broj chisla
ot klaviaturatan i namira sumata samo na onezi ot tqh, 
koito sa po-malki ot predvaritelno zadadeno chislo u 
i po-golemi ot predvarielno zadadenoto chislo v.'''

n = int(input("Enter n: "))
u = int(input("Enter u: "))
v = int(input("Enter v: "))
s = 0
for numbers in range (n):
    numbers = int(input("Enter numbers:"))
    if numbers<u and numbers>v:
        s += numbers
print(s)
