'''1.Write a Python class to convert an integer to a roman numeral'''

# class py_solution:
#     def int_to_Roman(self, num):
#         val = [
#             1000, 900, 500, 400,
#             100, 90, 50, 40,
#             10, 9, 5, 4,
#             1
#             ]
#         syb = [
#             "M", "CM", "D", "CD",
#             "C", "XC", "L", "XL",
#             "X", "IX", "V", "IV",
#             "I"
#             ]
#         roman_num = ''
#         i = 0
#         while  num > 0:
#             for _ in range(num // val[i]):
#                 roman_num += syb[i]
#                 num -= val[i]
#             i += 1
#         return roman_num


# print(py_solution().int_to_Roman(1))     #I
# print(py_solution().int_to_Roman(4000))  #MMMM
# print(py_solution().int_to_Roman(6))     #VI


'''2.Write a Python class to convert a roman numeral to an integer.'''

# class py_solution:
#     def roman_to_int(self, s):
#         rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#         int_val = 0
#         for i in range(len(s)):
#             if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
#                 int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
#             else:
#                 int_val += rom_val[s[i]]
#         return int_val

# print(py_solution().roman_to_int('MMMCMLXXXVI'))
# print(py_solution().roman_to_int('MMMM'))
# print(py_solution().roman_to_int('C'))


'''3.Write a Python class to reverse a string word by word.'''

# class py_solution:
#     def reverse_words(self, s):
#         return ' '.join(reversed(s.split()))


# print(py_solution().reverse_words('hello .py'))



'''4.Write a Python class which has two methods get_String and print_String. get_String accept a 
string from the user and print_String print the string in upper case.'''

# class IOString():
#     def __init__(self):
#         self.str1 = ""

#     def get_String(self):
#         self.str1 = input("Input string: ")

#     def print_String(self):
#         print(self.str1.upper())

# str1 = IOString()
# str1.get_String()
# str1.print_String()


'''5.'''