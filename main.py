"""Код, реализующий тестовое задание"""
import re
from tinydb import TinyDB, Query
import ehttp

# Регулярки для валидации
phone_regex = re.compile(r'^\+7 \d{3} \d{3} \d{2} \d{2}$')
date_regex = re.compile(r'^(\d{4}-\d{2}-\d{2})$|^(\d{2}\.\d{2}.\d{4})$')
email_regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

server = ehttp.Server(
    host="127.0.0.1",
    port=8000
)

def validate_phone(phone:str) -> bool:
    "Функция для проверки валидности номера телефона"
    if phone_regex.match(phone):
        return True
    return False

def validate_date(date:str) -> bool:
    "Функция для проверки валидности даты"
    if date_regex.match(date):
        return True
    return False

def validate_email(email:str) -> bool:
    "Функция для проверки валидности почты"
    if email_regex.match(email):
        return True
    return False

def get_type(data:str) -> str:
    "Функция для определения типа данных"
    if validate_date(data):
        return 'date'
    if validate_phone(data):
        return 'phone'
    if validate_email(data):
        return 'email'
    return 'text' # по ТЗ текст это все, что не прошло валидацию

db = TinyDB('db.json')
table = db.table('templates')
Template = Query() # Объект для поиска в БД

@server.bind('/get_form')
def get_form(req: ehttp.Request):
    "Метод для получения формы по параметрам"
    print(req.data)
    possible:list = [] # тут будут храниться все варианты с подходящими ключами
    if req.data:
        for key, value in req.data.items():
            _type = get_type(value)
            req.data[key] = _type # переназначение для ответа в случае провала
            res = table.search(Template[key] == _type)

            # добавление вариантов
            for r in res:
                if dict(r) not in possible:
                    possible.append(dict(r))

        data_items = req.data.items()
        for pos in possible:
            name = pos.pop('name') # Цбираем имя из словаря чтоб поиск проверка корректно работала
            if pos.items() <= data_items: # проверка, что все ключи подходят
                return name

    return req.data # в случае провала всех проверок возвращаем ключи и их типы данных

server.start()
db.close()
