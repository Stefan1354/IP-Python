#9.Съставете клас на Python с името Student с две свойства: student_id и student_name. Добавете ново свойство student_class. Създайте функция за
#извеждане на цялото свойство и техните стойности в класа Student.

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def add_class(self, student_class):
        self.student_class = student_class

    def Print(self):
        print(self.student_name, self.student_id, self.student_class)

student1 = Student(1212121, "Stefan")
student1.add_class(43)
student1.Print()                         #printira
                                         #Stefan 1212121 43
