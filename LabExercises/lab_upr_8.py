#1.Да се напише код на Пайтън който дефинира Class Person с полета име 
# (name), фамилия (family), възраст(age), националност(nationality).
# Да се дефинира конструктор (init) който инициализира полетата на класа.
# Да се добави метод print който отпечатва имената и националноста на съответното лице. 
# Да се създадат обекти инстанции на класа. За тях да се извика методът print.
# Да се добави към кода от задача 1 Class Student, наследник на Class Person с две нови полета университет (university)
#и година на обучение (year of study).Да се предефинира за него методът принт, така че да отпечатва и тези две полета. 
#Да се създадат инстанции на новия клас и за тях да се извика методът принт.Да се добави клас Lecturer, наследник на
#класа Person с две нови полета - университет (university) и опит (experience) - брой години преподавателски стаж.
#Да се предефинира за него методът принт, така че да отпечатва тези две полета. Да се създадат инстанции на новия 
#клас и за него да се извика методът принт.


#1.
class Person:
    def __init__(self, name, family, nationality, age):
        self.name = name
        self.family = family
        self.nationality = nationality
        self.age = age

    def print(self):
        print(self.name, self.family, self.nationality, self.age)
    
class Student(Person):
    def __init__(self, name, family, nationality, age, university, year_of_study):
        Person.__init__(self, name, family, nationality, age)
        self.university = university
        self.year_of_study = year_of_study

    def print(self):
        print(str.format("{} {} - {} years old - {} : {} year:{}\n\n", self.name, self.family, self.age, self.nationality, self.university, self.year_of_study))

class Lecturer(Person):
    def __init__(self, name, family, nationality, age, university, experience):
        super().__init__(name, family, nationality, age)
        self.university = university
        self.experience = experience

    def print(self):
        print(str.format("{} {} - {} years old - {} : {} year:{}\n\n", self.name, self.family, self.age, self.nationality, self.university, self.experience))


Person1 = Person("Ivan", "Vasilev", "Bulgarian", 19)
Person2 = Student("Petar", "Stoyanov", "Bulgarian", 21, "Technical University", 2019)
Person3 = Lecturer("Marko", "Minkov", "Bulgarian", 30, "Sofia University St. Kliment Ohridski", 7)
Person1.print()
Person2.print()
Person3.print()

#2.Създайте клас който представя студентите във вашата група. Напишете метод който по добавено име добавя само
#студенти които не са записани в списъка от студенти. Напишете метод remove за триене на студентите със слаб успех. 
#Напишете метод за намиране на среден успех на групата.
#part 2 метод за намиране на min/max grade - 2methods и метод който връща данните за студентите с еднакъв успех

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

    def create_new_list(self, file):
        for row in file:
            data_list = row.split(' ')
            self.st_list.append(Student(int(data_list[0]), data_list[1], data_list[2], float(data_list[3])))


    def get_names_a(self):
        res_list = list()
        for i in self.st_list:
            if i.name[0] == 'A':
                res_list.append(i)
        return res_list

    def set_names_upper(self):
        for i in range(len(self.st_list)):
            self.st_list[i].name = self.st_list[i].name.upper()
            self.st_list[i].f_name = self.st_list[i].f_name.upper()

    def sort_id(self):
        return sorted(self.st_list, key=lambda st: st.f_num)

gr43a = Group([Student(121221146, 'Aleksandar', 'Shopov', 4.60), Student(121221144, 'Aysel', 'Kazalieva', 4.60),
               Student(121221178, 'Miroslav', 'Dilov', 5.60), Student(121221000, 'Nqkoi', 'Nepoznat', 2.60),
               Student(121221096, 'Vasil', 'Alendarov', 5.60)])

gr43a.add_new(Student(121221096, 'Kristiqn', 'Petkov', 6.00))
gr43a.add_new(Student(121221010, 'Maksim', 'Nikolov', 3.60))
gr43a.present()

# # print по успех
print("Uspehat na grupata e ",gr43a.avg_grade())
print("Minimalen uspeh ima ",gr43a.get_min_grade())
print("Maksimalen uspeh ima ",gr43a.get_max_grade())

# метод който връща данните за студентите с еднакъв успех
gr_stud_list = gr43a.get_equal_grade(5.60)
for i in gr_stud_list:
         print("Studentite s ednakuv uspeh sa ",i)
gr_stud_list=gr43a.get_equal_grade(4.60)
for i in gr_stud_list:
    print("Studentite s ednakuv uspeh sa ",i)

gr43a.remove()

for st in gr43a.get_names_a():
    print(st)
print()
gr43a.set_names_upper()
for st in gr43a.st_list:
    print(st)
print()  #163 do 166 red se mora napise da bi site printiralo s golemi bukvi

for st in gr43a.sort_id():
    print(st)
