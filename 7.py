class Student:
    def __init__(self, name, surname, age, group):
        self.name = name
        self.surname = surname
        self.age = age
        self.group = group
        self.grades = []

    def show_info(self):
        print(f"Ism: {self.name}")
        print(f"Familiya: {self.surname}")
        print(f"Yosh: {self.age}")
        print(f"Guruh: {self.group}")

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if not self.grades:
            return "Baholar mavjud emas"
        return sum(self.grades) / len(self.grades)

    def show_grades(self):
        if not self.grades:
            print("Baholar mavjud emas")
        else:
            print(f"Baholar: {', '.join(map(str, self.grades))}")

    def is_excellent(self):
        avg = self.average_grade()
        if isinstance(avg, (int, float)) and avg >= 4.5:
            print("A'lochi talaba")
        else:
            print("Oddiy talaba")


student1 = Student("Ali", "Valiyev", 17, "Python-01")
student2 = Student("Olim", "Karimov", 18, "Python-01")
student3 = Student("Zuhra", "Toshmatova", 17, "Python-02")

student1.add_grade(5)
student1.add_grade(4)
student1.add_grade(5)

student2.add_grade(3)
student2.add_grade(4)
student2.add_grade(4)

student3.add_grade(5)
student3.add_grade(5)
student3.add_grade(5)

students = [student1, student2, student3]

for i, student in enumerate(students, 1):
    print(f"--- {i}-talaba ---")
    student.show_info()
    student.show_grades()
    avg = student.average_grade()
    if isinstance(avg, float):
        print(f"O'rtacha baho: {avg:.2f}")
    else:
        print(f"O'rtacha baho: {avg}")
    student.is_excellent()
    print()