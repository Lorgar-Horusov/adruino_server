from flask import Flask, request
import json

from main import json_file_path

app = Flask(__name__)


@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.data.decode('utf-8')
    print(f'Received data: {data}')

    try:
        with open(json_file_path, 'r') as json_file:
            existing_users = json.load(json_file)
    except Exception as e:
        print(f'Error reading file: {e}')

    for user_info in existing_users:
        if data == user_info['key']:
            result = f'User {user_info["user"]}\naccess accept'
            print(result)
            return result

    result = 'access denied'
    print(result)
    return result


def start_server():
    app.run(debug=True, host='0.0.0.0', port=5000)


if __name__ == '__main__':
    start_server()
