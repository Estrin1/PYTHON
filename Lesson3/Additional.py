"""
1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

*Пример:*

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""
import math

# from functools import reduce
#
# list_1 = list(map(int, input("Введите числа через пробел: ").split()))
# a = list(filter(lambda item: (list_1.index(item) % 2 != 0), list_1))
# d = reduce(lambda c, b: c + b, a)
# print(d)
"""
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй 
и предпоследний и т.д.
Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""


# list_1 = list(map(int, input("Введите числа через пробел: ").split()))
# list_2 = list()
# length_list = len(list_1)
# for i in range(length_list//2):
#     a = list_1[i] * list_1[len(list_1)-i-1]
#     list_2.append(a)
# print(list_2)
""""

Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""
# def fractional_part(list_1):
#     list_2 = list()
#     for el in list_1:
#         list_2.append(round(el - int(el), 3))
#     return list_2
#
# list_3 = list(map(float, input('введите список через пробел: ').split()))
# list_4 = list()
# list_4 = fractional_part(list_3)
# print(max(list_4) - min(list_4))

def another_calculus_system(a):
    list_2 = list()
    while a >= 1:
        list_2.append(a % 2)
        a = a // 2
    return print(list_2)


b = 45
list1 = list()

list1 = another_calculus_system(b)
list2 = list1[::-1]
print(list2)