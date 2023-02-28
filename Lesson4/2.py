# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
N = int(input('Введите натуральное число: '))
list1 = []
i = 2
flag = True
while flag:
    if N % i == 0:
        list1.append(i)
        N = N / i
    else:
        i += 1
    if N <= 1:
        flag = False
    if len(list1) == 0 and i == N:
        print("Число делится только на себя")
        break

print(list1)