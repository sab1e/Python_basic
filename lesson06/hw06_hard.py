# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла
import os


class Worker:
    def __init__(self, string_from_file):
        string_from_file = string_from_file.split()
        self.name = string_from_file[0]
        self.surname = string_from_file[1]
        self.solary = int(string_from_file[2])
        self.position = string_from_file[3]
        self.hours_rate = int(string_from_file[4])
        self.hours_of = None

    def set_hours_of(self, hours_of):
        self.hours_of = int(hours_of)

    def calc_salary(self):
        one_hour_pay = self.solary / self.hours_rate
        delta_hours = self.hours_of - self.hours_rate
        if delta_hours > 0:
            return round(self.solary + one_hour_pay * delta_hours * 2)
        else:
            return round(self.solary - abs(one_hour_pay * delta_hours))


path_1 = os.path.join('data', 'workers')
with open(path_1, 'r', encoding='UTF-8') as f:
    next(f)
    workers = [Worker(line.strip()) for line in f]

path_2 = os.path.join('data', 'hours_of')
with open(path_2, 'r', encoding='UTF-8') as f2:
    next(f2)
    for line in f2:
        hours_worked = line.split()
        for worker in workers:
            if worker.name == hours_worked[0] and worker.surname == hours_worked[1]:
                worker.set_hours_of(hours_worked[2])

print("Итоговая зарплата сотрудников ООО 'Рога и Копыта' за месяц составила:")
for worker in workers:
    print(f'{worker.name} {worker.surname}: {worker.calc_salary()} руб.')

