import logging
import requests
from requests import JSONDecodeError

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://test-stand.gb.ru'

    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                             message=f"Can't find element by locator {locator}")
        except TimeoutException as e:
            logging.exception('Find element exception')
            logging.error(e)
            element = None
        return element

    def get_element_property(self, locator, el_property):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(el_property)
        else:
            logging.error(f'Property {el_property} not found in element with locator {locator}')
            return None

    def go_to_site(self):
        try:
            start_browsing = self.driver.get(self.base_url)
        except TimeoutException:
            logging.exception('Exception while open site')
            start_browsing = None
        return start_browsing

    def get_alert_text(self):
        try:
            alert = self.driver.switch_to.alert
            return alert.text
        except TimeoutException:
            logging.exception('Exception with alert')
            return None


class BaseRest:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.session = requests.Session()

    def login(self):
        rest = self.session.post(url=self.base_url, data={'username': self.username, 'password': self.password})
        return rest.json()['token']

    def get_token(self):
        token = ''
        try:
            token = self.login()
        except KeyError:
            logging.exception(f'{self.username} auth login')
        except JSONDecodeError:
            logging.exception(f'Auth page not found!')
        return token

    def get_own_posts(self, address_posts):
        logging.info('Getting titles of our posts...')
        token = self.get_token()
        results = []
        try:
            data = self.session.get(url=address_posts, headers={'X-Auth-Token': token}).json()['data']
            results = [i['title'] for i in data]
        except KeyError:
            logging.exception('Auth error')
        return results

    def get_other_posts(self, address_posts):
        logging.info('Getting titles of not our posts...')
        token = self.get_token()
        results = []
        try:
            data = self.session.get(url=address_posts,
                                    headers={'X-Auth-Token': token},
                                    params={'owner': 'notMe'}).json()['data']
            results = [i['title'] for i in data]
        except KeyError:
            logging.exception('Auth error')
        return results

    def new_post(self, address_posts, title, description, content):
        logging.info('Creating a new post...')
        token = self.get_token()
        descriptions = []
        try:
            self.session.post(url=address_posts,
                              headers={'X-Auth-Token': token},
                              data={'title': title, 'description': description, 'content': content})
            posts_info = self.session.get(url=address_posts,
                                          headers={'X-Auth-Token': token}).json()['data']
            descriptions = [i['description'] for i in posts_info]
        except KeyError:
            logging.exception('Auth error')
        return descriptions
