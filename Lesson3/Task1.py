
# 1. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите два варианта решения: через list и через dict.
#
# Пример:
# Введите номер месяца: 10
# Результат через список: Осень
# Результат через словарь: Осень
"""
x = int(input("Введите число от 1 до 12: "))
list_season = ["winter", "spring", "summer", "autumn"]
if x <= 3:
    print(list_season[0])
elif 3 <= x <= 6:
    print(list_season[1])
elif 6 <= x <= 9:
    print(list_season[2])
elif 9 <= x <= 12:
    print(list_season[3])
else:
    print('Введены не корректные данные')
"""
x = int(input("Введите число от 1 до 12: "))
dict_season = {1: "winter", 2: "winter", 3: "winter", 4: "spring", 5: "spring", 6: "spring",
               7: "summer", 8: "summer", 9: "summer", 10: "autumn", 11: "autumn", 12: "autumn"}
print(dict_season[x])

