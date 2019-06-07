__author__ = 'Соболев Антон'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

print(f'{"-"*5} Задача 1 {"-"*5}')

fruits = ["абрикос", "инжир", "лайм", "киви", "дуриан", "авокадо", "апельсин", "грейпфрут"]

for fruit in fruits:
	print(f'{str(fruits.index(fruit) + 1)}.{fruit:>12}')


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

# Варинт 1
print(f'\n {"-"*5} Задача 2 {"-"*5}')

# задаем изначальные списки
colors_1 = ["yellow", "green", "blue", "brown", "white", "red", "orange", "pink"]
colors_2 = ["gray", "violet", "green", "blue", "black", "purple", "orange", "white"]

# выводим списки на экран
print(f'Список 1: {colors_1}')
print(f'Список 2: {colors_2}\n')

# проверяем есть ли совпадение элементов списка colors_2
# с элементами в списке colors_1
# при таком совпадении элемент удаляется из списка colors_1
for color in colors_2:
	if color in colors_1:
		colors_1.remove(color)

# выводим список colors_1 без элементов списка colors_2
print(f'Вариант 1. Список 1 без элементов списка 2: {colors_1} \n')

# Вариант 2
colors_1 = ["yellow", "green", "blue", "brown", "white", "red", "orange", "pink"]
colors_2 = ["gray", "violet", "green", "blue", "black", "purple", "orange", "white"]

# преобразовываем исходные списки в множества
# исключаем из первого списка элементы, которые встречаются во втором списке с помощью метода множества
# и преобразовываем, полученное множество обратно в список (по условию задачи должен быть список)

colors_1 = list(set(colors_1) - set(colors_2))

print(f'Вариант 2. Список 1 без элементов списка 2: {colors_1}')

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

print(f'\n{"-"*5} Задача 3 {"-"*5}')

import random

# генерируем случайный исходный список
some_data = [random.randint(1, 100) for i in range(10)]
print("Исходный список:\n", some_data)

# Вариант 1
data = []
for x in some_data:
	if x%2 == 0:
		data.append(x/4)
	else:
		data.append(x*2)

print("Новый список Вариант 1:\n", data)

# Вариант 2
data = []
data = [x/4 if x%2 == 0 else x*2 for x in some_data]
print("Новый список Вариант 2:\n", data)