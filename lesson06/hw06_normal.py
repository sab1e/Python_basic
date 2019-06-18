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


class People:
    def __init__(self, name, surname, middlename, birth_date, school):
        self.name = name
        self.surname = surname
        self.middlename = middlename
        self.birth_date = birth_date
        self.school = school

    def get_full_name(self):
        return self.surname + ' ' + self.name + ' ' + self.middlename

    def get_surname_n_m(self):
        return self.surname + ' ' + self.name[0] + '.' + self.middlename[0] + '.'

    def set_name(self, new_name):
        self.name = new_name


class Student(People):
    def __init__(self, name, surname, middlename, birth_date, school, class_room, fio_mother, fio_father):
        People.__init__(self, name, surname, middlename, birth_date, school)
        self._class_room = {'class_num': int(class_room.split()[0]),
                            'class_char': class_room.split()[1]}
        self.parents = {'mother': fio_mother,
                        'father': fio_father}

    @property
    def class_room(self):
        return f"{self._class_room['class_num']} {self._class_room['class_char']}"

    def next_class(self):
        self._class_room['class_num'] += 1


class Teacher(People):
    def __init__(self, name, surname, middlename, birth_date, school, topic, teach_classes):
        People.__init__(self, name, surname, middlename, birth_date, school)
        self.topic = topic
        self._teach_classes = list(map(self.convert_class, teach_classes))

    # Уникальный метод Учителя
    def convert_class(self, class_room):
        """
        '<class_num> <class_int>' --> {'class_num': <class_num>, 'class_int': <class_int>}
        """
        return {'class_num': int(class_room.split()[0]),
                'class_char': class_room.split()[1]}

    @property
    def teach_classes(self):
        return [str(self._teach_classes[i]['class_num']) + ' ' + self._teach_classes[i]['class_char']
                for i in range(len(self._teach_classes))]


students = [Student("Александр", "Иванов", "Петрович", '10.11.1998', "8 гимназия", "7 В",
                    "Иванова Мария Николаевна", "Иванов Петр Алексеевич"),
            Student("Петр", "Сидоров", "Олегович", '10.01.1995', "8 гимназия", "5 А",
                    "Сидорова Ольга Констатиновна", "Сидоров Олег Игоревич"),
            Student("Иван", "Петров", "Дмитриевич", '12.11.1999', "8 гимназия", "4 В",
                    "Петрова Александра Михайловна", "Петров Дмитрий Николаевич"),
            Student("Амадей", "Тимофеев", "Анатольевич", "05.05.1996", "8 гимназия", "5 А",
                    "Тимофеева Сильва Филипповна", "Тимофеев Анатолий Константинович")
            ]

teachers = [Teacher("Борислав", "Ахметзянов", "Сергеевич", "27.11.1974", "8 гимназия", "информатика",
                    ["7 В", "8 Б"]),
            Teacher("Эммануил", "Лютов", "Юрьевич", "28.06.1970", "8 гимназия", "математика",
                    ["5 А", "8 Б", "4 В", "7 В"]),
            Teacher("Вера", "Фомина", "Дмитриевна", "18.05.1977", "8 гимназия", "чтение",
                    ["4 В", "5 А"])
            ]


# Полный список всех классов школы
full_class = []
for student in students:
    if student.class_room not in full_class:
        full_class.append(student.class_room)
print(f"Список всех классов в школе: {', '.join(full_class)}")

# Список всех учеников в указанном классе
class_room_search = '5 А'
print(f'\nСписок учеников в {class_room_search} классе:')
class_list = [student.get_surname_n_m() for student in students if student.class_room == class_room_search]
for i, fio in enumerate(class_list, start=1):
    print(f'{i}. {fio}')

# Список всех предметов указанного ученика
student_topic = 'Иванов Александр Петрович'
i = 1
print(f'\nСписок предметов ученика {student_topic}:')
for student in students:
    if student.get_full_name() == student_topic:
        for teacher in teachers:
            if student.class_room in teacher.teach_classes:
                print(f'{i}. {teacher.topic}')
                i += 1

# ФИО родителей указанного ученика
student_parents = 'Иванов Александр Петрович'
print(f'\nРодители ученика {student_parents}:')
for student in students:
    if student.get_full_name() == student_parents:
        print(f"Мама - {student.parents['mother']}\nПапа - {student.parents['father']}")


# Список всех Учителей, преподающих в указанном классе
class_teachers = '5 А'
print(f'\nСписок учителей, преподающтх в {class_teachers}:')
teachers_for_class = [teacher.get_full_name() for teacher in teachers if class_teachers in teacher.teach_classes]
for i, teacher in enumerate(teachers_for_class, start=1):
    print(f'{i}. {teacher}')