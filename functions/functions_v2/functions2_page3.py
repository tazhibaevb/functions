# 1) Напишите функцию которая принимает 2 аргумента. Эти аргументы могут быть
# любого типа данных но функция должна Вам вернуть эти аргументы как тип данных List

# def fun(first, second):
#     l = []
#     l.append(first)
#     l.append(second)
#     print(l)
#
#
# fun(first=23, second=234)


# 2) Напишите функцию которая спрашивает у пользователя число и выводит ему на экран
# именно столько строк самой себя как текст.

# n = int(input('Введите число: '))
#
# def fun1(n):
#     b = str(n) * n
#     return b
#
# print(fun1(n))


# 3) Создайте функцию которая принимает Имя пользователя и его зарплату и возвращает
# это строкой как: ИМЯ - ЗАРПЛАТА. Если в функции не была указана зарплата - подставьте её сами.
# Значение по умолчанию - 5000.

# name = input('Введите имя: ')
# salary = input('Введите зарплату: ')
#
#
# def fun2(salary=5000):
#     print(f'{name} {salary}')
#
#
# fun2()


# 4) Напишите функцию которая спрашивает число N и генерирует вам List состоящий из N разных элементов.
# from random import randrange
#
#
# def fun3():
#     a = int(input('Введите число: '))
#     count = 0
#     lst = []
#     while a != count:
#         b = randrange(100)
#         lst.append(b)
#         count += 1
#     print(lst)
#
#
# fun3()

