"""
== OpenWeatherMap ==

OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.

    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID,
    используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys

        Ключ имеет смысл сохранить в локальный файл, например, "app.id"


== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz

    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка
     (воспользоваться модулем gzip
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)

    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}


== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}


== Сохранение данных в локальную БД ==
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.


При работе с XML-файлами:

Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""
import os
import sqlite3
import json
import requests
import re


class CityList():
    def __init__(self, path):
        self.data_str = self.city_list_load(path)
        self.country_list = []
        self.city_id = []

    def city_list_load(self, path):
        with open(path, 'r', encoding='UTF-8') as file_city:
            data_str = file_city.read()
            return data_str

    # метод вывода списка всех стран из базы
    # страны ищем регулярным выражением, с помощью кортежа убираем повторы
    # выводим на экран по 10 стран, для удобства
    def print_country_list(self):
        pat_country = r'"country": "(\w*)"'
        self.country_list = list(set(re.findall(pat_country, self.data_str)))
        self.country_list.sort()
        for i in range(-10, len(self.country_list), 10):
            print(self.country_list[i + 10:i + 20])

    # метод поиска id городов в выбранной стране
    # после получения ввода, проверяем есть ли страна в списке всех сран
    # при успешной проверки, с помощью регулярного выражения, ищем записи с указанной страной
    # и при совпадении собираем id городов
    # если введеной страны нет в списке, повторяем цикл еще раз
    def get_city_id(self):
        while True:
            self.print_country_list()
            country = input('Введите страну: ').upper()
            if country in self.country_list:
                pattern = r'"id": (\w*),\s*"name": "[\w*\s*]*",\s*"country": "' + country + r'"'
                self.city_id = re.findall(pattern, self.data_str)
                break
            else:
                print('Введеной страны не в списке. Попробуйте еще раз')

    #
    def get_weather_in_country(self):
        data_req = {"id": "", "units": "metric", "appid": "f6d4e8a7d8b134fdf9bb8540c948ffda"}
        for cid in self.city_id:
            data_req['id'] = cid
            response = requests.get('http://api.openweathermap.org/data/2.5/weather', params=data_req)
            weather_by_city = json.loads(response.text)
            self.write_in_db(weather_by_city)

    def write_in_db(self, weather):
        with sqlite3.connect("weather.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS погода
                          (id_города integer primary key, город text, дата integer,
                           температура integer, id_погоды integer)
                           """)
            weather_id = [int(weather['id'])]
            cursor.execute("""SELECT * FROM погода WHERE id_города=?""", (weather_id))
            if len(cursor.fetchall()) > 0:
                cities_weather_upd = [int(weather['dt']), int(weather['main']['temp']),
                                      int(weather['weather'][0]['id']), int(weather['id'])]
                cursor.execute("""UPDATE погода SET дата=?, температура=?, id_погоды=? 
                                WHERE id_города=?""", (cities_weather_upd)
                               )
            else:
                cities_weather = [(int(weather['id']), weather['name'], int(weather['dt']),
                                   int(weather['main']['temp']), int(weather['weather'][0]['id']))]
                cursor.executemany("INSERT INTO погода VALUES(?, ?, ?, ?, ?)", cities_weather)



path = os.path.join('city.list.json')
city = CityList(path)
city.get_city_id()
city.get_weather_in_country()



