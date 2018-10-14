# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import sys


def mk_dir():
    dir_name = input("Введите название создаваемой папки")

    try:
        os.mkdir(dir_name)
        print("Папка " + dir_name + " создана")
    except FileExistsError:
        print("Такая папка уже существует!")


mk_dir()


def del_dir():
    dir_name = input("Введите название папки, которую хотите удалить.")
    try:
        os.rmdir(dir_name)
        print("Папка " + dir_name + " удалена")
    except FileNotFoundError:
        print("Нет такой папки")


del_dir()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def list_dir():
    dirs = [f for f in os.listdir() if os.path.isdir(f)]
    return dirs


print(list_dir())

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

this_file = os.path.basename(sys.argv[0])[:-3]
new_file = this_file + '_copy.py'.strip()
file_path = os.path.abspath(sys.argv[0])
file_read = open(file_path, 'r', encoding='UTF-8')
f = file_read.read()
file_read.close()
new_file_write = open(new_file, 'w', encoding='UTF-8')
new_file_write.write(f)
new_file_write.close()


