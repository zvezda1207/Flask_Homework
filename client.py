import requests

params = {
    'title': 'Куплю дом',
    'description': 'Дом 150 кв.м. 2020 года постройки',
    'owner': 'Иванова Наталья',
}

headers = {
    'Content-Type': 'application/json; charset=utf-8',
    'Accept': 'application/json; charset=utf-8'
}

r = requests.post('http://localhost:5000/adv', json=params, headers=headers)
print(r)
print(r.json())

