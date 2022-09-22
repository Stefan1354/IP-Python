'''Da se sastavi programa, koqto vavejda n na broi chisla
ot klaviaturata i namira sumata samo na onezi ot tqh, 
koito sa otricatelni.'''

n = int(input("Enter n "))
sum = 0
for numbers in range(n):
    numbers = int(input("Enter numbers "))
    if numbers<0:
        sum = sum + numbers
print("Sumata na otricatelnite e", sum)
