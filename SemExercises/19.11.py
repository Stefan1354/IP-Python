#1.Напишете програма, в която се създава  функция. 
#Функцията получава като аргумент числов списък  и 
#връща като резултат друг списък, в който са включени 
#само нечетните числа от списъка аргумент.

#def necetni(_list):
    #NewList=[]
    #for i in range (len(_list)):
        #if _list[i]%2!=0:
            #NewList.append(_list[i])
    #return NewList

#n=int(input("Enter n "))
#nums=[]
#for i in range(n):
    #num=int(input(f"Please enter number {i+1}: "))
    #nums.append(num)
#print(necetni(nums))

#2.Напишете функция, която проверява дали два стринга 
#въведени от потребителя са анаграма.Функцията получава 
#като аргументи два стринга,връща като резултат 1 ако са 
#анаграма и 0 ако не са.

    #Примерен вход: "coast "    "stoak "           
    #Изход : The strings aren't anagrams.        
     
    #Примерен вход: "stop "    "post " 
    #Изход : The strings are anagrams.

#word_1=input("String 1: ")
#word_2=input("String 2: ")

#def is_anagrama(str1,str2):
    #s1=sorted(list(str1))
    #s2=sorted(list(str2))

    #return int(s1==s2)

#print(is_anagrama(word_1, word_2))


#3.Напишете програма,в която е описана функция,връщаща 
#като резултат второто по големина число в списъка, 
#предаден като аргумент на функцията.

'''def second_highest(input_list):
    input_list.sort()
    return input_list[len(input_list)-2]

n = int(input("n = "))
l = []

for i in range(n):
    l.append(int(input(f"l[{i}] = ")))

print(f"{second_highest(l)} is the second highest number in the list")'''

#2 nacin

'''def second_highest(input_list):
    input_list.sort()
    return input_list[-2]  

n = int(input("n = "))
l = []

for i in range(n):
    l.append(int(input(f"l[{i}] = ")))

print(f"{second_highest(l)} is the second highest number in the list.")'''


#4.Напишете програма , в която се създава функция с два 
#аргумента, които са числови списъци. Резултатът от
#функцията е число, равно на сумата от двойките 
#произведения на елементите на списъците. Ако в един от 
#списъците елементите са по-малко от другия, то 
#недостигащите елементи се получават посредством циклично
#повторение на съдържанието на списъка.

#def sum_two_lists(list1, list2):
    #sum = 0
    #list1_len = len(list1)
    #list2_len = len(list2)
    #count = 0

    #if list1_len >= list2_len:
        #for i in range(list1_len):
            #if count > list2_len-1:
                #count = 0
            #sum += list1[i] + list2[count]
            #count += 1

    #else:
        #list3 = list1
        #list1 = list2
        #list2 = list3
        #sum_two_lists(list1, list2)
    #return sum

#n = int(input("n1 = "))
#l1 = []
#for i in range(n):
    #l1.append(int(input(f"l1[{i}] = ")))

#n = int(input("n2 = "))
#l2 = []
#for i in range(n):
    #l2.append(int(input(f"l2[{i}] = ")))

#print(f"The sum of the two lists is {sum_two_lists(l1,l2)}")


#5.Напишете програма, която включва две функции. Първата функция
#създава матрица с числа и я запълва със стойности, 
#приема като аргумент броя редове и броя колони на
#матрицата , връща като резултат запълнената матрица.  
#Втората функция получава като аргумент матрицата и я 
#принтира под формата на таблица.

#Примерен вход:  row= 2
                #column= 4

#изход:          1 3 5 7
                #9 2 6 8


# import random

# def column_sum(matrix):
#     column_len = len(matrix[0])
#     for i in range(column_len):
#         sum = 0
#         for j in range(len(matrix)):
#             sum += matrix[j][i]
#         print(f"sum of column {i+1} = {sum}")



# def matrix_print(matrix):
#     for i in range(len(matrix)):
#         print(matrix[i])
#     column_sum(matrix)

# def matrix_fill(row, column):
#     l = []
#     c = []
#     for i in range(row):
#         for j in range(column):
#             c.append(random.randint(1,9))
#         l.append(c)
#         c = []
#     return l

# row = int(input("row = "))
# column = int(input("column = "))
# print(matrix_print(matrix_fill(row, column)))


'''2 nacin'''

# import random
# def make_matrix(rows, cols):
#     return [[random.randint(0, 10) for j in range(cols)] for i in range(rows)]


# def print_matrix(matr):
#     for i in matr:
#         for j in i:
#             print(j, end=" ")
#         print()


# def print_sum_cols(matr):
#     for i in range(len(matr[0])):
#         sum = 0
#         for j in range(len(matr)):
#             sum += matr[j][i]
#         print(sum)


# rows = int(input("Rows: "))
# cols = int(input("Cols: "))

# new_matrix = make_matrix(rows, cols)
# print_matrix(new_matrix)
# print_sum_cols(new_matrix)








































