__author__ = 'Соболев Антон'


import sys
import hw05_easy

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


def main_menu():
    print(f'\nСписок действий:')
    print(f'1. Перейти в папку')
    print(f'2. Просмотреть содержимое текущей папки')
    print(f'3. Удалить папку')
    print(f'4. Создать папку')
    print(f'5. Выход')


do_main = {1: hw05_easy.change_dir,
           2: hw05_easy.view_dir,
           3: hw05_easy.remove_dir,
           4: hw05_easy.create_dir,
           5: sys.exit
           }

print(f'Добро пожаловать в консольную утилиту для работы с папками')

while True:
    main_menu()
    try:
        action = int(input('\nВведите номер меню:'))
    except IndexError:
        action = None
    except ValueError:
        print('Необходимо ввести число от 1 до 5')
        action = None

    if action:
        if do_main.get(action):
            do_main[action]()
        else:
            print('Такого номера оперции не существует, попробуйте еще раз')
