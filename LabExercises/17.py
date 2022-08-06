'''Da se sastavi programa, koqto vavejda dve celi chisla i 
izvejda proizvedenieto im samo ako proizvedenieto e
po-golqmo ot 1000. V protiven sluchai da se izvede
tqhnata suma.'''

x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = x * y
b = x + y
if z>1000:
    print("Proizvedenieto e: ", z)
else:
    print("Sumata e: ",b)
