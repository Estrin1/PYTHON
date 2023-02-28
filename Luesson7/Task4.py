"""
Задание 4.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""
import random


import numpy


class Matrix:

    def __init__(self, matrix_1, matrix_2, matrix_3):
        self.matrix_1 = matrix_1
        self.matrix_2 = matrix_2
        self.matrix_3 = matrix_3
    def __str__(self):
         return '\n'.join(map(str, self.matrix_3))

    def __add__(self, matrix_1, matrix_2, matrix_3):
        for i in range(len(self.matrix_1)):
            for j in range(len(self.matrix_2)):
                matrix_3[i][j] = self.matrix_1[i][j] + self.matrix_2[i][j]
        return matrix_3


list_1 = [[random.randint(1, 99) for i in range(2, 5)] for j in range(2, 5)]
list_2 = [[random.randint(1, 99) for i in range(2, 5)] for j in range(2, 5)]
matrix_3 = [[i for i in range(2, 5)] for j in range(2, 5)]
print(f'{list_1} \n {list_2} \n')
a = Matrix(list_1, list_2, matrix_3)
a.__add__(list_1, list_2, matrix_3)
print(a)




