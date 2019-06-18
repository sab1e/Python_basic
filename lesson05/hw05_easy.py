__author__ = 'Соболев Антон'


import os
import sys
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def create_dir(dir_name=None):
    try:
        if dir_name:
            os.mkdir(os.path.join(os.getcwd(), dir_name))
        else:
            dir_name = input('Введите имя папки: ')
            os.mkdir(os.path.join(os.getcwd(), dir_name))
    except FileExistsError:
        print(f'Директория \'{dir_name}\' уже существует')
    except PermissionError:
        print(f'Не хватает прав доступа')
    except Exception:
        print(f'Директория \'{dir_name}\' не создана')
    else:
        print(f'Директория \'{dir_name}\' успешно создана')


def remove_dir(dir_name=None):
    try:
        if dir_name:
            os.rmdir(os.path.join(os.getcwd(), dir_name))
        else:
            dir_name = input('Введите имя папки: ')
            os.rmdir(os.path.join(os.getcwd(), dir_name))
    except FileNotFoundError:
        print(f'Директория \'{dir_name}\' не существует')
    except NotADirectoryError:
        print(f'\'{dir_name}\' не является директорией')
    except PermissionError:
        print(f'Не хватает прав доступа')
    else:
        print(f'Директория \'{dir_name}\' успешно удалена')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def view_dir():
    print('\nCодержимое текущей папки:')
    for el in os.listdir(os.path.join(os.getcwd())):
        print(el)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copy_script():
    file_name = os.path.basename(__file__)
    shutil.copy2(sys.argv[0], os.path.splitext(file_name)[0] + '_copy' + os.path.splitext(file_name)[1])
    print(f'\nФайл {sys.argv[0]} успешно скопирован')


def change_dir(dir_name=None):
    try:
        if dir_name:
            os.chdir(os.path.join(os.getcwd(), dir_name))
        else:
            dir_name = input('Введите имя папки в текущей директории или путь к папке в которую надо перейти '
                             '(../ - для перехода на папку выше или для задания относительного пути):')
            os.chdir(os.path.join(os.getcwd(), dir_name))
    except FileNotFoundError:
        print(f'Директория \'{dir_name}\' не существует')
    except NotADirectoryError:
        print(f'\'{dir_name}\' не является директорией')
    except PermissionError:
        print(f'Не хватает прав доступа')
    else:
        print(f'Вы успешно перешли в \'{os.getcwd()}\'')


if __name__ == '__main__':
    for i in range(1, 10):
        create_dir(f'dir_{i}')

    for i in range(1, 10):
        remove_dir(f'dir_{i}')

    view_dir()

    copy_script()

