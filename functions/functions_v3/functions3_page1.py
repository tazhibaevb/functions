# 1) Написать lambda которая принимает 3 параметра и умножает все параметры между собой.
# Функция должна вернуть строку: "Объём бассейна " и значение которое получилось.

# f = lambda a, b, c: f'Обьем бассейна: {a * b * c}'
# print(f(1, 2, 3))


# 2) Написать lambda которая получает сколько дней ПРОШЛО с нового года как параметр
# и говорит пользователю сколько дней ОСТАЛОСЬ до нового года.

# a = input('сколько дней прошло с нового года?: ')
# f = lambda a: f'до нового года осталось: {365 - a} дня'
# print(f(2))


# 3) Напишите программу которая выводит только нечётные числа с помощью рекурсии.

# def rec():
#     for x in range(50):
#         if x % 2 == 0:
#             print(x)
#     rec()
#
# print(rec())


# 4) Напишите функцию которая принимает SET и рекурсивно удаляет оттуда по одному элементу при запуске.

# my_set = {'123', True, 'asdad', 21, 22, }
#
#
# def dltr(a):
#     print(a.pop())
#     if len(my_set) == 0:
#         print('все элементы удалены')
#     dltr(a)
#
#
# dltr(my_set)
