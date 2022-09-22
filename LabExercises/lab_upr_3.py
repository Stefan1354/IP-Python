'''1.Da se sastavi programa, koqto vavejda n celi chisla,
i gi sumira.'''

n = int(input("Enter n: "))
sum = 0
for i in range(n):
    num = int(input("Enter num: "))
    sum = sum + num
print("Sumata e", sum)


'''2.Da se sastavi programa, koqto vavejda chislo n
i pechati triugulnik ot zvezdichki.'''

n = int(input("Enter n: "))
for i in range(1, n+1):
    print('*'*i)

'''3.Da se sastavi programa koqto proverqva da li
chisloto e prosto, koeto vavejda potrebitelq.'''

n = int(input("Enter n: "))
isPrime = False
if n<2:
    isPrime = False
else:
    for i in range(2, n):
        if n%i==0:
            isPrime = True
            break
if isPrime:
    print("NotPrime")
else:
     print("Prime")
