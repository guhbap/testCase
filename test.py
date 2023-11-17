import requests


print("\n тест 1")
res = requests.post("http://127.0.0.1:8000/get_form", data={
    "email_field": "wex335@yandex.ru",
    "name_field": "wex335",
    "password_field": "tsdafoiuygsdfext"
    
}, headers={
     'Content-Type': 'application/x-www-form-urlencoded'
}, timeout=2)

print(res.text)

print("\n тест 2")

res = requests.post("http://127.0.0.1:8000/get_form", data={
    "email_field": "wex335@yandex.ru",
    "phone_field": "+7 989 274 82 79"
    
}, headers={
     'Content-Type': 'application/x-www-form-urlencoded'
}, timeout=2)

print(res.text)

print("\n тест 3")

res = requests.post("http://127.0.0.1:8000/get_form", data={
    "access_token": "oiuhg18765asd7g27897sdf",
    "content_field": "Привет мир!"
    
}, headers={
     'Content-Type': 'application/x-www-form-urlencoded'
}, timeout=2)

print(res.text)