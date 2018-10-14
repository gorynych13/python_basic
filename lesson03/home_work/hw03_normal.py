# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
import math


def fibonacci(n, m):
    fib = list()

    def fib_index(num):
        """
        Нахочим число фибоначи по номеру элемента
        :param num: номер элемента
        :return: fib: число фибоначи
        """
        f_last = 1
        f_prev = 0
        fib_num = 1
        if num == 1:
            fib_num = 1
        else:
            for i in range(1, num):
                fib_num = f_last + f_prev
                f_prev = f_last
                f_last = fib_num
        return fib_num

    for i in range(n, m + 1):
        fib.append(fib_index(i))
    return fib


print(fibonacci(3, 5))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    s = origin_list
    not_sorted = True
    count = len(s)

    while not_sorted:
        not_sorted = False

        for i in range(1, count):
            if s[i] < s[i - 1]:
                temp = s[i]
                s[i] = s[i - 1]
                s[i - 1] = temp
                not_sorted = True
    return s


lst = sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
print(lst)


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def my_filter(func, elements):
    s = elements
    count = len(s)
    dlt = []
    for i in range(count):
        if func(s[i]):
            continue
        else:
            dlt.append(s[i])

    for j in range(len(dlt)):
        s.remove(dlt[j])
    return s


my_fil = my_filter(lambda x: x > 0, lst)
my_fil1 = my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(my_fil)
print(my_fil1)
# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
#                   a
#          A1______________A2
#         /               /
#        /               /
#     d /               / b
#      /               /
#   A4/_______________/A3
#           c
# если a == c and b == d => параллерограм

# Дано
a1 = [2, 4]
a2 = [5, 4]
a3 = [4, 1]
a4 = [1, 1]


def line_length(a1, a2):
    length_line = math.sqrt((a1[0] - a2[0]) ** 2 + (a1[1] - a2[1]) ** 2)
    return length_line


def is_parallerogram(a1, a2, a3, a4):
    a = line_length(a1, a2)
    b = line_length(a2, a3)
    c = line_length(a3, a4)
    d = line_length(a4, a1)
    if a == c and b == d:
        return True
    else:
        return False


print(is_parallerogram(a1, a2, a3, a4))