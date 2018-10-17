# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class School:
    def __init__(self, name):
        self.name = name
        self.classrooms = []

    def add_classroom(self, classroom):
        self.classrooms.append(classroom)

    def show_classrooms(self):
        for i in self.classrooms:
            print(i.name)


class Classroom:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        for i in self.students:
            print(i.show_fio())

    def show_teachers(self):
        for i in self.teachers:
            print(i.show_fio())

    def show_lesson(self):
        for i in self.teachers:
            print(i.lesson)


class People:
    def __init__(self, surname, name, second_name):
        self.name = name
        self.second_name = second_name
        self.surname = surname

    def show_fio(self):
        print("{} {}.{}." .format(self.surname, self.name[0:1], self.second_name[0:1]))


class Teacher(People):
    def __init__(self, surname, name, second_name, lesson):
        People.__init__(self, surname, name, second_name)
        self.lesson = lesson


class Student(People):
    def __init__(self, surname, name, second_name, classroom, mother_name, father_name):
        People.__init__(self, surname, name, second_name)
        self.classroom = classroom
        self.mother_name = mother_name
        self.father_name = father_name

    def show_parents(self):
        print("Мама {}, папа {}" .format(self.mother_name, self.father_name))

# Создаем школу
school = School("Школа №1")

# Создаем классы
classrooms = [Classroom("1A"), Classroom("2B"), Classroom("3B")]

# Добавляем классы в школу

school.add_classroom(classrooms[0])
school.add_classroom(classrooms[1])
school.add_classroom(classrooms[2])

# Создаем учителей

teachers = [Teacher("Петрова", "Мария", "Ивановна", "Русский язык"),
            Teacher("Стопкин", "Федор", "Петрович", "Труд"),
            Teacher("Тетчер", "Элеонора", "Фэйсомобтейбловна", "Английский язык"),
            Teacher("Синусова", "Гипотенуза", "Тангенсовна", "Геометрия"),
            Teacher("Аляскин", "Баскунчак", "Байкалович", "География"),
            Teacher("Ампер", "Вольт", "Омович", "Физика")]

# Добавляем учителей в класс

classrooms[0].add_teacher(teachers[0])
classrooms[0].add_teacher(teachers[2])
classrooms[0].add_teacher(teachers[4])
classrooms[1].add_teacher(teachers[1])
classrooms[1].add_teacher(teachers[3])
classrooms[1].add_teacher(teachers[5])
classrooms[2].add_teacher(teachers[1])
classrooms[2].add_teacher(teachers[2])
classrooms[2].add_teacher(teachers[3])

# Создаем учеников

students = [Student("Ivanov", "Ivan", "Ivanovich", classrooms[0], "Ivanova M.I", "Ivanov I.N"),
            Student("Petrov", "Peter", "Petrovich", classrooms[1], "Petorva M.P", "Petrov P.P"),
            Student("Sidoorv", "Sidor", "Sidorovich", classrooms[2], "Sidorova S.S.", "Sidorov S.V"),
            Student("Колобков", "Иван", "Петрович", classrooms[2], "Колобкова И.А.", "Колобков П.П7")]

# Добавляем учеников в класс

classrooms[0].add_student(students[0])
classrooms[1].add_student(students[1])
classrooms[2].add_student(students[2])
classrooms[2].add_student(students[3])

# 1. Получить полный список всех классов школы

school.show_classrooms()

# 2. Получить список всех учеников в указанном классе

classrooms[0].show_students()   # Здесь почемуто после ФИО пишет еще None
classrooms[1].show_students()   # Почему я так и не поня
classrooms[2].show_students()   # если простоученика вызвать то None не вылазит

#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)

students[0].classroom.show_lesson()
# 4. Узнать ФИО родителей указанного ученика

students[0].show_parents()
# 5. Получить список всех Учителей, преподающих в указанном классе

classrooms[2].show_teachers()



