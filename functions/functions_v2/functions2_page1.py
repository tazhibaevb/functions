# 1) Создайте 4 функции: add(), substract(), multiply(), divide() которые будут
# принимать по 2 аргумента и возвращать результат: сложения, вычитания, умножения и деления.

# def add(salary1, salary2):
#     summ = salary1 + salary2
#     return summ
#
# result = add(12,23)
# print(result)

# def substract(salary1, salary2):
#     dif = salary1 - salary2
#     return dif
#
# result = substract(12,23)
# print(result)

# def multiply(salary1, salary2):
#     mltply = salary1 * salary2
#     return mltply
#
# result = multiply(12,23)
# print(result)

# def divide(salary1, salary2):
#     dvd = salary1 / salary2
#     return dvd
#
# result = divide(12,23)
# print(result)


# 2) Написать Функцию которая принимает предложение как аргумент, считает количество
# букв и возвращает сколько символов он ввёл. НЕ ИСПОЛЬЗОВАТЬ функцию len()

# a = input('введите предложение: ')
#
# def counter(a):
#     i = 0
#     count1 = 0
#     count2 = 0
#     count3 = 0
#     while i < len(a):
#         if a[i] in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЬЫЭЮЯабвгдеёжзийклмнопрстуфхцчшщъььыэюя':
#             count1 += 1
#         elif a[i] in 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm':
#             count2 += 1
#         elif a[i] in '1234567890-=!@#$%^&*()_+"№;:?*=-/,.<>{}[]':
#             count3 += 1
#
#         i += 1
#     print('Вы ввели букв: ', count1 + count2, 'Вы ввели символов: ', count3)
#
# counter(a)


# 3) Напишите функцию которая принимает 2 Dictionary и добавляет втрорую Dictionary к первой.

# def test(**kwargs):
#     g = {}
#     for i in kwargs.keys():
#         g.update(kwargs[i])
#     return g
#
#
# print(test(dict={'qw': 1, 'wq': 2}, dict2={'er': 1, 're': 2}))


# 4) Напишите функцию которая спрашивает у вас чтобы вы хотели заказать покушать и выпить.
# А затем записывает это всё в файл на рабочем столе menu.txt

# def menu():
#     a = input('Закажите покушать и попить: ')
#     with open('C:/Users/99655/Desktop/menu.txt', 'w') as file:
#         file.write(a)
#
#
# menu()


# 5) Создайте функцию которая принимает слово и создаёт файл с таким именем в той же
# директории, где был запущен Ваш .py файл.

# def creator():
#     a = input('введите имя файла и формат: ')
#     b = open(a, 'w')
#     b.close()
#
#
# creator()
