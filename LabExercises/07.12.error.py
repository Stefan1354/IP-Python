#SyntaxError: invalid syntax
'''while True print("Hello world")'''
#SyntaxError: invalid syntax

#1: ZeroDivisionError
'''>>>> 10*(1/0)'''
#ZeroDivisionError: division by zero

#2: NameError
'''4+spam*3'''
#NameError: name 'spam' is not defined

#3: TypeError
''' '2' + 2'''
#TypeError: Can't convert 'int' object to str implicity


'''try:
    print(x)
except:
print("An exception occurred")
#SyntaxError: expected an indented block

try:
    print(x)
except:
    print("An exception occurred")'''

'''try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")'''

#kluchova duma else
'''try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")'''

#kluchova duma finally
'''try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")'''

#zatvarqne na obektite i osvobojdavane na resursite
'''try:
    f=open('demofile.txt')
    f.write("Lorem Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()'''

#vavejdane na cqlo schislo kato vhod ot strana na potrebitelq
'''while True:
    try:
        x=int(input("Enter x "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")

except(RuntimeError, TypeError, NameError):
    pass'''

#situaciq na izkluchenie pri funkcii
'''def this_files():
    x=1/0
try:
    this_fails()
except ZeroDivisionError as err:
    print("Handling run-time error:", err)
#Handling run-time error: division by zero'''

#kluchova duma raise
'''x=-1
if x<0:
raise Exception("Sorry, no numbers below zero")'''

#greshka TypeError, ako tipat na x ne e int
'''x='Hello'
if not type(x) is int:
raise TypeError("Only integers are allowed")'''

#greshka, vurnata ot interpretatora pri generirane na situaciq HiThere:
'''raise NameError('HiThere')
Traceback (most recent call last):
NameError: HiThere'''

#raise ValueError

#raise ValueError()
