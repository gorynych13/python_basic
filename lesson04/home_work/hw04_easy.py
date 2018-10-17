# Все задачи текущего блока решите с помощью генераторов списков!

import random

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]


lst_1 = [random.randint(-15, 15) for _ in range(20)]
print(lst_1)

lst_2 = [el*el for el in lst_1]
print(lst_2)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruit1 = ['orange', 'apple', 'grapefruit', 'melon', 'strawberry']
fruit2 = ['raspberry', 'blueberry', 'mango', 'apple', 'orange']
fruit3 = [el for el in fruit1 if el in fruit2]
print(fruit3)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

lst = [random.randint(-1000, 1000) for _ in range(20)]
lst_edit = [el for el in lst if el % 3 == 0 and el > 0 and el%4 != 0]
print(lst)
print(lst_edit)
