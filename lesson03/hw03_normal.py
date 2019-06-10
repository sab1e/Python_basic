__author__ = 'Соболев Антон'


# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

print(f'{"-"*5} Задание-1 {"-"*5}')


def fibonacci(n, m):
	fib = [1, 1]
	for i in range(m):
		fib.append(fib[i] + fib[i + 1])
	return fib[n-1:m]
	
print(fibonacci(6, 10))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

print(f'\n{"-"*5} Задача-2 {"-"*5}')


def sort_to_max(origin_list):
	for i in range(len(origin_list)):
		for j in range(len(origin_list) - i - 1):
			if origin_list[j] > origin_list[j + 1]:
				replace_el = origin_list[j]
				origin_list[j] = origin_list[j+1]
				origin_list[j+1] = replace_el
	return origin_list 

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
print(f'\n{"-"*5} Задача-3 {"-"*5}')

def my_filter(func, origin_list):
	filtred_list = []
	for el in origin_list:
		if func(el) == True:
			filtred_list.append(el)
	return filtred_list

mixed = ['мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'просо', 'просо', 'мак']
print(list(filter(lambda x: x == 'мак', mixed)))

a = [1, 2, 3, 4, 5, 6]
print(list(my_filter(lambda x : x % 2 == 0, a)))

dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
print(list(my_filter(lambda x : x['name'] == 'python', dict_a)))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

print(f'\n{"-"*5} Задача-4 {"-"*5}')

import math

def len_d(point_1, point_2):
	d = math.sqrt((point_2[0] - point_1[0])**2 + (point_2[1] - point_1[1])**2)
	return d

a1 = [100, 100]
a2 = [150, 200]
a3 = [350, 200]
a4 = [300, 100]

if len_d(a1, a2) == len_d(a3, a4) and len_d(a2, a3) == len_d(a4, a1):
	print('Точки А1, А2, А3, А4 являются вершинами параллелограмма.')
else:
	print('Точки А1, А2, А3, А4 не являются вершинами параллелограмма.')
