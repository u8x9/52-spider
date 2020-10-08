import requests

data = {
        'name': 'u8x9',
        'age': 99,
}

r = requests.get('https://httpbin.org/get', params=data)

print(type(r.text))
print(r.json())
print(type(r.json()))
