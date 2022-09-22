'''Da se sastavi programa, koqto vavejda ot klaviaturata
n chisla i sumira pootdelno vsichki chetni i nechetni
chisla. Programata da izvezda obshtata suma
i za dvata sluchaq.'''

n = int(input("Enter n: "))
sum_even = 0
sum_odd = 0
for numbers in range (n):
    numbers = int(input("Enter numbers: "))
    if (numbers%2)==0:
        sum_even+=numbers
    else:
        sum_odd+=numbers
print("Sum of even numbers is:", sum_even)
print("Sum of odd numbers is:", sum_odd)
