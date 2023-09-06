import logging
import yaml

from BaseApp import BaseRest

with open('testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)
    username = testdata['username']
    password = testdata['password']
    address = testdata['address']
    address_posts = testdata['address_posts']
    title = testdata['test_title']
    description = testdata['test_description']
    content = testdata['test_content']


def test_rest_my_title():
    logging.info('Test1 Rest starting')
    rest_session = BaseRest(address, username, password)
    posts = rest_session.get_own_posts(address_posts)
    assert 'kitty' in posts, 'Test1 Rest failed'


def test_rest_get_post():
    logging.info('Test2 Rest starting')
    rest_session = BaseRest(address, username, password)
    posts = rest_session.get_other_posts(address_posts)
    assert 'Test post' in posts, 'Test2 Rest failed'


def test_rest_new_post():
    logging.info('Test3 Rest starting')
    rest_session = BaseRest(address, username, password)
    new_post = rest_session.new_post(address_posts, title, description, content)
    assert description in new_post, 'Test3 Rest failed'
