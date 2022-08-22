#2.Съставете програма с функция, която получава като аргумент числов списък и
#връща като резултат друг списък, 
#в който са включени само четните числа от списъка аргумент.

# def cetni(l):
#     new_list=[]
#     for i in range (len(l)):
#         if l[i]%2==0:
#             new_list.append(l[i])
#     return new_list

# n=int(input("Enter n "))
# nums=[]
# for i in range(n):
#     num=int(input(f"Please enter number {i+1}: "))
#     nums.append(num)
# print(cetni(nums))





day=int(input("Enter day: "))
month=int(input("Enter month: "))
year=int(input("Enter year: "))

if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    max_days=31
elif month==4 or month==6 or month==9 or month==11:
    max_days=30
elif month==2:
    if (year%4==0 and year%100!=0) or year%400==0:
        max_days=29
    else:
        max_days=28

if month<1 or month>12:
    print("Entered date is valid")
    print("Check the range of month")
elif day<1 or day>max_days:
    print("Entered date is valid")
    print("Check the range of the day")
elif year<1900 or year>2021:
    print("invalid date")
else:
    print("Entered date is valid")
    dd=str(day)
    mm=str(month)
    yyyy=str(year)
    if month<10:
        mm="0"+mm
    if day<10:
        dd="0"+dd

    given_date=dd+mm+yyyy
    reversed_date=given_date[::-1]
    if given_date==reversed_date:
        print("The date is palindrom ")
    else:
        print("The date isn't palindrom")
