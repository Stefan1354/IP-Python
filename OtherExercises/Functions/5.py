#5.Да се състави програма с функция, която получава като аргументи референция към функция и две цели числа. Функцията връща като резултат
#най-голямата стойност на предадената като първи аргумент функция в целочислените точки на диапазона, границите на които се определят от втория
#и третия аргумент.

def max_s(func = 'x*2', a = 1, b = 4):
    max = eval(func.replace('x', str(a)))
    for i in range(a, b+1):
        value = eval(func.replace('x', str(i)))
        if value > max:
            max = value
        print(f"f({i})={eval(func.replace('x', str(i)))}")
    return max



function = input("Type in a function (eg. x*3):\n")

lim_1 = int(input("Type in the left limit: "))
lim_2 = int(input("Type in the right limit: "))

print(f"The highest value of the function ({function}) in the limit of [{lim_1}, {lim_2}] ="
      f" {max_s(function, lim_1, lim_2)}")
