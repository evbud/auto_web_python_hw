import logging
import yaml
from selenium.common import TimeoutException
from BaseApp import BasePage
from selenium.webdriver.common.by import By


class TestSearchLocators:
    ids = dict()
    with open('locators.yaml', encoding='utf-8') as f:
        locators = yaml.safe_load(f)
    for locator in locators['xpath'].keys():
        ids[locator] = (By.XPATH, locators['xpath'][locator])
    for locator in locators['css'].keys():
        ids[locator] = (By.CSS_SELECTOR, locators['css'][locator])
    for locator in locators['id'].keys():
        ids[locator] = (By.ID, locators['id'][locator])


class OperationsHelper(BasePage):

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'Send {word} to element {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f'Element {locator} not found')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except TimeoutException:
            logging.exception(f'Exception while operating with {locator}')
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except TimeoutException:
            logging.exception('Exception with click')
            return False
        logging.debug(f'Clicked {element_name} button')
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except TimeoutException:
            logging.exception(f'Exception while getting text from {element_name}')
            return None
        logging.debug(f'Found text {text} in field {element_name}')
        return text

#  ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'], word, description='login form')

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_PASS_FIELD'], word, description='pass form')

    def enter_post_title(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_POST_TITLE'], word, description='post title form')

    def enter_post_description(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_POST_DESCRIPTION'], word,
                                   description='post description form')

    def enter_post_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_POST_CONTENT'], word,
                                   description='post content form')

    def enter_img_path(self, path):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_POST_IMG'], path, description='post image form')

    def enter_contact_name(self, contact_name):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_INPUT_YOUR_NAME'], contact_name,
                                   description='contact name')

    def enter_contact_email(self, contact_email):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_INPUT_YOUR_EMAIL'], contact_email,
                                   description='contact email')

    def enter_contact_content(self, content):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_INPUT_CONTENT'], content,
                                   description='contact content')

# CLICK
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_LOGIN_BTN'], description='login')

    def click_create_post_btn(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_CREATE_POST_BTN'], description='new post')

    def click_save_btn(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_SAVE_BTN'], description='save')

    def click_contact_link(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_CONTACT_LINK'], description='contact')

    def click_contact_us_btn(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_CONTACT_US_BTN'], description='contact us')

# GET TEXT
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_ERROR_FIELD'])

    def get_login_text(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_HELLO_LOGIN'])

    def get_added_post_title(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_POST_ADDED'])

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        logging.info(f'Got alert {text}')
        return text
