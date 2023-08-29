import requests

url = "http://api.open-notify.org/astros.json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    astronauts = data['people']

    print("Космонавти на орбіті:")
    for astronaut in astronauts:
        print(astronaut['name'])
else:
    print("Не вдалося отримати дані. Статус коду:", response.status_code)
