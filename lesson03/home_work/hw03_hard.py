# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


def fraction_func():
    s = "-1 5/6 - -2 4/7"
    # s = input("Введите выражение в формате: n x/y +(-) n x/y ")
    operation = oper(s)
    lst = list(s.split())  # lst -> ['-1', '5/6', '-', '-2', '4/7']
    sign_index = lst.index(operation)  # '-'
    first_num = lst[0:sign_index]  # first_num -> ['-1', '5/6']
    second_num = lst[sign_index + 1: len(lst)]  # second_num -> ['-2', '4/7']

    print(first_num)
    print(second_num)

fraction_func()


def oper(s):
    operation = "+"
    if s.find("+") == -1:
        operation = "-"
    return operation


def denom(a):
    fract_num = a[1].Split('/')
    return int(fract_num[1])


def all_numenator(a):
    int_num = a[0]
    fract_num = a[1].Split('/')
    all = int(int_num) * int(fract_num[0])
    return all


def fraction(operation, a, b):
    """
    :param operation: "+", "-"
    :param a: ['n',  'x/y'] -> ['-1', '5/6']
    :param b: ['n',  'x/y'] -> ['-2', '4/7']
    :return: n x/y
    """
    a_num = all_numenator(a)
    a_den = denom(a)
    b_num = all_numenator(b)
    b_den = denom(b)
    ab_num = 0
    ab_den = 0

    if a_den == b_den:
        if operation == '+':
            ab_num = a_num + b_num
            ab_den = a_den
        elif operation == '-':
            ab_num = a_num - b_num
            ab_den = a_den
        else:
            print ('Error of operation')
    else:
        ab_den = a_den * b_den
        if operation == '+':
            ab_num = a_num * b_den + b_num * a_den
        elif operation == '-':
            ab_num == a_num * b_den - b_num * a_den
        else:
            print ('Error of operation')

    if










# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
