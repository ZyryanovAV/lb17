#Выполнить индивидуальное задание 1 лабораторной работы 13, оформив все классы программы
#в виде отдельного пакета. Разработанный пакет должен быть подключен в основную программу с
#помощью одного из вариантов команды import . Настроить соответствующим образом
#переменную __all__ в файле __init__.py пакета. Номер варианта уточнить у преподавателя.
#Вариант 8

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from pak_1 import Payment


if __name__ == '__main__':
    p_1 = Payment(Name="Михаил", oklad=35000, year=2001, percent=15, Worked_days=20, working_day=24)
    p_2 = Payment(Name="Иван", oklad=35000, year=2003, percent=10, Worked_days=23, working_day=24)

    print(f"{p_1}")
    print(f"Выданная сумма: {round(p_1)}\n")

    print(f"oklad_1 < oklad_2: {p_1 < p_2}")
    print(f"workingDays1 > workingDays2: {p_1 > p_2}")
    print(f"percent_1 != percent_2: {p_1 != p_2}")
    print(f"daysWorked_1 == daysWorked_2: {p_1 == p_2}")
    print(f"Experience_1 >= Experience_2: {p_1 >= p_2}")
    print(f"handAmount_1 <= handAmount_2: {p_1 <= p_2}\n")

    print(f"Разница в заработной плате: {p_1 / p_2}")
    print(f"Произведение процентов: {p_1 * p_2}")
    print(f"Добавленные рабочие дни: {p_1 + p_2}")
    print(f"Разница в отработанных днях: {p_1 - p_2}")