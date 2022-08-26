#12.Да се състави програма с използването на клас с два метода get_String и print_String. Методът get_String приема символен низ от потребителя, 
#а print_String извежда символния низ с главни букви.

class StringClass:
    def __init__(self):
        self.string = ""

    def get_string(self, user_str):
        self.string = user_str

    def print_string(self):
        print(self.string.upper())

string_class = StringClass()

string_class.get_string("hello world")
string_class.print_string()