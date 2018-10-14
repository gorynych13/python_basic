# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.
import os
import sys
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл (запросить подтверждение операции)")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную \n "
          "для перехода на уровень выше введите '..'")
    print("ls - отображение полного пути текущей директории")





def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def del_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.join(os.getcwd(), file_name)
    try:
        os.remove(file_path)
        print("Файл {} удалён.".format(file_name))
    except FileExistsError:
        print("Нет файла {}". format(file_name))


def copy_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    this_file = os.path.basename(sys.argv[0])[:-3]
    this_end_file = os.path.basename(sys.argv[0])[-3:]
    new_file = this_file + '_copy'.strip() + this_end_file.strip()
    file_path = os.path.join(os.getcwd(), file_name)

    file_read = open(file_path, 'r', encoding='UTF-8')
    f = file_read.read()
    file_read.close()
    new_file_write = open(new_file, 'w', encoding='UTF-8')
    new_file_write.write(f)
    new_file_write.close()


def list_file():
    file_path = os.getcwd()
    print(file_path)


def change_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    current_dir = os.getcwd()
    cd_name = dir_name

    if cd_name == '..':
        new_dir = os.path.split(current_dir)[0]
    else:
        new_dir = os.path.join(current_dir, cd_name)
    try:
        os.chdir(new_dir)
        print("Переход совешен успешно")
        print()
    except FileNotFoundError:
        print("Нет такой папки")


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "rm": del_file,
    "cp": copy_file,
    "ls": list_file,
    "cd": change_dir
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
