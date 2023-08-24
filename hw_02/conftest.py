"""вынести все локаторы элементов в фикстуры в conftest.py
вынести ожидаемый результат в фикстуру в conftest.py
добавить завершение работы Selenium после теста
вынести время ожидания в конфигурационный файл testdata.yaml

Доработать программу, полученную в предыдущем задании
добавив туда шаг, в котором будет проверяться успешность
входа пользователя при вводе верного имени и пароля.
Имя и пароль должны храниться в конфигурационном файле

Условие: Добавить в наш тестовый проект шаг добавления поста после входа.
Должна выполняться проверка на наличие названия поста на странице сразу после его создания.
Совет: не забудьте добавить небольшие ожидания перед и после нажатия кнопки создания поста."""

import pytest
import yaml

with open('testdata.yaml', encoding='utf-8') as f:
    userdata = yaml.safe_load(f)
    username = userdata['username']


@pytest.fixture()
def x_selector_1():
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
def x_selector_2():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def x_selector_3():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture()
def btn_login():
    return 'button'


@pytest.fixture()
def expected_result_1():
    return '401'


@pytest.fixture()
def x_selector_4():
    return """//*[@id="app"]/main/nav/ul/li[3]/a"""


@pytest.fixture()
def expected_result_2():
    return f'Hello, {username}'


@pytest.fixture()
def btn_create():
    return 'create-btn'


@pytest.fixture()
def selector_title():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""


@pytest.fixture()
def selector_description():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""


@pytest.fixture()
def selector_content():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""


@pytest.fixture()
def selector_img():
    return """//*[@id="create-item"]/div/div/div[6]/div/div/label/input"""


@pytest.fixture()
def btn_save():
    return """//*[@id="create-item"]/div/div/div[7]/div/button"""


@pytest.fixture()
def c_selector_title():
    return 'h1'
