#4.Да се състави програма с функция с един текстов аргумент и произволен брой целочислени
#аргументи. Резултатът се явява текст, сформиран от буквите на първия текстов аргумент. 
#Целочислените аргументи определят индексите на буквите, които трябва да влязат в текста 
#резултат.

def string_index(*args, string):
    new_string = ""
    for index in args:
        if index < len(string) and index >= 0:
            new_string += string[index]

    return new_string


print(string_index(1, 3, 3, 0, 0, string='Hello World'))
