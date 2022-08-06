'''Da se sastavi programa, koqto vavezda ot klaviaturata
n chisla i sumira pootdelno vsichki cetni i necetni
cisla. Programata da izvezda obshtata suma
i za dvata sluchaja.'''

n=int(input("Enter n:"))
sum_prime=0
sum_notprime=0
for numbers in range (n):
    numbers=int(input("Enter numbers:"))
    if (numbers%2)==0:
        sum_prime+=numbers
    else:
        sum_notprime+=numbers
print("Sum of prime numbers is:", sum_prime)
print("Sum of not prime numbers is:", sum_notprime)