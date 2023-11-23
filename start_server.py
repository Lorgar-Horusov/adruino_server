from flask import Flask, request
import json

# Импортируем путь к JSON-файлу из основного скрипта
from main import json_file_path

# Создаем экземпляр Flask
app = Flask(__name__)

# Обработчик POST-запроса по пути '/receive_data'
@app.route('/receive_data', methods=['POST'])
def receive_data():
    # Получаем данные из запроса
    data = request.data.decode('utf-8')
    print(f'Received data: {data}')

    try:
        # Пытаемся открыть JSON-файл и загрузить существующих пользователей
        with open(json_file_path, 'r') as json_file:
            existing_users = json.load(json_file)
    except Exception as e:
        print(f'Error reading file: {e}')

    # Проверяем, есть ли пользователь с переданным ключом
    for user_info in existing_users:
        if data == user_info['key']:
            result = f'User {user_info["user"]}\naccess accept'
            print(result)
            return result

    # Если пользователь не найден, возвращаем 'access denied'
    result = 'access denied'
    print(result)
    return result

# Функция для запуска сервера
def start_server():
    # Запускаем Flask-приложение
    app.run(debug=True, host='0.0.0.0', port=5000)

# Проверяем, является ли данный файл основным исполняемым скриптом
if __name__ == '__main__':
    start_server()
