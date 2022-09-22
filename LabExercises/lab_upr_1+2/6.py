#Da se sastavi programa, koqto izvezda slendiq model:

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

n = int(input("Enter n:"))
for i in range (1, n+1):
    print('*'*i)
for y in range(n-1, 0, -1):
    print('*'*y)
    
# second way

for i in range(1, 6):
    print('*'*i)
for y in range(4, 0, -1):
    print('*'*y)
