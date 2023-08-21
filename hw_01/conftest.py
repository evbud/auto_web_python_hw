"""Адрес сайта, имя пользователя и пароль хранятся в config.yaml
conftest.py содержит фикстуру авторизации по адресу https://test-stand.gb.ru/gateway/login
с передачей параметров “username" и "password" и возвращающей токен авторизации
Тест с использованием DDT проверяет наличие поста
с определенным заголовком в списке постов другого пользователя,
для этого выполняется get запрос по адресу https://test-stand.gb.ru/api/posts c хедером,
содержащим токен авторизации в параметре "X-Auth-Token".
Для отображения постов другого пользователя передается "owner": "notMe".

Условие: Добавить в задание с REST API ещё один тест, в котором создаётся новый пост,
а потом проверяется его наличие на сервере по полю «описание».
Подсказка: создание поста выполняется запросом к https://test-stand.gb.ru/api/posts
с передачей параметров title, description, content."""

import pytest
import yaml
import requests

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    username = data['username']
    password = data['password']
    address = data['address']
    address_posts = data['address_posts']
    title = data['title']
    description = data['description']
    content = data['content']

S = requests.Session()


@pytest.fixture()
def auth():
    rest1 = S.post(url=address, data={'username': username, 'password': password})
    return rest1.json()['token']


@pytest.fixture()
def post_title_my():
    return 'kitty'


@pytest.fixture()
def post_title_not_my():
    return ''


@pytest.fixture()
def create_post(auth):
    rest_post = S.post(url=address_posts, headers={'X-Auth-Token': auth}, data={'title': title,
                                                                                'description': description,
                                                                                'content': content,
                                                                                })
    return rest_post.status_code
