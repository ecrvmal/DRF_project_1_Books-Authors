import requests
import time

DOMAIN = 'http://127.0.0.1:8000'


def timeout():
    time.sleep(2)


def get_url(url):
    return f'{DOMAIN}{url}'


timeout()

# не авторизован
response = requests.get(get_url('/api/authors/'))
assert response.status_code == 401

timeout()
# базовая авторизация
response = requests.get(get_url('/api/authors/'), auth=('user1', 'Vovka123'))
assert response.status_code == 200

timeout()
# авторизация по токену
TOKEN = 'e819c986b7757a56cca190fbf2de2703917e90b9'
# response = requests.get(get_url('/api/projects/'), headers={'Authorization': f'Token {TOKEN}'})
headers = {'Authorization': f'Token {TOKEN}'}
response = requests.get(get_url('/api/authors/'), headers=headers)
assert response.status_code == 200

timeout()

# авторизация по jwt
# Получаем токен
response = requests.post(get_url('/api/token/'), data={'username': 'user1', 'password': 'Vovka123'})
result = response.json()
# это наш токен
access = result['access']
print('Первый токен', access, end=f'\n{150 * "*"}\n')
# это для рефреша
refresh = result['refresh']
print('refresh', refresh, end=f'\n{150 * "*"}\n')
timeout()
# Авторизуемся с ним
headers = {'Authorization': f'Bearer {access}'}
response = requests.get(get_url('/api/authors/'), headers=headers)
assert response.status_code == 200

timeout()
# Рефрешим токен ( ДЛЯ ОБНОВЛЕНИЯ)
# по адресу /api/token/refresh/   запрашиваем new token
# refresh token  lifetime 2 дней
response = requests.post(get_url('/api/token/refresh/'), data={'refresh': refresh})
# print(response.status_code)
# print(response.text)
result = response.json()
# это наш токен
access = result['access']
print('Обновленный токен', access, end=f'\n{150 * "*"}\n')
print('refresh', refresh, end=f'\n{150 * "*"}\n')
timeout()
# Авторизуемся с ним
headers = {'Authorization': f'Bearer {access}'}
response = requests.get(get_url('/api/authors/'), headers=headers)
assert response.status_code == 200
