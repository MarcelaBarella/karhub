import os
import json
import requests


FULL_NAME = os.environ['FULL_NAME']
EMAIL = os.environ['EMAIL']

def get_user_token():
    user = {
        'full_name': FULL_NAME,
        'email': EMAIL
    }
    url = 'https://api-data-engineer-test-3bqvkbbykq-uc.a.run.app/user/'
    headers = {'Content-Type': 'application/json', 'accept': 'application/json'}
    response = requests.post(url, headers=headers, json=user)
    return response.json()['API Token']

def get_cars_data(token):
    url = f'https://api-data-engineer-test-3bqvkbbykq-uc.a.run.app/token={token}'
    headers = {'Content-Type': 'application/json', 'accept': 'application/json'}
    response = requests.get(url, headers=headers)
    return response.json()


if __name__ == '__main__':

    user_token = get_user_token()

    cars_data = get_cars_data(user_token)

    with open('cars_data.json', 'w') as file:
        file.write(json.dumps(cars_data, indent = 2))
