'''
Da se sastavi programa, koqto vavezhda n na broj chisla ot
klaviaturata i namira sumata samo na onezi ot tqh, koito
sa po golemi ot predvaritelno zadadeno chislo k.
'''

n = int(input("Enter n: "))
k = int(input("Enter k: "))
s = 0
for numbers in range(n):
    numbers = int(input("Enter n: "))
    if numbers>k:
        s += numbers
print("Sumata e", s)

#2 sluchai kogato chislata sa po malenki od chisloto k

n = int(input("Enter n: "))
k = int(input("Enter k "))
s = 0
for numbers in range(n):
    numbers = int(input("Enter n: "))
    s += numbers
if numbers>k:
    print(s)
else:
    print("Vsicki cisla sa po malenki od cisloto k")
