#6.Напишете програма, в която по метода на рекурсията символите от текста, предаден като аргумент на функцията, се изобразяват „през един“: 
#т.е. изписва се първият, третият, петият и т.н. символ.

def recursion(string, index = 0):
    if index > len(string) - 1:
        return None
    if index % 2 == 0:
        print(string[index])
    recursion(string, index+1)
recursion(string = "Hello World")


#2 nacin

def recursion(string):
    new_string = ''
    for i in range(len(string)):
        if i%2==0:
            new_string+=string[i]
    return new_string
string = input("Enter string: ")
print(recursion(string))        #Enter string: Stefan
                                #Sea
