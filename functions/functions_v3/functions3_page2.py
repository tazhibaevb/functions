# 1) Напишите функцию которая генерирует 100 рандомных чисел в диапазоне от 10 до 50 и возвращает их в листе.
# Напишите ДЕКОРАТОР для этой функции которая удалит все дубликаты в первой функции и вернёт всё так же лист.

# from random import choices
#
# def dcrtr(func):
#     def wrapper():
#         s = set(func())
#         return list(s)
#     return wrapper
#
#
# @dcrtr
# def rndm():
#     b = choices(range(10, 50), k=100)
#     return list(b)
#
# print(rndm())


# 2) Напишите функцию которая спрашивает у пользователя login и password.
# Напишите декоратор который шифрует эти данные и возвращает вам зашифрованные данные.
# (Можете воспользоваться функцией ord и char, можете загуглить...)

# def get_log_par():
#     alfavit =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИ' \
#                'ЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
#     smeshenie = 2
#     login = input("введите логин : ").upper()
#     password = input("введите пароль : ").upper()
#     new_login = ''
#     new_password = ''
#
#     for i in login:
#         mesto = alfavit.find(i)
#         new_mesto = mesto + smeshenie
#         if i in alfavit:
#             new_login += alfavit[new_mesto]  # Задаем значения в итог
#         else:
#             new_login += i
#
#     for p in password:
#         mesto = alfavit.find(p)
#         new_mesto = mesto + smeshenie
#         if p in alfavit:
#             new_password += alfavit[new_mesto]  # Задаем значения в итог
#         else:
#             new_password += p
#
#     print('зашифрованный логин: ', new_login,'зашифрованный пароль: ', new_password)
# get_log_par()


# 3) Создайте lambda функцию которая принимает одно число и возвращает это число умноженное на 1.185.
# Вам дан список  пройдите по списку и примените функцию к каждому числу.

# my_lst = [1745345,98726,439872634,7312,64872,123687126,9312,4124,231,3123,34,3453]
#
# print(list(map(lambda x: x*1.85, my_lst)))
