'''Da se sastavi programa, koqto vavejda n na broi chisla
ot klaviaturata i namira srednoaritmetichnoto samo na
onezi ot tqh, koito sa po-golemi ot predvaritelno
zadadenoto chislo k.'''

n = int(input("Enter n:"))
k = int(input("Enter k:"))
s = 0
br = 0
for numbers in range (n):
    numbers = int(input("Enter numbers: "))
    if numbers>k:
        s += numbers
        br += 1
print(s/br)
