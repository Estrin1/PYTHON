"""
Задание 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""

import random


def find_number(number, step, list_1, l, r):
    if step > 10:
        return print(f'Количество попыток закончилось: загаданное число = {number}')
    elif r == number:
        return print(f'Загаданное число = {r}')
    mid = (l + r) // 2
    if list_1[mid] < number:
        l = mid
    elif list_1[mid] +1 > number:
        r = mid
    step += 1
    find_number(number, step, list_1, l, r)


number = random.randint(0, 100)
list_1 = [i for i in range(0, 100)]
r = 100
l = 0
step = 1
find_number(number, step, list_1, l, r)
