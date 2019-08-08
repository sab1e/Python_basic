""" OpenWeatherMap (экспорт)

Сделать скрипт, экспортирующий данные из базы данных погоды, 
созданной скриптом openweather.py. Экспорт происходит в формате CSV или JSON.

Скрипт запускается из командной строки и получает на входе:
    export_openweather.py --csv filename [<город>]
    export_openweather.py --json filename [<город>]
    export_openweather.py --html filename [<город>]

При выгрузке в html можно по коду погоды (weather.id) подтянуть
соответствующие картинки отсюда:  http://openweathermap.org/weather-conditions

Экспорт происходит в файл filename.

Опционально можно задать в командной строке город. В этом случае
экспортируются только данные по указанному городу. Если города нет в базе -
выводится соответствующее сообщение.

"""

import csv
import json
import sys
import sqlite3
import os


# вывод справки по экспорту
def export_help():
    print("Экспорт погоды в следующие форматы:")
    print("--csv filename [<город>]")
    print("--json filename [<город>]")
    print("--html filename [<город>]")
    print("Экспорт происходит в файл filename")
    print("Опционально можно задать в командной строке город. "
          "В этом случае экспортируются только данные по указанному городу.")


def read_db(t_name=False):
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM погода")
    weather_data_full = [tuple([cn[0] for cn in cursor.description])]
    if t_name:
        t_name = [t_name]
        cursor.execute("""SELECT * FROM погода WHERE город=?""", (t_name))
        _weather_data = cursor.fetchall()
        if len(_weather_data) > 0:
            weather_data_full.extend((_weather_data))
            return weather_data_full
        else:
            print(f"{t_name[0]} не найден")
            sys.exit()
    else:
        cursor.execute("SELECT * FROM погода")
        _weather_data = cursor.fetchall()
        weather_data_full.extend(_weather_data)
        return weather_data_full


# функция экспорта в csv
def export_csv():
    if not fname:
        print('Необходимо указать имя файла вторым аргуметом')
        return
    path = os.path.join(os.getcwd(), fname)
    if town_name:
        weather_data = read_db(town_name)
    else:
        weather_data = read_db()
    with open(path, "w", encoding='UTF-8', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in weather_data:
            writer.writerow(line)


# функция экспорта в json
def export_json():
    if not fname:
        print('Необходимо указать имя файла вторым аргуметом')
        return
    path = os.path.join(os.getcwd(), fname)
    if town_name:
        weather_data = read_db(town_name)
    else:
        weather_data = read_db()
    weather_data_json = []
    for i in range(1, len(weather_data)):
        weather_data_json.append({weather_data[0][0]: weather_data[i][0], weather_data[0][1]: weather_data[i][1],
                                  weather_data[0][2]: weather_data[i][2], weather_data[0][3]: weather_data[i][3],
                                  weather_data[0][4]: weather_data[i][4]})

    with open(path, "w", encoding="UTF-8") as json_file:
        json.dump(weather_data_json, json_file, ensure_ascii=False)


def export_html():
    pass

print('sys.argv = ', sys.argv)

do = {
    "--help": export_help,
    "--csv": export_csv,
    "--json": export_json,
    "--html": export_html
}

try:
    fname = sys.argv[2]
except IndexError:
    fname = None

try:
    town_name = ' '.join(sys.argv[3:])
except IndexError:
    town_name = None

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
