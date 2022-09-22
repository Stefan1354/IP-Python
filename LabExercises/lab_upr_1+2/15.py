'''Da se sastavi programa, koqto vavejda n na broi chisla ot
klaviaturata i namira srednoaritmetichnoto samo na onezi ot
tqh, koito sa po-malki ot predvaritelno zadadenoto chislo u
i po-golemi ot predvaritelno zadadenoto chislo v(u>v).'''

n = int(input("Enter n: "))
u = int(input("Enter u: "))
v = int(input("Enter v: "))
s = 0
br = 0
for numbers in range(n):
    numbers = int(input("Enter numbers: "))
    if numbers<u and numbers>v:
        s += numbers
        br += 1
print(s/br)
