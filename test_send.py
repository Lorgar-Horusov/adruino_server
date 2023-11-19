import requests
from requests.exceptions import RequestException

url = 'http://127.0.0.1:5000/receive_data'


data_to_send = "7B A9 D2 64"

try:
    response = requests.post(url, data=data_to_send)
    if response.status_code == 200:
        print("Ответ от сервера:", response.text)
    else:
        print(f"Ошибка при отправке запроса. Статус код: {response.status_code}")
except RequestException as e:
    print(f'Ошибка при соединении с сервером. Проверьте состояние сервера или сетевое соединение. Статус:\n'
          f'{e}')