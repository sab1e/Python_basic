__author__ = 'Соболев Антон'

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

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3

import os, sys, shutil

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not own_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), own_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(own_name))
    except FileExistsError:
        print('директория {} уже существует'.format(own_name))
    except PermissionError:
        print(f'Не хватает прав доступа')


def ping():
    print("pong")


def copy_file():
    if not own_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        dir_path = os.path.join(os.getcwd(), own_name)
        file_name = os.path.basename(dir_path)
        file_copy_name = os.path.splitext(file_name)[0] + '_copy' + os.path.splitext(file_name)[1]
        if not os.path.isfile(file_copy_name):
            shutil.copy2(dir_path, file_copy_name)
        else:
            raise FileExistsError
    except FileExistsError:
        print(f'Файл {file_copy_name} уже существует')
    except FileNotFoundError:
        print(f'Файл {own_name} не существует')
    except PermissionError:
        print(f'Не хватает прав доступа')
    else:
        print(f'Файл {own_name} успешно скопирован')


def remove_file():
    if not own_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        dir_path = os.path.join(os.getcwd(), own_name)
        os.remove(dir_path)
    except FileNotFoundError:
        print(f'Файл {own_name} не существует')
    except PermissionError:
        print(f'Не хватает прав доступа')
    else:
        print(f'Файл {own_name} успешно удален')


def change_dir():
    if not own_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    try:
        dir_path = os.path.join(os.getcwd(), own_name)
        os.chdir(dir_path)
    except FileNotFoundError:
        print(f'Директория \'{dir_path}\' не существует')
    except NotADirectoryError:
        print(f'\'{dir_path}\' не является директорией')
    except PermissionError:
        print(f'Не хватает прав доступа')
    else:
        print(f'Вы успешно перешли в \'{os.getcwd()}\'')


def full_path():
    print(os.getcwd())


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": remove_file,
    "cd": change_dir,
    "ls": full_path
}

try:
    own_name = sys.argv[2]
except IndexError:
    own_name = None

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