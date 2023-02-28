"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
str(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_ = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return (f'{self.name} {self.surname}')
    def get_total_income(self):

        return self._income_['wage'] +  self._income_['bonus']

    def __str__(self):
        return '({},{},{})'.format(self.name, self.surname, self.get_total_income())

a = Position('Анто', 'Виноградов', 'топ менеджер', 130, 50 )
print(a)
print(f'Полное имя {a.get_full_name()}  общий заработок с учетом бонусов: {a.get_total_income()}')

