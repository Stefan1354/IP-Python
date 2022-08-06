'''Da se sastavi programa, koqto vavezda dve celi chisla i 
izvezda proizvedenieto im samo ako proizvedenieto e
po-golqmo ot 1000. V protiven slucai da se izvede
tqhnata suma.'''

x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = x * y
b = x + y
if z>1000:
    print("Proizvedenieto e: ", z)
else:
    print("Sumata e: ",b)
