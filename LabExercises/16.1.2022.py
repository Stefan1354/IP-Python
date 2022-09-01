from hashlib import new


class Student:
    def __init__(self, f_num, name, family, grade):
        self.f_num=f_num
        self.name=name
        self.family=family
        self.grade=grade

    def __str__(self):
        return f"{self.f_num}, {self.name} : , {self.grade} "

class Group:
    def __init__(self, st_list:list):
        self.st_list:list=st_list
    
    def present(self):
        for st in self.st_list:
            print(f"{st.name}, {st.family} -> {st.f_num}")
        print()

    def add_new(self, new_st:Student):
        for st in self.st_list:
            if st.f_num==new_st.f_num:
                print("This student is already in the group!")
                return
        else:
            self.st_list.append(new_st)
            print("The new student is ",new_st)
    
    def remove(self):
        for i in self.st_list:
            if i.grade<3:
                self.st_list.remove(i)

    def avg_grade(self):
        grades=[st.grade for st in self.st_list]
        return round(sum(grades)/len(self.st_list), 2)

    def get_min_grade(self):
        sr_list=sorted(self.st_list, key=lambda student:student.grade)
        return sr_list[0]
    
    def get_max_grade(self):
        sr_list=sorted(self.st_list, key=lambda student:student.grade, reverse=True)
        return sr_list[0]

    def get_equal_grade(self, grade):
        new_set=set()
        for i in range(len(self.st_list),2):
            if self.st_list[i].grade==grade:
                new_set.add(self.st_list[i])
        return new_set

gr43a=Group([Student(121221146, "Aleksandar", "Shopov", 4.60), Student(121221987, "Ivan", "Smiljanov", 5.50), Student(1231232, "Mirko", "Ivanov", 2.90),
Student(123554433, "Igor", "Rakovski", 4.60)])

gr43a.add_new(Student(12322255, "Boris", "Manov", 5.40))
gr43a.present()

print("Sredniqt uspeh na grupata e ",gr43a.avg_grade())
print("Minimalniq uspeh ima ",gr43a.get_min_grade())
print("Maksimalniqt uspeh ima ",gr43a.get_max_grade())

gr_stud_list=gr43a.get_equal_grade(4.60)
for i in gr_stud_list:
    print("Studentite sus ednakuv uspeh sa ",i)

gr43a.remove()