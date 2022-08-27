# '''1.Напишете код на метод който приема като параметър име на текстов файл, 
# прочита съдържанието на файла и го връща като стринг.'''

# def readFromFile(fileName):
#     f=open(fileName, "r")
#     print(f.read())

# try:
#     f=open("file.txt","x")
# except FileExistsError:
#     f=open("file.txt","w")
# f.write("Test file!")
# f.close()

# readFromFile("file.txt")

#2 primer
# def read_txt(filepath):
#     try:
#         with open(filepath) as file:
#             file_data=file.read()
#             return file_data
#     except FileNotFoundError:
#         print("This file does not exist!")
# filepath=input("What is the path of the file? ")
# print(read_txt(filepath))

# '''2.Напишете метод за намиране на минимален успех на групата. 
# Напишете метод за намиране на максимален успех на групата. 
# Напишете метод който връща данните за студентите които са с един и същ успех.'''
#BITNA ZADACA!!!!!!!!!!!!


class Student():
    def __init__(self, f_num, name, family, grade):
        self.f_num = f_num
        self.name = name
        self.f_name = family
        self.grade = grade

    def __str__(self):
        return str.format('{} {}: {}', self.f_num, self.name, self.grade)


class Group:
    def __init__(self, st_list: list):
        self.st_list: list = st_list

    def present(self):
        for st in self.st_list:
            print(str.format("{} {} -> f_num: {}", st.name, st.f_name, st.f_num))
        print()

    def add_new(self, new_st: Student):
        for st in self.st_list:
            if st.f_num == new_st.f_num:
                print('This student is already in the group!!')
                return
        else:
            self.st_list.append(new_st)
            print("Done")

    def remove(self):
        for i in self.st_list:
            if i.grade < 3:
                self.st_list.remove(i)

    def avg_grade(self):
        grades = [st.grade for st in self.st_list]
        return round(sum(grades) / len(self.st_list), 2)

    def get_min_grade(self):
        sr_list = sorted(self.st_list, key=lambda student: student.grade)
        return sr_list[0]

    def get_max_grade(self):
        sr_list = sorted(self.st_list, key=lambda student: student.grade, reverse=True)
        return sr_list[0]

    def get_equal_grade(self, grade):
        new_set = set()
        for i in range(len(self.st_list)):
            if self.st_list[i].grade == grade:
                new_set.add(self.st_list[i])
        return new_set


gr43a = Group([Student(121221146, 'Aleksandar', 'Shopov', 4.60), Student(121221144, 'Aysel', 'Kazalieva', 4.60),
               Student(121221178, 'Miroslav', 'Dilov', 5.60), Student(121221000, 'Nqkoi', 'Nepoznat', 2.60),
               Student(121221096, 'Vasil', 'Alendarov', 5.60)])

# gr43a.add_new(Student(121221096, 'Vasil', 'Alendarov', 5.60))
gr43a.add_new(Student(121221010, 'Ívan', 'Nikolov', 5.60))
gr43a.present()

# print по успех
print("Sredniq uspeh na grupata e ", gr43a.avg_grade())
print("Minimalniq uspeh na student ot grupata e ", gr43a.get_min_grade())
print("Maksimalen uspeh na student ot grupata e ", gr43a.get_max_grade())

# метод който връща данните за студентите с еднакъв успех
gr_stud_list = gr43a.get_equal_grade(5.60)
for i in gr_stud_list:
    print("Studentite sus susht uspeh sa: ", i)

#gr43a.remove()
