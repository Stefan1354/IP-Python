'''1.Napisete potrebitelska funkciq proverqvashta dali chislo
e palindrom. Funkciqta poluchava kato argument chislo, vrshta
kato rezultat 1, ako chisloto e palindrom, i 0 ako chisloto
ne e palindrom.'''

#palindrom e poredica od chislovi stoinosti, koito se cetat
#po edin i susht nacin otpred nazad i otzad napred
#primer 787, 505, 101


# def palindrom(n):
#     a=str(n)
#     b=a[::-1]
#     if a==b:
#         return 1
#     else:
#         return 0
# n=input("Enter n: ")
# print(palindrom(n))


'''2.Da se szdade programa koqto realizira kalkulator za celi
chisla. Deistviata koito ispulnava sa sbirane(+),izvazdane(-)
umnozenie(*),delenie(/).Pri natiskane na butona, potrebitelq
vavezda vida na operaciata, sled tova vavezda dve chisla i 
rezultata se izvezda na ekrana.'''

# def operations(op):
#      n1 = int(input("n1 ="))
#      n2 = int(input("n2 ="))
#      if op == '+':
#          return n1 + n2

#      if op == '-':
#          return n1 - n2

#      if op == '*':
#          return n1 * n2

#      if op == '/':
#          return n1 / n2


#operation = input('What operation to you want to do? \n')
#print(operations(operation))

'''3. Na funkciq se podavat 2 argumenta: spisuk s chisla i chislo.
Promenete vsichki elementi ot spisuka ss stoinost po golqma
ot dadenoto chislo na 0.
podavame na funkciq 2 elementa'''

# def list_limit(list, limit):
#     new_list = []
#     for item in list:
#         if item >= limit:
#             item = 0
#         new_list.append(item)

#     return new_list


# n = int(input('How long do you want the list to be? '))

# l = []
# for i in range(n):
#     l.append(int(input(f'l[{i}] = ')))

# lim = int(input('what is the limit you want? '))

# print(f"the new list is: {list_limit(l, lim)} ")


'''4.Napisete programa s funkciq s proizvolen broj cislovi argumenti,
koqto vurshta kato rezultat spisuk ot tri elementa:
srednoaritmeticnata, maksimalnata i minimalnata stoinost na argumentite.'''

# def n_arg_func(*args):
#     list=args
#     return[sum(list)/len(list),max(list),min(list)]
# print(n_arg_func(1,2,3)) #[2.0, 3, 1]
