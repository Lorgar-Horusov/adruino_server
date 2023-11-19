import json
import os
import re
import pandas as pd
import subprocess
import sys

from tabulate import tabulate

json_file_path = 'users.json'


def add_user(user='', key=''):
    if len(user) > 16:
        print("max 16 symbols")
        return
    if not re.match("^[A-Za-z ]*$", user):
        print('only latn symbols')
        return

    try:
        with open(json_file_path, 'r') as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        existing_data = []

    for entry in existing_data:
        if entry.get("key") == key:
            print("Данный ключ уже записан.")
            return

    new_user_entry = {
        'user': user,
        'key': key
    }
    existing_data.append(new_user_entry)

    try:
        with open(json_file_path, 'w') as json_file:
            json.dump(existing_data, json_file, indent=2)
            print("done")
    except Exception as e:
        print(f"Ошибка при добавлении пользователя в JSON-файл: {e}")


def user_list():
    try:
        with open(json_file_path, 'r') as json_file:
            user_lists = json.load(json_file)
    except Exception as e:
        print(f'Ошибка пр чтении файла {e}')

    print_list = pd.DataFrame(user_lists)
    print(tabulate(print_list, headers='keys', tablefmt='mixed_grid'))


def menu(choose):
    choose = choose.lower().strip()
    if choose in ['1', 'start', 's']:
        subprocess.Popen([sys.executable, 'start_server.py', 'run'], creationflags=subprocess.CREATE_NEW_CONSOLE)

    elif choose in ['2', 'list', 'l']:
        user_list()
        os.system('pause')

    elif choose in ['3', 'add', 'a']:
        add_user(user=input('user name'), key=input('key'))

    elif choose in ['3', 'exit', 'e']:
        exit()

    else:
        print('Command not found')


def main():
    menu_list = [["1) Start", "Use to run server"],
                 ["2) List", "Use to print users"],
                 ["3) Add", "Use to add new user"],
                 ["0) Exit,", "Use to exit"]]
    while True:
        print('=======================================')
        print(tabulate(menu_list, tablefmt='fancy_grid'))
        print('=======================================')
        choose = input("[>>] Select: ")
        menu(choose)


if __name__ == '__main__':
    main()
