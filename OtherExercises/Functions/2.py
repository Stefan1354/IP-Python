#2.Съставете програма с функция, която получава като аргумент числов списък и
#връща като резултат друг списък, 
#в който са включени само четните числа от списъка аргумент.

def cetni(l):
    new_list = []
    for i in range (len(l)):
        if l[i]%2==0:
            new_list.append(l[i])
    return new_list

n = int(input("Enter n: "))
nums=[]
for i in range(n):
    num = int(input(f"Please enter number {i+1}: "))
    nums.append(num)
print(cetni(nums))
