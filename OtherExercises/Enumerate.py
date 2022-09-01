'''values=["a", "b", "c"]
for value in values:
    print(value)      #a
                      #b
                      #c

index=0
for value in values:
    print(index, value)
    index+=1            #0 a 
                        #1 b
                        #2 c

for index in range(len(values)):
    value=values[index]
    print(index, value) #0 a
                        #1 b
                        #2 c

for count, value in enumerate(values):
    print(count, value) #0 a
                        #1 b
                        #2 c'''

# When you use enumerate(), the function gives you back two loop variables:
#   1. The count of the current iteration
#   2. The value of the item at the current iteration


# Когато използвате enumerate(), функцията ви връща две променливи на цикъла:
# 1. Броят на текущата итерация
# 2. Стойността на елемента при текущата итерация

'''for count, value in enumerate(values, start=1):
    print(count, value)   #1 a
                          #2 b
                          #3 c'''

users=["Test User", "Real User 1", "Real User 2"]
for index, user in enumerate(users):
    if index==0:
        print("Extra verbose output for: ",user)
    print(user)
#Extra verbose output for: Test User
#Test User 1
#Real User 2

def even_items(alphabet):
    '''Return items from ''iterable'' when their index is even.'''
    values=[]
    for index, value in enumerate(alphabet, start=1):
        if not index%2:
            values.append(value)
    return values
alphabet="abcdefghijklmnopqrstuvwxyz"
print(even_items(alphabet))
# ['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v', 'x', 'z']

def even_items(alphabet):
    return [v for i, v in enumerate(alphabet, start=1) if not i%2]
alphabet="abcdefghijklmnopqrstuvwxyz"
print(even_items(alphabet))
# ['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v', 'x', 'z']

def even_items(seq):
    return [v for i, v in enumerate(seq, start=1) if not i%2]
seq=list(range(1,11))
print(seq)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(even_items(seq))
#[2, 4, 6, 8, 10]

alphabet='abcdefghijklmnopqrstuvwxyz'
print(list(alphabet[1::2]))
# ['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v', 'x', 'z']

def even_items(alphabet):
    return [v for i, v in enumerate(alphabet, start=1) if not i%2]
def alphabet():
    alpha="abcdefghijklmnopqrstuvwxyz"
    for a in alpha:
        yield a
print(even_items(alphabet()))
# ['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v', 'x', 'z']