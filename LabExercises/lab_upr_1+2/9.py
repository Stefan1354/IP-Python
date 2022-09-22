'''Da se sastavi programa, koqto vavezda n chisla ot 
klaviaturata i namira srednoaritmetichnata stoinost
(1<=n<=1000).'''

n = int(input("Enter n:"))
sum = 0
br = 0
for numbers in range(n):
    numbers = int(input("Enter numbers:"))
    if n>=1 and n<=1000:
        sum += numbers
        br += 1
print("Srednoaritmeticnata stoinost e ", sum/br)
