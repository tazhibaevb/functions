# 1) Создайте функцию которая которая берёт лист делит его пополам и обе стороны
# разворачивает в противоположную сторону. Пример:
# Оригинальный Лист:
# list_1 = ['name', 'age', '1', '19']
# Изменённый Лист:
# list_1 = ['age', 'name', '19', '1']

# list_1 = ['name', 'age', '1', '19']
#
#
# def rev_list():
#     print(list(reversed(list_1[:len(list_1) // 2])) + list(reversed(list_1[len(list_1) // 2:])))
#     b = list(reversed(list_1[len(list_1) // 2:]))
#     a = list(reversed(list_1[:len(list_1) // 2]))
#     print(a + b)
#
#
# rev_list()


# 2) Создайте функцию которая генерирует 10 чисел Фибоначчи:
# 1,1,2,3,5,8,13,21,34,...

# def fib(n):
#    a, b = 0, 1
#    for __ in range(n):
#       yield a
#       a, b = b, a + b
#
#
# print(list(fib(10)))


# 3) Создайте функцию сложения, затем функцию вычитания двух чисел...
# Создайте 3-ю функцию которая вызывает первые 2 внутри себя.

# def add(q, w):
#     return q + w
#
#
# a = add(2, 2)
# print(a)
#
#
# def minus(c, d):
#     return c - d
#
#
# b = minus(3, 3)
# print(b)
#
#
# def tri():
#     return a, b
#
#
# print(tri())