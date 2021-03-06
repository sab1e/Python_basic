__author__ = 'Соболев Антон'

# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

print(f'{"-"*5} Задание-1 {"-"*5}')

a = [1, 2, 3, 4, 0]
b = [x**2 for x in a]

print(b)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

print(f'\n{"-"*5} Задание-2 {"-"*5}')

fruits_list1 = ["абрикос", "инжир", "лайм", "киви", "дуриан", "авокадо", "апельсин", "грейпфрут"]
fruits_list2 = ["абрикос", "арбуз", "лимон", "дуриан", "киви", "авокадо", "апельсин", "яблоко"]
fruits = [fruit for fruit in fruits_list1 if fruit in fruits_list2]

print(fruits)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

print(f'\n{"-"*5} Задание-3 {"-"*5}')

a = [1, 9, -5, 16, 7, 10, -8, 12, 40, 21]
b = [x for x in a if x > 0 and x % 3 == 0 and x % 4 > 0]

print(b)