import requests
from requests.exceptions import RequestException

# URL сервера, на который отправляется POST-запрос
url = 'http://127.0.0.1:5000/receive_data'

# Данные для отправки на сервер (ваш пример - строка "7B A9 D2 64")
data_to_send = "7B A9 D2 64"

try:
    # Отправляем POST-запрос на сервер
    response = requests.post(url, data=data_to_send)

    # Проверяем успешность запроса (статус код 200 означает успешный запрос)
    if response.status_code == 200:
        print("Ответ от сервера:", response.text)
    else:
        print(f"Ошибка при отправке запроса. Статус код: {response.status_code}")

except RequestException as e:
    # Обрабатываем исключение, если произошла ошибка при отправке запроса
    print(f'Ошибка при соединении с сервером. Проверьте состояние сервера или сетевое соединение. Статус:\n{e}')
