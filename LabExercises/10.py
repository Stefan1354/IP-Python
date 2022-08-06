'''Da se sastavi programa, koqto vavejda n chisla(n<=10) 
na broi realni chisla po-malki ot 1000 i namira
tqhnoto proizvedenie.'''

n = int(input("Enter n: "))
p = 1
if n<=10:
    for numbers in range (n):
        numbers = int(input("Enter numbers: "))
        if numbers<1000:
            p *= numbers
print("Proizvedenieto e", p)
