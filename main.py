import json
import os
import re
import pandas as pd
import subprocess
import sys
from tabulate import tabulate

# Путь к JSON-файлу для хранения данных о пользователях
json_file_path = 'users.json'

# Функция для добавления нового пользователя
def add_user(user='', key=''):
    # Проверяем, чтобы имя пользователя было на латинице и не превышало 16 символов
    if len(user) > 16:
        print("max 16 symbols")
        return
    if not re.match("^[A-Za-z ]*$", user):
        print('only latin symbols')
        return
    
    try:
        # Пытаемся открыть существующий JSON-файл и загрузить данные
        with open(json_file_path, 'r') as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        # Если файл не найден, создаем новый список
        existing_data = []

    # Проверяем, не существует ли уже пользователь с данным ключом
    for entry in existing_data:
        if entry.get("key") == key:
            print("Данный ключ уже записан.")
            return

    # Создаем новую запись о пользователе
    new_user_entry = {
        'user': user,
        'key': key
    }
    existing_data.append(new_user_entry)

    try:
        # Пытаемся записать обновленные данные обратно в JSON-файл
        with open(json_file_path, 'w') as json_file:
            json.dump(existing_data, json_file, indent=2)
            print("done")
    except Exception as e:
        print(f"Ошибка при добавлении пользователя в JSON-файл: {e}")

# Функция для отображения списка пользователей
def user_list():
    try:
        # Пытаемся открыть JSON-файл и загрузить данные
        with open(json_file_path, 'r') as json_file:
            user_lists = json.load(json_file)
    except Exception as e:
        print(f'Ошибка при чтении файла {e}')

    # Отображаем список пользователей с использованием библиотеки pandas и tabulate
    print_list = pd.DataFrame(user_lists)
    print(tabulate(print_list, headers='keys', tablefmt='mixed_grid'))

# Функция для обработки выбора в меню
def menu(choose):
    choose = choose.lower().strip()
    if choose in ['1', 'start', 's']:
        # Запуск сервера в новой консоли
        subprocess.Popen([sys.executable, 'start_server.py', 'run'], creationflags=subprocess.CREATE_NEW_CONSOLE)
    elif choose in ['2', 'list', 'l']:
        # Вывод списка пользователей
        user_list()
        os.system('pause')
    elif choose in ['3', 'add', 'a']:
        # Добавление нового пользователя
        add_user(user=input('user name'), key=input('key'))
    elif choose in ['3', 'exit', 'e']:
        # Выход из программы
        exit()
    else:
        print('Command not found')

# Основная функция для запуска программы
def main():
    # Меню программы
    menu_list = [["1) Start", "Use to run server"],
                 ["2) List", "Use to print users"],
                 ["3) Add", "Use to add new user"],
                 ["0) Exit,", "Use to exit"]]
    while True:
        # Выводим меню и ожидаем выбор пользователя
        print('=======================================')
        print(tabulate(menu_list, tablefmt='fancy_grid'))
        print('=======================================')
        choose = input("[>>] Select: ")
        menu(choose)

# Проверяем, является ли данный файл основным исполняемым скриптом
if __name__ == '__main__':
    main()
