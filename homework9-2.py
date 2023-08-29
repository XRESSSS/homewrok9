import requests

url = "https://dummyjson.com/todos"
response = requests.get(url)

if response.status_code == 200:
    todos = response.json()

    incomplete_todos = [todo for todo in todos if not todo["completed"]]

    selected_todos = incomplete_todos[:150]

    for todo in selected_todos:
        print(f"ID: {todo['id']}, Завдання: {todo['title']}")
else:
    print(f"Помилка запиту: {response.status_code}")
