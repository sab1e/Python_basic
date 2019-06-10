__author__ = 'Соболев Антон'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
print(f'{"-"*5} Задание-1 {"-"*5}')


def my_round(number, ndigits):
    round_number = float(str(number)[:(2+ndigits)])
    if int(str(number)[2 + ndigits]) > 5:
      round_number += 10**(-ndigits)
    return float(round_number)

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
print(f'{"-"*5} Задание-2 {"-"*5}')


def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)
    left_part = 0
    right_part = 0
    if len(ticket_number) != 6:
      return 'Номер билета должен быть шестизначным'
    for i in range(len(ticket_number)//2):
      left_part += int(ticket_number[i])
      right_part += int(ticket_number[-(i+1)])
    if left_part == right_part:
      return 'Билет счастливый'
    else:
      return 'Билет обычный'

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))