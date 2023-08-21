import requests
import yaml

S = requests.Session()
HTTP_RESPONSE_OK = 200

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    address = data['address_posts']
    description = data['description']


def test_my_title(auth, post_title_my):
    res = S.get(url=address, headers={'X-Auth-Token': auth}).json()['data']
    r = [i['title'] for i in res]
    assert post_title_my in r, 'Own title test (1) Failed'


def test_not_my_title(auth, post_title_not_my):
    res = S.get(url=address, headers={'X-Auth-Token': auth}, params={'owner': 'notMe'}).json()['data']
    r = [i['title'] for i in res]
    assert post_title_not_my in r, "Other user's title test (2) Failed"


def test_new_post(auth, create_post):
    res = S.get(url=address, headers={'X-Auth-Token': auth}).json()['data']
    r = [i['description'] for i in res]
    assert create_post == HTTP_RESPONSE_OK and description in r, 'New post test (3) Failed'
