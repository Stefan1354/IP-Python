#1.Напишете програма , в която се създава функция с два 
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