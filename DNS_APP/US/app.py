from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')

    if not all([hostname, fs_port, number, as_ip, as_port]):
        return 'Bad Request', 400

 
    params = {'name': hostname, 'type': 'A'}
    response = requests.get(f'http://{as_ip}:{as_port}/dns-query', params=params)
    if response.status_code != 200:
        return ' Query Failed', 500
    ip_address = response.json()['value']

    
    response = requests.get(f'http://{ip_address}:{fs_port}/fibonacci', params={'number': number})
    if response.status_code != 200:
        return ' Query Failed', 500
    fibonacci_value = response.text

    return fibonacci_value, 200

if __name__ == '__main__':
    app.run(port=8080)