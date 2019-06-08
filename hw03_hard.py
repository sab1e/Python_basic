__author__ = 'Соболев Антон'

# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

print(f'{"-"*5} Задание-1 {"-"*5}')


def fraction_sum(fract_1, fract_2):
    m_fraction_1 = []
    m_fraction_2 = []
    for i in fract_1:
        m_fraction_1.append(int(i) * int(fract_2[1]))
    for i in fract_2:
        m_fraction_2.append(int(i) * int(fract_1[1]))
    sum_fraction = []
    sum_fraction.append(m_fraction_1[0] + m_fraction_2[0])
    sum_fraction.append(m_fraction_1[1])
    return sum_fraction


def fraction_in(fract_expr):
    fract_lst = fract_expr.split()
    if '-' in fract_lst:
        action = '-'
        index = fract_lst.index('-')
    elif '+' in fract_lst:
        action = "+"
        index = fract_lst.index('+')

    if len(fract_lst[:index]) == 1:
        fract_1 = fract_lst[0].split('/')
    elif len(fract_lst[:index]) == 2:
        fract_1 = fract_lst[1].split('/')
        numerator = abs(int(fract_lst[0])) * int(fract_1[1]) + int(fract_1[0])
        if int(fract_lst[0]) < 0:
            numerator = -numerator
        fract_1[0] = numerator

    if len(fract_lst[index:]) == 2:
        fract_2 = fract_lst[-1].split('/')
        if action == '-':
            fract_2[0] = -int(fract_2[0])
    elif len(fract_lst[index:]) == 3:
        fract_2 = fract_lst[-1].split('/')
        numerator = abs(int(fract_lst[-2])) * int(fract_2[-1]) + int(fract_2[0])
        if int(fract_lst[-2]) < 0:
            numerator = -numerator
        if action == '-':
            numerator = -numerator
        fract_2[0] = numerator

    return fract_1, fract_2


def fraction_out(fract):
    if len(fract) == 2:
        print(f'{fract[0]}/{fract[1]}')
    if len(fract) == 1:
        print(f'{fract[0]} {fract[1]}/{fract[2]}')


fract_1, fract_2 = fraction_in('5/6 + 4/7')

summ = fraction_sum(fract_1, fract_2)
fraction_out(summ)


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
print(f'{"-"*5} Задание-2 {"-"*5}')

import os


def open_files(path):
    with open(path, 'r', encoding = 'UTF-8') as f:
        next(f)
        l = [line.strip() for line in f]
    return list(map(lambda x: x.split(), l))


def calc_salary (staff, hours):
    for i in range(len(staff)):
        for j in range(len(hours)):
            if staff[i][0] in hours[j] and staff[i][1] in hours[j]:
                staff[i].append(hours[j][2]) 
    
    for i in range(len(staff)):
        one_hours_pay = int(staff[i][2]) / int(staff[i][4])
        delta_hours = int(staff[i][5]) - int(staff[i][4])
        if delta_hours > 0:
            staff[i].append(round(int(staff[i][2]) + one_hours_pay*delta_hours*2))
        else:
            staff[i].append(round(int(staff[i][2]) - abs(one_hours_pay*delta_hours)))
    return staff

staff_list = open_files(os.path.join('data', 'workers'))
hours_of = open_files(os.path.join('data', 'hours_of'))
result_staff_list = calc_salary(staff_list, hours_of)

print("Итоговая зарплата сотрудников ООО 'Рога и Копыта' за месяц составила:")
for i in range(len(result_staff_list)):
    print(f'{result_staff_list[i][0]} {result_staff_list[i][1]}: {result_staff_list[i][6]} руб.')


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
print(f'{"-"*5} Задание-3 {"-"*5}')

import os

path = os.path.join('data', 'fruits.txt')
with open(path, 'r', encoding = 'UTF-8') as f:
    for line in f:
        if line != '\n':
            fruit = line.strip()
            file_name = 'fruits_' + fruit[0] + '.txt'
            path_alpha = os.path.join('data', file_name)

            with open(path_alpha, 'a', encoding='UTF-8') as fw:
                fw.write(fruit + '\n')
                fw.write('\n')

print('Запись в файлы заверешена')
